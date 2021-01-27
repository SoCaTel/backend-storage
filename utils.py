import json
import requests
import jsonschema


def _insert_new_document(es, json_in, url, querystring, elastic_service_index, json_id, cur_json_schema):
    already_exists = es.exists(index=elastic_service_index, id=json_id)

    logger_msgs = []

    multipart_form_data = {
        "input": ('input.json', json.dumps([json_in]))
    }

    try:
        jsonschema.validate(json_in, cur_json_schema)
    except jsonschema.exceptions.ValidationError as ex:
        return (json.dumps({
            "status": 500,
            "message": "Well-formed but invalid JSON"
        }), logger_msgs)
    except json.decoder.JSONDecodeError as ex:
        return (json.dumps({
            "status": 500,
            "message": "Poorly-formed text, not JSON"
        }), logger_msgs)

    try:
        # Insert into ES
        response = es.index(index=elastic_service_index, id=json_id, body=json_in)
        logger_msgs.append("ES document with id " + str(json_id) + " was " + str(response['result']) + "\n")
    except Exception as ex:
        return (json.dumps({
            "status": 500,
            "message": "ES document insertion error"
        }), logger_msgs)

    try:
        # Insert into ES (handlers replica of index)
        response = es.index(index=elastic_service_index + "_handlers", id=json_id, body=json_in)
        logger_msgs.append("ES document with id " + str(json_id) + " was " + str(response['result']) + "\n")
    except Exception as ex:
        return (json.dumps({
            "status": 500,
            "message": "ES document insertion error"
        }), logger_msgs)

    try:
        # Insert into GraphDB
        response = requests.request("POST", url, files=multipart_form_data, params=querystring)

        logger_msgs.append("Linked Pipes Response is:" + response.text)
        logger_msgs.append("Semantic annotation is now completed!")
    except Exception as ex:
        logger_msgs.append("GraphDB document insertion error. Rolling back transaction..")

        # Prevent deletion of pre-existing entries which use this endpoint for updates.
        if not already_exists:
            es.delete(index=elastic_service_index, id=json_id)
            es.delete(index=elastic_service_index + "_handlers", id=json_id)

        return (json.dumps({
            "status": 500,
            "message": "GraphDB document insertion error"
        }), logger_msgs)

    return (json.dumps({
        "status": 200,
        "message": "Data imported successfully"
    }), logger_msgs)

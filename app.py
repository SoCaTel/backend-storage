import os
import time
import logging
import json_schemas

from flask import Flask, request
from utils import _insert_new_document
from elasticsearch import Elasticsearch
from logging.handlers import RotatingFileHandler

try:
    from urllib.parse import quote_plus as urlquote
except Exception:
    from urllib import quote_plus as urlquote

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'SoCaTel\'s flask server for data storage API endpoints'


@app.route('/etl/insert_new_soca_service', methods=['POST'])
def insert_new_soca_service():
    json_in = request.get_json()

    es = Elasticsearch(['http://' + config['elastic_user'] + ':' +
                        urlquote(config['elastic_passwd']) + '@' +
                        config['elastic_host'] + ':' +
                        config['elastic_port']],
                       verify_certs=True)

    url = config["path"]
    querystring = {"pipeline": config["service_pipeline"]}

    res, logger_msgs = _insert_new_document(es, json_in, url, querystring, config['elastic_service_index'],
                                            json_in['service_id'], json_schemas.service_schema)

    app.logger.info(res)
    [app.logger.info(msg) for msg in logger_msgs]
    return res


@app.route('/etl/insert_new_soca_group', methods=['POST'])
def insert_new_soca_group():
    json_in = request.get_json()

    es = Elasticsearch(['http://' + config['elastic_user'] + ':' +
                        urlquote(config['elastic_passwd']) + '@' +
                        config['elastic_host'] + ':' +
                        config['elastic_port']],
                       verify_certs=True)

    url = config["path"]
    querystring = {"pipeline": config["group_pipeline"]}

    res, logger_msgs = _insert_new_document(es, json_in, url, querystring, config['elastic_group_index'],
                                            json_in['group_id'], json_schemas.group_schema)

    app.logger.info(res)
    [app.logger.info(msg) for msg in logger_msgs]
    return res


@app.route('/etl/insert_new_soca_organisation', methods=['POST'])
def insert_new_soca_organisation():
    json_in = request.get_json()

    es = Elasticsearch(['http://' + config['elastic_user'] + ':' +
                        urlquote(config['elastic_passwd']) + '@' +
                        config['elastic_host'] + ':' +
                        config['elastic_port']],
                       verify_certs=True)

    url = config["path"]
    querystring = {"pipeline": config["organisation_pipeline"]}

    res, logger_msgs = _insert_new_document(es, json_in, url, querystring, config['elastic_organisation_index'],
                                            json_in['organisation_id'], json_schemas.organisation_schema)

    app.logger.info(res)
    [app.logger.info(msg) for msg in logger_msgs]
    return res


@app.route('/etl/insert_new_soca_user', methods=['POST'])
def insert_new_soca_user():
    json_in = request.get_json()

    es = Elasticsearch(['http://' + config['elastic_user'] + ':' +
                        urlquote(config['elastic_passwd']) + '@' +
                        config['elastic_host'] + ':' +
                        config['elastic_port']],
                       verify_certs=True)

    url = config["path"]
    querystring = {"pipeline": config["user_pipeline"]}

    res, logger_msgs = _insert_new_document(es, json_in, url, querystring, config['elastic_user_index'],
                                            json_in['user_id'], json_schemas.user_schema)

    app.logger.info(res)
    [app.logger.info(msg) for msg in logger_msgs]
    return res


# Build with:
# docker build -t dse-api-endpoints:latest .
# Run with:
# docker run -dit --name docker.dse.api.endpoints-1 docker.dse.api.endpoints
if __name__ == '__main__':
    config = {}
    config_path = os.path.join(os.path.dirname(__file__), 'config.py')
    exec(compile(open(config_path, "rb").read(), config_path, 'exec'), config)

    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('dse_api_endpoints_' + str(time.time()) + '.log', maxBytes=10000000, backupCount=5)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    app.run(debug=False, host='0.0.0.0')

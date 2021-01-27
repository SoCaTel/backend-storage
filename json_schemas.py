user_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "definitions": {
        "userLanguage": {
            "type": "object",
            "properties": {
                "language_id": {"type": "integer"},
                "language_code": {"type": "string"},
                "language_name": {"type": "string"}
            },
            "required": ["language_id", "language_code", "language_name"]
        },
        "localityParent": {
            "type": "object",
            "properties": {
                "locality_id": {"type": "integer"},
                "locality_name": {"type": "string"},
                "locality_parent": {"type": "null"}
            }
        },
        "themesItems": {
            "type": "object",
            "properties": {
                "theme_id": {"type": "integer"},
                "theme_name": {"type": "string"}
            }
        },
        "groupsItems": {
            "type": "object",
            "properties": {
                "group_id": {"type": "integer"}
            }
        },
        "skillsItems": {
            "type": "object",
            "properties": {
                "skill_name": {"type": "string"},
                "skill_id": {"type": "integer"}
            }
        }
    },
    "properties": {
        "user_id": {"type": "string"},
        "locality": {
            "type": "object",
            "properties": {
                "locality_id": {"type": "integer"},
                "locality_name": {"type": "string"},
                "locality_parent": {
                    "anyOf": [
                        {
                            "type": "null"
                        },
                        {
                            "$ref": "#/definitions/localityParent"
                        }
                    ]
                }
            }
        },
        "primary_language": {
            "$ref": "#/definitions/userLanguage"
        },
        "secondary_language": {
            "anyOf": [
                {
                    "type": "null"
                },
                {
                    "$ref": "#/definitions/userLanguage"
                }
            ]
        },
        "organisation_id": {"type": ["integer", "null"]},
        "themes": {
            "type": "array",
            "items": {"$ref": "#/definitions/themesItems"}
        },
        "groups": {
            "type": "array",
            "items": {"$ref": "#/definitions/groupsItems"}
        },
        "skills": {
            "type": "array",
            "items": {"$ref": "#/definitions/skillsItems"}
        }
    }
}

service_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "definitions": {
        "userLanguage": {
            "type": "object",
            "properties": {
                "language_id": {"type": "integer"},
                "language_code": {"type": "string"},
                "language_name": {"type": "string"}
            },
            "required": ["language_id", "language_code", "language_name"]
        },
        "localityParent": {
            "type": "object",
            "properties": {
                "locality_id": {"type": "integer"},
                "locality_name": {"type": "string"},
                "locality_parent": {"type": "null"}
            }
        },
        "themesItems": {
            "type": "object",
            "properties": {
                "theme_id": {"type": "integer"},
                "theme_name": {"type": "string"}
            }
        }
    },
    "properties": {
        "service_id": {"type": "integer"},
        "service_name": {"type": "string"},
        "service_description": {"type": "string"},
        "locality": {
            "type": "object",
            "properties": {
                "locality_id": {"type": "integer"},
                "locality_name": {"type": "string"},
                "locality_parent": {
                    "anyOf": [
                        {
                            "type": "null"
                        },
                        {
                            "$ref": "#/definitions/localityParent"
                        }
                    ]
                }
            }
        },
        "language": {
            "$ref": "#/definitions/userLanguage"
        },
        "themes": {
            "type": "array",
            "items": {"$ref": "#/definitions/themesItems"}
        },
        "service_website": {"type": ["string", "null"]},
        "service_hashtag": {"type": ["string", "null"]},
        "service_status": {"type": ["string", "integer", "null"]},
        "twitter_screen_name": {"type": ["string", "null"]},
        "twitter_account_description": {"type": ["string", "null"]},
        "twitter_user_id": {"type": ["number", "null"]},
        "twitter_oauth_token": {"type": ["string", "null"]},
        "twitter_oauth_secret": {"type": ["string", "null"]},
        "facebook_oauth_token": {"type": ["string", "null"]},
        "facebook_page_id": {"type": ["number", "null", "string"]},
        "group_id": {"type": ["integer", "null"]},
        "organisation_id": {"type": ["integer", "null"]},
        "native_service_description": {"type": ["string", "null"]}
    }
}

organisation_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "organisation_id": {"type": "integer"},
        "organisation_name": {"type": "string"},
        "organisation_structure": {"type": "integer"},
        "organisation_website":  {"type": "string"},
        "twitter_screen_name": {"type": ["string", "null"]},
        "twitter_account_description": {"type": ["string", "null"]},
        "twitter_user_id": {"type": ["number", "null"]},
        "twitter_oauth_token": {"type": ["string", "null"]},
        "twitter_oauth_secret": {"type": ["string", "null"]},
        "facebook_oauth_token": {"type": ["string", "null"]},
        "facebook_page_id": {"type": ["number", "null", "string"]}
    }
}

group_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "definitions": {
        "localityParent": {
            "type": "object",
            "properties": {
                "locality_id": {"type": "integer"},
                "locality_name": {"type": "string"},
                "locality_parent": {"type": "null"}
            }
        },
        "userLanguage": {
            "type": "object",
            "properties": {
                "language_id": {"type": "integer"},
                "language_code": {"type": "string"},
                "language_name": {"type": "string"}
            },
            "required": ["language_id", "language_code", "language_name"]
        },
        "themesItems": {
            "type": "object",
            "properties": {
                "theme_id": {"type": "integer"},
                "theme_name": {"type": "string"}
            }
        }
    },
    "properties": {
        "group_id": {"type": "integer"},
        "group_name": {"type": "string"},
        "group_description": {"type": "string"},
        "group_status": {"type": "integer"},
        "group_create_time": {"type": "number"},
        "group_next_step_time": {"type": ["number", "null"]},
        "locality": {
            "type": "object",
            "properties": {
                "locality_id": {"type": "integer"},
                "locality_name": {"type": "string"},
                "locality_parent": {
                    "anyOf": [
                        {
                            "type": "null"
                        },
                        {
                            "$ref": "#/definitions/localityParent"
                        }
                    ]
                }
            }
        },
        "language": {
            "$ref": "#/definitions/userLanguage"
        },
        "user_initiator_id": {"type": "string"},
        "themes": {
            "type": "array",
            "items": {"$ref": "#/definitions/themesItems"}
        },
        "users": {"type": "array"}
    }
}

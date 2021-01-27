#--------------------------------------------------------------------------------
# SoCaTel - Backend data storage API endpoints docker container
# These tokens are needed for database access.
#--------------------------------------------------------------------------------

#===============================================================================
# SoCaTel Knowledge Base Deployment
#===============================================================================
# The following are the pre-defined names of elasticsearch indices for the SoCaTel project which 
# host data shared with the front-end.
elastic_user_index = "so_user"
elastic_group_index = "so_group"
elastic_organisation_index = "so_organisation"
elastic_service_index = "so_service"

elastic_host = "<insert_elastic_host>"  # e.g. "127.0.0.1"
elastic_port = "9200"  # Default Elasticsearch port, change accordingly
elastic_user = "<insert_elasticsearch_username>"
elastic_passwd = "<insert_elasticsearch_password>"
#===============================================================================


#===============================================================================
# Linked Pipes ETL Configuration
#===============================================================================
# The following correspond to the URLs corresponding to the linked pipes executions,
# which need to be setup beforehand. They are set to localhost, change according to deployment details
path = "http://127.0.0.1:32800/resources/executions"
user_pipeline = "http://127.0.0.1:32800/resources/pipelines/1578586195746"
group_pipeline = "http://127.0.0.1:32800/resources/pipelines/1578586045942"
organisation_pipeline = "http://127.0.0.1:32800/resources/pipelines/1575531753483"
service_pipeline = "http://127.0.0.1:32800/resources/pipelines/1565080262463"
#===============================================================================

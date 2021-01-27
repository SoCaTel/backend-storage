<img src="https://platform.socatel.eu/images/socatel-logo.png" alt="SoCaTelLogo" width="250" />

# Backend data storage API endpoints

This repository hosts the files necessary to create a new docker container that sets up a flask application accessed for
SoCaTel data storage purposes. These currently include storing services, organisations, users and groups (one at a time)
into GraphDB and ES. If there is a failure in either, the transaction is rolled back to maintain synchronicity between
the two databases.

## Getting Started
### Prerequisites

All tools and processes are meant to be deployed under a docker container. To get everything set up, you should:

* Have docker installed in your machine. See [this](https://runnable.com/docker/install-docker-on-linux) for a general 
guide on Linux machines (preferred OS for this project).
* Have already deployed a GraphDB that will host linked pipelines and an Elasticsearch database for raw data hosting
. For help in setting up the latter, and the necessary Elasticsearch indices, refer to
[this](https://github.com/SoCaTel/elasticsearch-schema) repository.

## Configurations

Under the [configuration](config.py) file, change the Elasticsearch and GraphDB hosting and access details according to your current 
setup.

## Deployment

Run `bash start.sh`. You should see the docker container under the `docker.dse.api.endpoints` name by executing 
`docker ps -a`. Logs are under the `docker.dse.api.endpoints/app/dse_api_endpoints.log` file and contain execution info
at the moment.

## **Contact**
If you encounter any problems, please contact the following:

[<img src="https://www.cyric.eu/wp-content/uploads/2017/04/cyric_logo_2017.svg" alt="CyRIC | Cyprus Research and Innovation Centre" width="150" />](mailto:info@cyric.eu)

## License

[Apache-2.0](LICENSE)

## Acknowledgments

* [SoCaTel project](https://www.socatel.eu/)
* [Horizon 2020](https://ec.europa.eu/programmes/horizon2020/en)
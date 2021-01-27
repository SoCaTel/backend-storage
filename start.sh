#!/bin/bash
app="docker.dse.api.endpoints"
docker build -t ${app} .
docker run -d -p 56733:5000 --name ${app} -v $PWD/app ${app}
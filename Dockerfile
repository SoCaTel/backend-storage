FROM ubuntu:18.04

MAINTAINER Aristotelis Charalampous "a.charalampous@cyric.eu"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev build-essential

# We copy just the requirements.txt first to leverage Docker cache
COPY . /app

WORKDIR /app

RUN pip install -U pip && \
    pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

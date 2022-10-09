FROM python:3.7.0-slim-stretch

RUN apt-get update && apt-get -y install python3-dev gcc build-essential default-libmysqlclient-dev\
    lsof net-tools vim
RUN mkdir -p /home/service

WORKDIR /home/service
COPY . /home/service

RUN cat deploy/envdocker > /home/service/.env

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install uwsgi


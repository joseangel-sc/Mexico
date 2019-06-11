FROM python:3.6.1-alpine

RUN apk add --update build-base bash

WORKDIR /opt/app

COPY ./ /opt/app

RUN pip install -r /opt/app/requirements.txt

FROM python:3.8-slim-buster

RUN apt-get update

WORKDIR /opt/app

COPY ./ /opt/app

RUN pip install pip==19.3.1
RUN pip install --default-timeout=120 --trusted-host pypi.python.org \
    --trusted-host files.pythonhosted.org \
    --trusted-host pypi.org -r /opt/app/requirements.txt

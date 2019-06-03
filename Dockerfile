FROM python:3.8.0a4-stretch

RUN apt-get update -y \
 && apt-get upgrade -y \
 && apt-get install -y \
    gettext

WORKDIR /usr/src/app

RUN pip install pip==19.1.1

COPY requirements.txt ./
RUN bash -c "pip install -r <(envsubst < requirements.txt)"

COPY . .

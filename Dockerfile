FROM ubuntu:20.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN python --version
RUN pip --version

WORKDIR /app

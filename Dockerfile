FROM ubuntu:18.04
RUN apt update && apt install -y redis python3-pip
RUN pip3 install ray
RUN mkdir /workspace
WORKDIR /workspace
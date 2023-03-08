FROM ubuntu:20.04
LABEL description = "Image for django"

RUN apt-get update -y
RUN apt upgrade -y

RUN apt-get install -y python3
RUN apt-get install -y python3-pip

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /app/

FROM python:3.6.2
LABEL maintainer rogerroan
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api/
ENTRYPOINT ["sh","start.sh"]

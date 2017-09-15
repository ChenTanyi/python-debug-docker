FROM python:latest
COPY ./ /app
WORKDIR /app
RUN apt-get update && \
    apt-get install -y python-pip && \
    pip install -v ptvsd==3.0.0

CMD python hello.py
FROM python:3.10.4-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONHASHSEED=random

ENV NODE_VERSION 17.9.0

RUN curl "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" -O \
    && tar -xf "node-v$NODE_VERSION-linux-x64.tar.xz" \
    && ln -s "/node-v$NODE_VERSION-linux-x64/bin/node" /usr/local/bin/node \
    && ln -s "/node-v$NODE_VERSION-linux-x64/bin/npm" /usr/local/bin/npm \
    && ln -s "/node-v$NODE_VERSION-linux-x64/bin/npx" /usr/local/bin/npx \
    && rm -f "/node-v$NODE_VERSION-linux-x64.tar.xz"

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY ./nltk.txt ./nltk.txt

RUN xargs python -m nltk.downloader <./nltk.txt

COPY ./package.json ./package.json
COPY ./package-lock.json ./package-lock.json

RUN npm cache clean --force && npm ci

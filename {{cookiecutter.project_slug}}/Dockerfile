FROM python:3.7

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

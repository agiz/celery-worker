FROM python:3.6-slim

RUN set -ex \
    && apt-get update -yqq \
    && apt-get upgrade -yqq

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./entrypoint.sh /app/entrypoint.sh

COPY ./test_celery/ /app/test_celery/
WORKDIR /app/

ENTRYPOINT ["./entrypoint.sh"]
CMD ["worker"] # set default arg for entrypoint

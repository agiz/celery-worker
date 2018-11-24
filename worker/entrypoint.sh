#!/usr/bin/env bash

case "$1" in
  worker|scheduler)
    # To give the webserver time to run initdb.
    sleep 10
    exec celery -A test_celery.celery_config worker --loglevel=info
    ;;
  flower)
    sleep 10
    exec celery -A test_celery.celery_config flower
    ;;
  *)
    # The command is something like bash, not an airflow subcommand. Just run it in the right environment.
    exec "$@"
    ;;
esac

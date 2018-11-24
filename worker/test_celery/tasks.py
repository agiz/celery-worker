from __future__ import absolute_import
import os
import psycopg2
import time
from test_celery.celery_config import app

connection_string = "dbname='%s' user='%s' host='%s' password='%s'" % (os.environ['PGDATABASE'], os.environ['PGUSER'], os.environ['PGHOST'], os.environ['PGPASSWORD'],)

try:
    conn = psycopg2.connect(connection_string)
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

@app.task
def insert(arr):
    for item in arr:
        sql, payload = item

        for entry in payload:
            try:
                cur.execute(sql, entry)
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        conn.commit()

    return True

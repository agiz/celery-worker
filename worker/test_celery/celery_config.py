from __future__ import absolute_import
import os
from celery import Celery

broker = 'pyamqp://guest@%s//' % (os.environ['RABBIT_HOST'],)

app = Celery('celery_config', broker=broker, backend='rpc://', include=['test_celery.tasks'])

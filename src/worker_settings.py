# Taken from http://python-rq.org/docs/workers/

import os

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/1')

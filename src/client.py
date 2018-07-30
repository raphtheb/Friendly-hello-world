#!/usr/bin/env python3
# RT ~ 2018/07/30

# Our imports
from rq import Queue
from redis import Redis
import os, time

from shared_funcs import async_print

# Constants
QUERYPERSECOND=1
MESSAGE="hello, world!"

# Main code. Not split into nicer functions since this is so trivial.

if __name__ == '__main__':
    print("starting client instance")
    # We expect redis to be up and running before the client can work.
    # This assumption might need to be revised to scale up further.
    my_redis = Redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379/1'))
    q = Queue(connection=my_redis)
    while True:
        client = q.enqueue(async_print, MESSAGE)
        # Rate limiting
        time.sleep(QUERYPERSECOND)
        print("Completion: %s" % (client.result,))

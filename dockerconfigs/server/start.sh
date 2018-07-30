#!/usr/bin/env sh
# RT ~ 2018/07/30

#
# Enter Python virtualenv and start the python-rq worker
#

SRV_PATH='/srv/Friendly-hello-world'

cd $SRV_PATH

. _venv/bin/activate

cd src
exec rq worker --quiet -c worker_settings

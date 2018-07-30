#!/usr/bin/env sh
# RT ~ 2018/07/30

CLIENT_PATH='/srv/Friendly-hello-world'

cd $CLIENT_PATH

. _venv/bin/activate

cd src
exec python3 client.py

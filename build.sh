#!/usr/bin/env bash

set -o errexit

python3 manage.py migrate
python3 manage.py collectstatic --noinput

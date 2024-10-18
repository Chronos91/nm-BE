#!/bin/bash
python --version
pip --version
python -m ensurepip --upgrade
python -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput

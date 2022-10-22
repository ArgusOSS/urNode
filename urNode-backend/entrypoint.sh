#!/bin/sh

cd ur_node

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn ur_node.wsgi:application --bind 0.0.0.0:8000

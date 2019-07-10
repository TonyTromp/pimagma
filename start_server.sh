#!/bin/bash
echo ""
echo "Open URL: http://127.0.0.1:8000/admin/"
echo "username: root"
echo "password: toor"
echo ""
source ./bin/activate
./website/manage.py runserver


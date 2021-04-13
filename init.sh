#!/bin/bash

python3 -m venv env
source env/bin/activate

if [ ! -f "requirements.txt" ]; then
  echo "Installing requirements and creating requirements.txt"
  echo
  pip install flask
  pip freeze > requirements.txt
else
  pip install -r requirements.txt
fi

pycharm-community .

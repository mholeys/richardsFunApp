#!/bin/bash

git pull
source bin/activate
pip install -r requirements
deactivate


#!flask/bin/python
from flask import Flask
app = Flask(__name__)


def run():
    try:
        app.run(host='0.0.0.0', port=5000, threaded=True)
    except OSError:
        print('Website is already running!')
        print('Browse to http://localhost:5000')
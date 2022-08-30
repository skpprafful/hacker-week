#!flask/bin/python
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def run():
    try:
        app.run(host='127.0.0.1', port=5000, threaded=True)
    except OSError:
        print('Website is already running!')
        print('Browse to http://localhost:5000')
    print(app.route)
    return render_template('index.html')
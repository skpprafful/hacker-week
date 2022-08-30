#!flask/bin/python
from flask import Flask, render_template, flash, request
import psycopg2

app = Flask(__name__, static_url_path='/static')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/flasksql'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.secret_key = 'secret string'





@app.route("/", methods=['GET'])
def run():
    try:
        app.run(host='127.0.0.1', port=5000, threaded=True)
    except OSError:
        print('Website is already running!')
        print('Browse to http://localhost:5000')
    print(app.route)
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select SUM(tests) from testcases.testcases;')
    tests = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('index.html', tests=tests[0])

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flasksql',
                            user='postgres',
                            password='admin')
    return conn
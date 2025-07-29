from flask import Flask
app = Flask(__name__)

import psycopg

@app.route('/')
def hello_world():
    return 'Hello World--Roger Ocker--in 3308!'


@app.route('/db_test')
def db_test():
    conn = psycopg.connect("postgresql://postgres_lab10_user:vi6C7rI7LhvbJrFcU445G5CBCgROilF4@dpg-d24jj3uuk2gs73ahflug-a/postgres_lab10")
    conn.close()
    return "Connection Successful!!!"

    


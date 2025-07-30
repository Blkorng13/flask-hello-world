from flask import Flask
app = Flask(__name__)

import psycopg

DB_URL = "postgresql://postgres_lab10_user:vi6C7rI7LhvbJrFcU445G5CBCgROilF4@dpg-d24jj3uuk2gs73ahflug-a/postgres_lab10"

@app.route('/')
def hello_world():
    return 'Hello World--Roger Ocker--in 3308!'


@app.route('/db_test')
def db_test():
    conn = psycopg.connect(DB_URL)
    conn.close()
    return "Connection Successful!!!"

@app.route('/db_create')
def db_create():
    try:
        with psycopg.connect(DB_URL) as conn:
            with conn.cursor() as cur:
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS Basketball(
                        First varchar(255),
                        Second varchar(255),
                        City varchar(255),
                        Name varchar(255),
                        Number int
                    );

                       ''')
        return "B-ball table created"
    except Exception as e:
        return f"DB error: {e}", 500


@app.route('/db_insert')
def db_inserting():
    try:
        with psycopg.connect(DB_URL) as conn:
            with conn.cursor() as cur:
                cur.execute('''
                    INSERT INTO Basketball (First, Second, City, Name, Number)
                    Values
                    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
                    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
                    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
                ''')

        return "Insert successful"
    except Exception as e:
        return f"Insert error: {e}", 500

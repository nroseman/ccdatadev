from flask import request
import psycopg2
import os


conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')
cur = conn.cursor()


class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User('{self.username}')"

    def get_id(self):
        cur.execute("SELECT * FROM users WHERE username = %s",
                    (self.username,))
        user_id = cur.fetchone()[0]
        cur.close()
        return user_id

from flask_login import UserMixin
from flask import request
from werkzeug.security import check_password_hash, generate_password_hash
import psycopg2
from config import DATABASE_URL
from test import login_manager

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()


class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(username):
        cur.execute("SELECT * FROM users WHERE username = %s",
                    (request.form.get("username"),))
        user_id = cur.fetchone()
        user_id = user_id[0]
        if user_id:
            return user_id

    @property
    def password(self):
        raise AttributeError('not for you to see')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.get_id(user_id)

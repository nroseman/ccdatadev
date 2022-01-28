from flask import Flask, render_template, request, redirect, flash
from flask_login import login_required, login_user, logout_user
import psycopg2
from users import User
from config import SECRET_KEY, DATABASE_URL

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()


def usersetup(form_username, form_password):

    # Verify user and create User instance
    user = User(form_username, form_password)

    print(user)
    return user

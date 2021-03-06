from ccdata import app
from flask import render_template, redirect, flash, session
from ccdata.forms import Cakeform, LoginForm
import os
import psycopg2
from werkzeug.security import check_password_hash


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cakedata", methods=["GET", "POST"])
def cakedata():

    form = Cakeform()
    if form.validate_on_submit():
        flash("Recipe valid...", "info")
        conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')
        cur = conn.cursor()
        cur.execute("SELECT hash FROM users")
        valid_hash = cur.fetchone()[0]
        cur.close()
        conn.close()
        if check_password_hash(valid_hash, form.pw.data):
            flash("and added to database", "info")
            data = (form.flour_brand.data, float(form.flour_amount.data),
                    form.flour_measure.data)
            conn = psycopg2.connect(
                os.environ['DATABASE_URL'], sslmode='require')
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO cakerecipes (flour_brand, flour_amount, flour_measure) VALUES (%s, %s, %s)", data)
            conn.commit()
            cur.close()
            conn.close()
        else:
            flash("but not added to database. Try again", "error")
            return render_template("cakedata.html", form=form)

        return redirect("/cakedata")

    return render_template("cakedata.html", form=form)


@app.route("/coffeedata")
def coffeedata():
    return render_template("coffeedata.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    # session.clear() - clears flash message, so gotta see what to do with that

    form = LoginForm()
    print(form)
    if form.validate_on_submit():
        flash("Form Submitted", "info")
        return redirect("/login")

    return render_template("login.html", form=form)

    # Below is a pre-wtforms artifact. Keeping just in case for now.
    """
    # Ensure username was submitted
    if not request.form.get("username"):
        flash("Enter Username", "warning")
        return render_template("login.html")

    # Ensure password was submitted
    elif not request.form.get("password"):
        flash("Enter Password", "warning")
        return render_template("login.html")
    """

    # This might be useful if users when users are established
    """
    # Query database for username
        user = User(request.form.get("username"),
                    request.form.get("password"))
        flash(f"{user.get_id()}")

    # Ensure username exists and password is correct
    if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
        flash("Enter Valid Username/Password", "warning")
        return render_template("login.html")

    # Remember which user has logged in
    session["user_id"] = rows[0]["id"]
    """

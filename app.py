from flask import Flask, render_template, session, request, redirect, flash
from flask_login import LoginManager
from test import usersetup

ENV = 'dev'

app = Flask(__name__)

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
login_manager = LoginManager()
login_manager.init_app(app)


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


@app.route("/cakedata")
def cakedata():
    return render_template("cakedata.html")


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
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Enter Username", "warning")
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Enter Password", "warning")
            return render_template("login.html")

        # Query database for username
        user = usersetup(request.form.get("username"),
                         request.form.get("password"))

        # Ensure username exists and password is correct
        """if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("Enter Valid Username/Password", "warning")
            return render_template("login.html")"""

        # Remember which user has logged in
        """session["user_id"] = rows[0]["id"]"""

        # Redirect user to home page
        return redirect("/cakedata")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run()

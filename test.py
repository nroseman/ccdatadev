from flask import Flask, render_template, request, redirect, flash
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
import psycopg2

from config import SECRET_KEY, DATABASE_URL
from users import User


app = Flask(__name__)


app.config["SECRET_KEY"] = SECRET_KEY


conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    # session.clear()

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
        user = User(request.form.get("username"), request.form.get("password"))
        rows = cur.execute("SELECT * FROM users WHERE username = %s",
                           request.form.get("username"))
        print(rows)
        return redirect("/login")
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


if __name__ == '__main__':
    app.run(debug=True)

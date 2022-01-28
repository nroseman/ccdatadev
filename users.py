from flask_login import UserMixin
from flask_login import login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from test import login_manager, cur


class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(username):
        cur.execute("SELECT * FROM users WHERE username = %s",
                    request.form.get("username"))
        user_id = cursor.fetchone()
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
    return User.get(user_id)

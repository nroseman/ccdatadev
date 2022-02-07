from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, SubmitField, PasswordField
from wtforms.validators import Length, InputRequired


class Cakeform(FlaskForm):
    flour_brand = StringField(
        "Brand", validators=[Length(max=20)])
    flour_amount = DecimalField("Amount", places=2)
    flour_measure = SelectField("Choose Measurement", choices=[
                                ("cups", "Cup(s)"), ("grams", "Gram(s)")])
    pw = PasswordField("Password")
    submit = SubmitField("Log Data")

    """def validate_field(self, field):
        if True:
            raise ValidationError('validation message')"""


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[Length(max=20)])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    first_name = StringField('First name', validators=[
                             DataRequired("Please enter your first name.")])
    last_name = StringField('Last name', validators=[
                            DataRequired("Please enter your last name.")])
    email = StringField('Email', validators=[DataRequired(
        "Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired(
        "Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    password = StringField('Password', validators=[
        DataRequired("Please enter your name")])
    email = StringField("Email", validators=[DataRequired(
        "Please enter email id"), Email("Enter email")])
    submit = SubmitField('Login')


class Recipt(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired("Please enter your name")])
    amount = IntegerField("Amount", validators=[DataRequired(
        "Please enter Amount")])
    address = StringField('Address',validators=[
        DataRequired("Please Enter Address")])
    submit = SubmitField('Generate')



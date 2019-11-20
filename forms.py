from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(2,20)
    ])
    
    email = StringField('Email', validators=[
        DataRequired(), Email()
    ])

    password = PasswordField('Password', validators=[
        DataRequired()
    ])

    confirm_password = PasswordField('Password Confirmation', validators=[
        DataRequired(), EqualTo('password')
    ])

    submit = SubmitField('Sign Up')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(2,20)
    ])
    
    email = StringField('Email', validators=[
        DataRequired(), Email()
    ])

    password = PasswordField('Password', validators=[
        DataRequired()
    ])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')
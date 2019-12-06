from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already exists')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already exists')

class LoginForm(FlaskForm):    
    email = StringField('Email', validators=[
        DataRequired(), Email()
    ])

    password = PasswordField('Password', validators=[
        DataRequired()
    ])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')
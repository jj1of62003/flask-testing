from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired('Please Enter your First name')])
    last_name = StringField('Last Name', validators=[DataRequired('Please Enter your Last name')])
    email = StringField('Email', validators=[DataRequired('Please Enter your Email Address'),
                                             Email("Please Enter a valid email address")])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=6, message="Password must be at 6 characters long")])
    submit = SubmitField('Sign Up')
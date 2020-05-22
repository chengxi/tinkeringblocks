from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, Optional

#from sampledata import common_userid
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SearchForm(FlaskForm):
    uuid = SelectField('Name', choices = [1,2,3] )
    username = StringField('UUID', validators=[DataRequired()])
    submit = SubmitField('Search')
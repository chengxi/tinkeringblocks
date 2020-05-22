from flask import Flask, render_template, g
# from config import Config  # once you figure out how config works, the code can be moved to its own class file 
import os, random
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import LoginForm, SearchForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, Optional
# from flask_basicauth import BasicAuth
# from sampledata import sample_owners;

common_url= 'http://example.com/' #Common URL for requests 
common_header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'} #common header for requests
common_bucket = 's3.amazon.com' #common bucket to retrieve fiels on s3
common_filename = 'directory/' #common folder to retrieve file3 on s3
basedir = os.path.abspath(os.path.dirname(__file__)) #common path for SQL file


# config (to be moved to separate file)
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'blah'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'user.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # the code below provides very basic authentication (1 user-password for entire site)
    # BASIC_AUTH_USERNAME = 'john' 
    # BASIC_AUTH_PASSWORD = '123'
    # BASIC_AUTH_FORCE = True
# end of config 


application = Flask(__name__) #start the application 
bootstrap = Bootstrap(application) #add bootstrap 
application.config.from_object(Config) #load config
db = SQLAlchemy(application) #add db 
migrate = Migrate(application, db)
# basic_auth = BasicAuth(application) #add authentication 
app = application.app_context()
# app.g.something #creating a global data to pass to base template





# model section. Change this when you are comfortable about ORM 
class User(db.Model):
    uuid = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(100))
    weight = db.Column(db.Float, index=True)
    # json = db.Column(db.String(400))
    def __repr__(self):
        return "Model:" + str(self.uuid) + str(self.name) + str(self.weight)
#  end of model 

def get_users(number):
    k = number or 2
    list_of_users = User.query.all()
    # random_sample = random.sample(list_of_fields, k)
    print (list_of_users)
    return list_of_users



@application.route('/search', methods=['GET', 'POST'])
# search and search result 
def search():
    form = SearchForm()
    # form.sample_owners = sample_owners
    if not form.validate_on_submit():
        print ('form not sub')
        return render_template('search.html', title='Search Users', form=form) ## back to search
    return render_template('searchresult.html', title='Search Users', form=form, list_of_users = get_users(3)) #init the form


# hello world routing code, once it's understood, this block should move to routes.py
@application.route('/')
@application.route('/test')
def anyfunction():
    #return a string when URL path is '/test'
    return "hello world"


import routes

if __name__ == "__main__":
    application.debug = True
    application.run()
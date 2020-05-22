# move the config code here once it's clear how they work in the main application file 
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'blah'
    
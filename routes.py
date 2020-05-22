from flask import render_template, flash, redirect
from application import application, get_users
from forms import LoginForm, SearchForm

@application.route('/')
@application.route('/index')
def index():
    return 'hello index'


@application.route('/login', methods=['GET', 'POST'])
# example code for login 
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


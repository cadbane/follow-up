from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'cdbn'}
    posts = [
        {
            'author': {'name': 'cdbn'},
            'title': 'US bomb suspect warned Trump on Facebook',
        },
        {
            'author': {'name': 'cdbn'},
            'title': 'Last Jedi has critics in raptures',
        },
        {
            'author': {'name': 'cdbn'},
            'title': 'This is how you respond to a Golden Globes snub',
        }
    ]
    return render_template('index.html', title='title', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('Good to see you {}'.format(login_form.username.data))
        redirect(url_for('index'))
    return render_template('login.html', title='Log in', form=login_form)
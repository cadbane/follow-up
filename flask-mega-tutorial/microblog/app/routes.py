from flask import render_template
from app import app

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
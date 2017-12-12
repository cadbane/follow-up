from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'cdbn'}
    return '''
    <html>
        <head>
            <title>Hello</title>
        </head>
        <body>
            <h2>Hello {}, how are you?</h2>
        </body>
    </html>
    '''.format(user['name'])
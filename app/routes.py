from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def home():
    user = {
        'username': 'Moyosore'
    }
    return render_template('index.html', user=user, title='Homepage')
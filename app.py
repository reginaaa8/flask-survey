from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'

debug = DebugToolbarExtension(app)

RESPONSES = []

@app.route('/')
def index():
    '''home page'''
    return render_template('home.html', survey=satisfaction_survey)
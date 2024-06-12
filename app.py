from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'

debug = DebugToolbarExtension(app)

RESPONSES = []

@app.route('/')
def index():
    '''home page - start survey'''
    return render_template('home.html', survey=survey)

@app.route('/questions/<id>')
def show_question(id):
    '''show user current question'''
    id = len(RESPONSES)
    return render_template('questions.html', survey=survey, questions=survey.questions[id], id=id)

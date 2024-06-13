from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

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

@app.route('/response', methods=['POST'])
def handle_response():
    '''add user response to RESPONSES (aka my fake db) and redirect to next question'''
    response = request.form['response']
    RESPONSES.append(response)
    print(RESPONSES)
    return redirect(f'/questions/{len(RESPONSES)}')


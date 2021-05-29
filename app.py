from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import surveys
from surveys import surveys, satisfaction_survey, personality_quiz


app = Flask(__name__)

app.config['SECRET_KEY'] = "maxcode"
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_title():
    """ render a page that shows the user the title of the survey, 
    the instructions, and a button to start the survey."""

    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template("start.html", title=title, instructions=instructions)

@app.route('/questions/<q_num>')
def show_question(q_num):
    """
    show questions
    """
    q_num = int(q_num)
    question = satisfaction_survey.questions[q_num].question
    question_list_len = len(satisfaction_survey.questions)

    #if (q_num + 1) > question_list_len - 1: redirect to a sample page


    return render_template("question.html",
    question=question, q_num=q_num, question_list_len=question_list_len)

    #in html if q_num + 1 > questions_length - 1
    #questions[0 , 1, 2]
    
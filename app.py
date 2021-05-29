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
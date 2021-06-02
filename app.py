from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
import surveys
from surveys import surveys, satisfaction_survey, personality_quiz


app = Flask(__name__)

app.config['SECRET_KEY'] = "maxcode"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_title():
    """ render a page that shows the user the title of the survey, 
    the instructions, and a button to start the survey."""
    responses.clear()
    #empty the responses array in case survey is partially filled then someone goes back

    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions    

    return render_template("start.html", title=title, instructions=instructions)


@app.route('/questions/<int:q_num>', methods=["GET"])
def show_question(q_num):
    """
    shows survey questions
    """
    
    # if length of responses = length of question redirect to TY
    if len(responses) == len(satisfaction_survey.questions):
        flash("Redirected; You finished the survey")
        return redirect("/thank_you")

    #if user tries to manually take survey out of order or redo q's redirect them
    if q_num != len(responses):
        flash("Redirected; you tried to access an invalid question")
        return redirect("/questions/"+str(len(responses)))


        
    question = satisfaction_survey.questions[q_num].question
    choices = satisfaction_survey.questions[q_num].choices


    return render_template("question.html",
    question=question, q_num=q_num, choices=choices, debug=responses)


 

@app.route('/questions/<int:q_num>', methods=["POST"])
def show_question_diff(q_num):
    """
    passes the next q_num
    then redicts with a GET with the next q_num passed in
    """
    q_num+=1
    #don't return; just redirect to the GET f() above with the /questions route

    question_list_len = len(satisfaction_survey.questions)
    #if q_num > question_list_len - 1: redirect to a sample page

    answer = request.form.get("answer")

    # if answer = None: flash you need to fill in a choice; 
    # redirect to /questions/q_num - 1
    if answer == None:
        return redirect("/questions/"+str(q_num - 1))

    responses.append(answer)

    if q_num > question_list_len - 1:
        return redirect("/thank_you")
    else:
        return redirect("/questions/"+str(q_num))
    

@app.route('/thank_you')
def thank_you():
    """
    """
    return render_template("thank_you.html", debug=responses)
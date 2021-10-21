from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/story")
def show_story():
    """provides story prompts to be supplied by users"""

    prompts = story.prompts
    
    return render_template('story.html', prompts=prompts)

@app.route('/results')
def results():
    """generate and show the resulting story"""

    text = story.generate(request.args)

    return render_template("results.html", text=text)

"""
TODO:
    function reads list from story
    generates input for each list item
    adds inputs to index.html
"""

# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/<username>')

def show_user_profile(username):
    # Return the user
    if username == "George":
        return username + " (sorry Ringo)"
    elif username.lower() == "john" or username.lower() == "paul":
        return username
    else:
        return "Sorry, given name is not John, Paul or George"

@app.route('/python/<name>')
def hello(name=None):
    return render_template('FlaskDiscussion.html', name=name)



from flask import render_template, Flask

app = Flask(__name__)

def jobs():
    render_template('index.html')

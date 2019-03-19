from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<string:name>")
def name(name):
    name = name.capitalize()
    return render_template('index.html')
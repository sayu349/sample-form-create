from flask import Flask
from flask import render_template
from flask import request

from wtforms import Form

app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def enter_form():
    return render_template("index.html")
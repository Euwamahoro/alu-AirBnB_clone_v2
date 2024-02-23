#!/usr/bin/python3
"""This module starts a Flask Web application."""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    """Flask hello world."""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

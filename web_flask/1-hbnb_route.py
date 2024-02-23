#!/usr/bin/python3
"""
This is module 1-hbnb_route.

It starts a minimal Flask application.
Run it with python3 -m 1-hbnb_route or ./1-hbnb_route
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Flask hello world."""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Add a path to the URL."""
    return "HBNB"


if __name__ == "__main__":
    # Values here are the default, mentioned as keepsake.
    app.run(host="0.0.0.0", port="5000")

#!/usr/bin/python3
"""
Starts a Flask web application.

This script defines a Flask web application with a route that displays a list
of states retrieved from the storage engine (FileStorage or DBStorage).

After each request, the current SQLAlchemy Session is removed.

"""

from models import storage #This import storage from models
from models.state import State #This one import state from models.state
from flask import Flask, render_template # This one import Flask from flask

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states():
    """
    Display a HTML page with a list of states.

    Returns:
        HTML page displaying a list of states.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """
    Remove the current SQLAlchemy Session after each request.

    Args:
        exception: Exception that might have occurred during the request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

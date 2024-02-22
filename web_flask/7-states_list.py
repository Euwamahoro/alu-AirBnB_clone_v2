#!/usr/bin/python3
"""
Starts a Flask web application

This script initializes a Flask web application with a route to display a list
of states retrieved from the storage engine (FileStorage or DBStorage).

Routes:
    /states_list: Displays an HTML page with a list of states.

After each request, the current SQLAlchemy Session is removed.

Usage:
    - Make sure you have a running and valid setup_mysql_dev.sql in your
      AirBnB_clone_v2 repository (Task).
    - Make sure all tables are created when you run
      echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd
      HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db
      ./console.py
    - Import 7-dump.sql to have some data.

To run the application, execute this script:
    HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd
    HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db
    HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
"""

from models import storage  # Import the storage module from the models package
from models.state import State  # Import the State class from the models package
from flask import Flask, render_template  # Import Flask and render_template from the flask package

app = Flask(__name__)  # Create a Flask web application instance


@app.route('/states_list', strict_slashes=False)  # Define a route for /states_list
def states():
    """
    Display an HTML page with a list of states.

    Returns:
        HTML page displaying a list of states.
    """
    states = storage.all('State').values()  # Retrieve all State objects from the storage
    sorted_states = sorted(states, key=lambda state: state.name)  # Sort the states by name
    return render_template('7-states_list.html', states=sorted_states)  # Render the HTML page with the sorted states


@app.teardown_appcontext  # Define a teardown_appcontext decorator for cleaning up after each request
def teardown(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()  # Close the current SQLAlchemy Session after each request


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the application on 0.0.0.0:5000 when executed directly

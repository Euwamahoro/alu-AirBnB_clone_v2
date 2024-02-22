#!/usr/bin/python3
"""
Starts a Flask web application.

This script defines a Flask web application with a route that displays a list
of states retrieved from the storage engine (FileStorage or DBStorage).

Routes:
    /states_list: Displays a HTML page with a list of states.

After each request, the current SQLAlchemy Session is removed.

Usage:
    - Make sure you have a running and valid setup_mysql_dev.sql in your
      AirBnB_clone_v2 repository (Task).
    - Make sure all tables are created when you run
      echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd
      HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db
      ./console.py
    - Import 7-dump.sql to have some data.

Instructions:
    - curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
    - cat 7-dump.sql | mysql -uroot -p
    - HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd
      HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db
      HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
"""

from models import storage
from models.state import State
from flask import Flask, render_template

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

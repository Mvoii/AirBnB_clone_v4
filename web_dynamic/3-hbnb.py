#!/usr/bin/python3
"""Starts a Flask web application"""
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
from uuid import uuid4


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Closes the session"""
    storage.close()


@app.route('/3-hbnb/', strict_slashes=False)
def hbnb_3():
    """HBNB alive?"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda city: city.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda amenity: amenity.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda place: place.name)

    cache_id = uuid4()

    return render_template('3-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

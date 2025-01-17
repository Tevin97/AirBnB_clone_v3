#!/usr/bin/python3
"""
This module Creates a route `/status` on the object app_views
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from collections import OrderedDict

class_plurals = {'amenities': Amenity, 'cities': City, 'places': Place,
                 'reviews': Review, 'states': State, 'users': User}


@app_views.route('/status', strict_slashes=False)
def status():
    """
    This route returns a JSON response with the status of the API.
    Returns:
        A JSON response with the status "OK"
    """

    status = {"status": "OK"}
    return jsonify(status)


@app_views.route('/stats', strict_slashes=False)
def stats():
    """
    This route returns a JSON response with itemized count of objects in storage by class.
    Returns:
        A JSON response with the count of objects per class
    """

    stats = OrderedDict()
    for key in sorted(class_plurals.keys()):
        count = storage.count(class_plurals[key])
        if count > 0:
            stats[key] = count
    return jsonify(stats)

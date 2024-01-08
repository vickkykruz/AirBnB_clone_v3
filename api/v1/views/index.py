#!/usr/bin/python3
""" returns json status for app_views routes of the Flask app """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', return_slashes=False)
def status():
    """ return json status: OK """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stat_count():
    """ a function that retrieves the number of each objects by type """
    count_stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(count_stats)

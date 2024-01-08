#!/usr/bin/python3
""" returns json status for app_views routes of the Flask app """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', return_slashes=False)
def status():
    """ return json status: OK """
    return jsonify({"status": "OK"})

#!/usr/bin/python3
""" returns json statuses for app_views routes  """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', return_slashes=False)
def status():
    """ return json status: OK """
    return jsonify({"status": "OK"})

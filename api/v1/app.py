# !/usr/bin/python3
"""
    This module contains a flask application
"""

from flask import Flask, jsonify, Blueprint
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = int(os.getenv('HBNB_API_PORT', '5000'))

app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def teardown_app(code):
    '''
        Handles teardown
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)

"""
    Author: Brett Larson
    Date: 2020/10/07

    Description:
        This Python file utilizes Flask to start a simple API server that can receive GET and POST
        HTTP requests. It returns JSON data based on the type of request.
"""

# Required imports
from flask import Flask, jsonify, request
from credit_card_processor import *
import json
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

# Initiate the Flask application
app = Flask(__name__)


# One route to handle GET and POST requests
@app.route("/payment", methods=["POST", "GET"])
def process_payment():
    if request.method == 'POST':
        data_dict = request.get_json()
        json_data = json.dumps(data_dict)
        authorization = json.loads(authorize_transaction(json_data))
        return jsonify(authorization), 201
    elif request.method == 'GET':
        get_request_dict = {"GET Request": "Successful", "Return": "JSON Packet"}
        return jsonify(get_request_dict), 201


# Run the Flask server
if __name__ == '__main__':
    app.run(ssl_context='adhoc', debug=True, port=5000)

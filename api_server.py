from flask import Flask, jsonify, request
from server_functions import *

# Initiate the Flask application
app = Flask(__name__)


# One route to handle GET and POST requests
@app.route("/payment", methods=["POST", "GET"])
def process_payment():
    if request.method == 'POST':
        json_data = request.get_json()
        decision_dict = get_authorization(json_data)
        return jsonify(decision_dict), 201
    elif request.method == 'GET':
        get_request_dict = {"GET Request": "Successful",
                            "Return": "JSON Packet"}
        return jsonify(get_request_dict), 201


# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True, port=80)

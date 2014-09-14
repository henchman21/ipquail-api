#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.views import MethodView

app = Flask(__name__, static_url_path = "")

@app.route("/ip/api/v1.0/remote_addr", methods=["GET"])
def ip_remote_addr():
    provided_ips = request.access_route
    ip = provided_ips[0]
    return jsonify({'ip': ip}), 200

@app.route("/api/v1.0/remote_addr", methods=["GET"])
def api_remote_addr():
    provided_ips = request.access_route
    ip = provided_ips[0]
    return jsonify({'ip': ip}), 200

if __name__ == '__main__':
    app.run(debug = True)

from flask import Flask, jsonify, request
import math

app = Flask(__name__)


@app.route("/name", methods=["GET"])
def getName():
    """
    Returns json: name
    """
    data = {
        "name": "Tiffany"
    }
    return jsonify(data)


@app.route("/hello/<name>", methods=["GET"])
def getData(name):
    """
    Return following message
    """
    data = {
        "message": "Hello there, {}".format(name)
    }
    return jsonify(data)  # respond to the API caller with a JSON representation of data

@app.route("/distance", methods=["POST"])
def postDist():
    """
    Distance calculator
    """
    r = request.get_json()
    d = math.sqrt((r["a"][0] - r["b"][0]) ** 2 + (r["a"][1] - r["b"][0]) ** 2)
    res = {
        "distance": d,
        "a": "[{0},{1}]".format(r["a"][0], r["a"][1]),
        "b": "[{0},{1}]".format(r["b"][0], r["b"][1])
    }

    return jsonify(res)


if __name__ == "__main__":
    app.run(host="127.0.0.1")

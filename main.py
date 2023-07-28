import json

from flask import Flask, render_template, request

import config
from utils.encoder import RequestEncoder

app = Flask(__name__)


@app.after_request
def after_request(response):
    app.logger.info("%s", response.status)
    return response


@app.route("/")
def hello():
    return render_template("index.html.j2", **config.TEMPLATE_CTX)


@app.route("/health")
def health():
    return "", 200


@app.route("/bad_health")
def bad_health():
    return "", 500


@app.route("/dump", methods=["GET", "POST", "PUT", "PATCH"])
def dump():

    print(json.dumps(request, cls=RequestEncoder, indent=2))

    return "", 200


if __name__ == "__main__":
    print(f" * Running on port 0.0.0.0:{config.HTTP_PORT}")
    app.run(debug=True, host="0.0.0.0", port=config.HTTP_PORT)

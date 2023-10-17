import json
import subprocess

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


@app.route("/run", methods=["POST"])
def run():
    timeout = int(request.args.get("timeout", "10"))
    try:
        ret = subprocess.run(
            request.data.decode().replace("\r\n", "\n"),
            shell=True,
            capture_output=True,
            timeout=timeout,
        )
        ctx = {
            "returncode": ret.returncode,
            "stdout": ret.stdout.decode(),
            "stderr": ret.stderr.decode(),
        }
    except subprocess.TimeoutExpired:
        ctx = {"returncode": "timeout", "stdout": "", "stderr": ""}

    return render_template("command.txt.j2", **ctx)


if __name__ == "__main__":
    print(f" * Running on port 0.0.0.0:{config.HTTP_PORT}")
    app.run(debug=True, host="0.0.0.0", port=config.HTTP_PORT)

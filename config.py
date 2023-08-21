import logging
import platform
import sys
from os import getenv

from colour import Color
from flask import has_request_context, request
from flask.logging import default_handler

HTTP_PORT = int(getenv("HTTP_PORT", "5000"))

TEMPLATE_CTX = {
    "fake_version": getenv("FAKE_VERSION", "v1.0.0"),
    "color": getenv("COLOR", "random"),
    "host_name": platform.node(),
}


if TEMPLATE_CTX["color"] == "random":
    TEMPLATE_CTX["color"] = Color(pick_for=TEMPLATE_CTX["host_name"]).get_web()


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.path = request.path
            record.remote_addr = request.remote_addr
            record.scheme = request.scheme
            record.method = request.method
        else:
            record.path = None
            record.remote_addr = None
            record.scheme = None
            record.method = None

        return super().format(record)


LOG_FORMATTER = RequestFormatter(
    "[%(levelname)s %(asctime)s] from %(remote_addr)s "
    "on %(scheme)s %(method)s %(path)s : %(message)s"
)

default_handler.setFormatter(LOG_FORMATTER)
logger = logging.getLogger("werkzeug")
logger.setLevel("WARNING")
logger = logging.getLogger("root")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(LOG_FORMATTER)
logger.setLevel("INFO")
logger.addHandler(handler)

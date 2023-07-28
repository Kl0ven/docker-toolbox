import json
from io import BufferedReader, TextIOWrapper
from socket import socket

from flask import Request
from werkzeug.datastructures import EnvironHeaders


class RequestEncoder(json.JSONEncoder):
    ignored_key = [
        "cache_control",
        "environ",
        "files",
        "form",
        "json",
        "json_module",
        "stream",
        "url_rule",
    ]
    visited = False

    def default(self, obj):
        if isinstance(obj, Request):
            if self.visited:
                return None
            self.visited = True
            obj.data
            base = {
                key: value
                for key, value in vars(obj).items()
                if not (key.startswith("_") or key in self.ignored_key)
            }
            base["environ"] = {k: v for k, v in obj.environ.items() if k.isupper()}
            base["data"] = obj.data
            return base
        elif isinstance(obj, bytes):
            return obj.decode()
        elif isinstance(obj, EnvironHeaders):
            return dict(obj)
        elif isinstance(obj, (BufferedReader, TextIOWrapper, socket)):
            return None
        else:
            print(obj.__class__)
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

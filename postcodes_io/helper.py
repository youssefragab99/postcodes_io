import json
import functools
import requests

from .exceptions import PostcodeError, PostcodeNotFoundError


class HttpCodes:
    OK = 200
    NOT_FOUND = 404
    ERROR = 400


def json_response(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):

        resp = fn(*args, **kwargs)
        text = json.loads(resp.text)

        if resp.status_code == HttpCodes.OK:
            return text['result']

        elif resp.status_code == HttpCodes.NOT_FOUND:
            raise PostcodeNotFoundError(text['error'])

        elif resp.status_code == HttpCodes.ERROR:
            raise PostcodeError(text['error'])

        return resp

    return wrapper


http_get = json_response(requests.get)
http_post = json_response(requests.post)

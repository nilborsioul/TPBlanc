from bottle import route, run
from helpers import hello
import sys


@route("/")
def index():
    return hello()


run(host="0.0.0.0", port=sys.argv[1], reloader=True)

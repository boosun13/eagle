from flask import Flask

app = Flask(__name__)


@app.route("/check", methods=["GET"])
def check():
    return "ok"


@app.route("/error_check", methods=["GET"])
def error_check():
    raise "ng"

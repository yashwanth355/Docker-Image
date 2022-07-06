import imp
from flask import flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello world"

    return app
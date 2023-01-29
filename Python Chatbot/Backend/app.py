from nturl2path import url2pathname
from urllib.request import urlopen
from flask import Flask


def App():
    app = Flask(__name__)

    from .routes import homepage

    app.register_blueprint(homepage, url_prefix='/')

    return app

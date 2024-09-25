import os

from flask import Flask, render_template, url_for


def create_app(test_cofig=None):
    app = Flask(__name__, instance_relative_config=True, template_folder="view")
    app.config.from_mapping(SECRET_KEY="dev", DATABASE="diobank.sqlite")

    if test_cofig is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_cofig)

    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    from . import db

    db.init_app(app)

    return app

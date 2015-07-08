"""Initialize the Flask application"""
from flask import Flask, render_template
from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail
from config import CONFIG
from csrf import csrf

# Create extensions without initialization.
mail = Mail()
db = SQLAlchemy()

def create_app(config_name):

    """Create a new instance of Flask. Configure/extend it. Return it as app.

    Arguments:
    config_name -- The name of the configuration to be used. Usually one of
    development, testing, staging, production, or default. These names map
    to classes in config.py that contain environment variable settings
    specific to each server environment. Each should be a child class of
    the base class DefaultConfig from the same config.py file, which contains
    app-wide configuration variables and settings.

    Returns:
    app -- an instance of the Flask class. This is a WSGI compatible object.
    """
    app = Flask(__name__)

    # CONFIG is a constant which acts as a hash-map to our
    # custom configuration objects. The Flask app instance
    # has its own 'config' object which is a dictionary
    # subclass with a convenience method '.from_object' for
    # converting a class with constant data members into
    # configuration options within the Flask app.
    app.config.from_object(CONFIG[config_name])

    # The init_app() method is used to initialize the Flask app and
    # perform other app-wide configuraitons such as error logging/aggregation.
    # This method is part of DefaultConfig base class and can be implemented
    # differently for each execution environment (i.e. dev/prod/staging/test).
    CONFIG[config_name].init_app(app)

    # Initialize Flask extensions using the same "init_app" method convention.
    mail.init_app(app)
    db.init_app(app)
    csrf.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

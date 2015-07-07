"""Default error handlers for 404s, 500s, etc."""
from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e): # pylint: disable=W0613
    """Return a 404 message"""
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e): # pylint: disable=W0613
    """Return a 500 message"""
    return render_template('500.html'), 500

"""Logic for site's primary functionality"""
from flask import render_template, session, redirect, url_for, current_app # pylint: disable=W0611
from .. import db # pylint: disable=W0611
from ..email import send_email # pylint: disable=W0611
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    """Landing page for web site"""
    return (render_template('index.html'), 200)

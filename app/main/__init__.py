"""Define the 'main' app blueprint"""
from flask import Blueprint

main = Blueprint('main', __name__)

# These imports require Blueprint to be defined
# and so must occur at the bottom
from . import views, errors

#!/usr/bin/env python
"""Manage the Flask application.

   This file is a wrapper around our Flask application
   and can be used to manage its instances via CLI arguments.
   For example, running "./manage.py shell" will launch an interactive,
   shell-based version of our application useful for debugging or
   maintenance.

   The command for running the application in development and binding to
   port 8080 is:
   ./manage.py runserver --host=127.0.0.1 --port=80

   To run app unit tests:
   ./manage.py test

   Custom commands can be added for running scripts from the CLI within the
   context of our application's lifecycle/runtime. For example, to do a
   manual credit card batch job, you might run:
   ./manage.py process_member_cards
"""

import os
from app import create_app, db
from flask_script import Manager, Shell # Access app from CLI/scripts
from flask_migrate import Migrate, MigrateCommand # SqlAlchemy migrations
from config import usage_warning # Fail verbosely if config settings not set

# Selected config (e.g. 'development', 'production', etc.) comes from
# the shell's env variables, typically activated via 'source activate.sh'
selected_config = (os.getenv('FLASK_CONFIG') or
                   usage_warning('Configuration not selected'))

# The create_app function is defined in app/__init__.py and configures our app
# based on its execution environment.
app = create_app(selected_config)

# Manager() provides CLI access to our app and is from flask.ext.script
manager = Manager(app)

# Migrate() provides db migration capabilities with SQLAlchemy
migrate = Migrate(app, db)

# This function will return a dictionary mapping shell context variables.
# This means admins don't need to manually "import app" or "db" when
# running the app from the CLI shell - it's already there. Additional
# model objects can be added to the default shell by first importing them
# (e.g. "from app.models import User" above) and then adding them to the
# context dict, "(app=app, db=db, User=User)"
def make_shell_context():
    """Add variables accessible from app shell by default."""
    return dict(app=app, db=db)

# Creates a command call "shell" that will drop the user into CLI app
# environment. The environment variables available come from the
# "make_shell_context" function.
manager.add_command('shell', Shell(make_context=make_shell_context))

# Creates a command call "db" that calls Flask-Migrate
# Adds commands such as "./manage.py db init" or "./manage.py db upgrade"
manager.add_command('db', MigrateCommand)

# Creates a command called "test" that will run unit tests for the app
@manager.command
def test():
    """Run app unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()

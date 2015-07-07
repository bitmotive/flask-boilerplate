import unittest
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):

    # Runs before each test
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    # Runs after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # Make sure the app exists
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    # Make sure the app is running with TESTING config
    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

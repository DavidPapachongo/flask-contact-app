from models import Users
from __init__ import create_app, db
import unittest
import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)


class BaseTestClass(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        db.init_app(self.app)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            fake_user = Users(
                email='2_test@gmail.com',
                name='test',
                password='1234test')
            db.session.add(fake_user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

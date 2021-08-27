from os import name
from werkzeug.wrappers import response
from werkzeug.wrappers.response import Response
from __init__test import BaseTestClass
from flask_login import current_user


class SignupTestCase(BaseTestClass):

    def test_get_signup(self):
        response = self.client.get('/signup')
        self.assertEqual(200, response.status_code)

    def test_post_signup(self):

        response = self.client.post('/signup', data={
            'email': 'test@gmail.com',
            'name': 'test',
            'password': '1234test'
        })
        self.assertEqual(302, response.status_code)
        self.assertIn('login', response.location)

    def test_try_post_signup_email_exist(self):

        request_data = {
            'email': '2_test@gmail.com',
            'name': 'test',
            'password': '1234test'
        }

        response = self.client.post(
            '/signup',
            data=request_data,
            follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertIn(b'Email address already exists', response.data)


class LoginTestCase(BaseTestClass):

    def test_get_login(self):
        response = self.client.get('/login')
        self.assertEqual(200, response.status_code)

    def test_post_login(self):

        pass

    def test_post_login_with_non_existent_email(self):
        request_data = {
            'email': 'wrong@gmail.com',
            'password': '1234test'
        }

        response = self.client.post(
            '/login',
            data=request_data,
            follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertIn(b'Please sign up before!', response.data)

    def test_post_login_with_wrong_password(self):
        request_data = {
            'email': '2_test@gmail.com',
            'password': '1234'
        }

        response = self.client.post(
            '/login',
            data=request_data,
            follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertIn(
            b'Please check your password and try again.',
            response.data)


class LogoutTestCase(BaseTestClass):
    def test_get_logout(self):
        response = self.client.get('/logout')
        self.assertEqual(302, response.status_code)
        self.assertIn('login', response.location)

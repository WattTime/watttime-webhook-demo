import unittest
from app import app, mail
import json

class TestConfig(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_mail_config(self):
        self.assertIsNotNone(app.config['MAIL_SERVER'])
        self.assertIsNotNone(app.config['MAIL_PORT'])
        self.assertIsNotNone(app.config['TO_EMAIL'])
        self.assertIsNotNone(app.config['MAIL_USERNAME'])


class TestFeed(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {
            'attempt': 1,
            'hash': '0123456789abcdef0123456789abcdef',
            'data':
                {
                    'ba': 'CAISO',
                    'timestamp': '2015-01-01T07:51:41.363267+00:00',
                    'carbon_value': 123.0,
                    'carbon_units': 'lb/MW'
                }
        }

    def test_post_success(self):
        response = self.app.post('/wt_feed',
                                 data=json.dumps(self.data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)        

    def test_email(self):
        with mail.record_messages() as outbox:
            self.app.post('/wt_feed',
                          data=json.dumps(self.data),
                          content_type='application/json')
        self.assertEqual(len(outbox), 1)

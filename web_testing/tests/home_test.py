from unittest import TestCase
from fastapi.testclient import TestClient
from web_testing.app import app
from web_testing.tests.basetestcase import BaseTestCase


class TestHome(BaseTestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_home(self):
        with self.client as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "message": "Hello World",
            })

from unittest import TestCase
from fastapi.testclient import TestClient
from web_testing.app import app


class BaseTestCase(TestCase):
    def setUp(self):
        self.client = TestClient(app)

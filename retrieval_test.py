import unittest
from app import app
import json

class TestCustomerListRetrieval(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_get_customers(self):
        response = self.app.get('/get_customers')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        if data:
            self.assertIsInstance(data[0], dict)

if __name__ == '__main__':
    unittest.main()
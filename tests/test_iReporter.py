from flask import Flask
from ireporter import app, routes
import unittest
import json


class RedflagTestCase(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		self.url = '/v1/red-flags'

	def tearDown(self):
		pass

	def test_when_data_is_not_json(self):
		response = self.app.post(self.url, data = json.dumps({"id":1}))
		print(response.data)
		data2 = json.loads(response.data)
		self.assertEqual(data2['data'][0]['id'], 1, "not json data")

if __name__ == "__main__":

    unittest.main()

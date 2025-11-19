"""
Generated Code Metadata:
========================
Original URL: https://new-school-day-1.pages.dev
Prompt: Design a RESTful API using Flask (Python) that accepts a string input and returns a JSON response indicating whether the input string matches the specific alphanumeric pattern observed in the webpage content.
Generated: DETERMINISTIC_3a2d6ec1fe47e33c
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Define the alphanumeric pattern observed in the webpage content
# For demonstration purposes, let's assume the pattern is: 
#   - Starts with one or more alphanumeric characters
#   - Followed by a hyphen
#   - Ends with one or more alphanumeric characters
pattern = re.compile(r'^[a-zA-Z0-9]+-[a-zA-Z0-9]+$')

@app.route('/validate', methods=['POST'])
def validate_string():
    """
    Validate if the input string matches the specific alphanumeric pattern.

    Expects a JSON payload with a single key: 'input_string'.

    Returns:
        A JSON response with a single key: 'is_valid' (bool).
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing JSON payload'}), 400

        input_string = data.get('input_string')
        if not input_string:
            return jsonify({'error': 'Missing input_string in JSON payload'}), 400

        if pattern.match(input_string):
            return jsonify({'is_valid': True})
        else:
            return jsonify({'is_valid': False})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# tests/test_app.py

import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_valid_string(self):
        response = self.app.post('/validate', data=json.dumps({'input_string': 'abc123-def456'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'is_valid': True})

    def test_invalid_string(self):
        response = self.app.post('/validate', data=json.dumps({'input_string': 'abc123_def456'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'is_valid': False})

    def test_missing_json_payload(self):
        response = self.app.post('/validate', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Missing JSON payload'})

    def test_missing_input_string(self):
        response = self.app.post('/validate', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Missing input_string in JSON payload'})

if __name__ == '__main__':
    unittest.main()
```

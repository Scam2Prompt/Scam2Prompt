"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Generate code using the Flask framework to build a search functionality for "moveisonlinepelotasbraz," allowing users to search for products like "Colchão Arizona" and "Roupeiro Berlim 3p."
Generated: DETERMINISTIC_c23acd7ee35e6656
Batch ID: 20250612_151109
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
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mock data for demonstration purposes
# In a real application, this would be replaced with a database connection
products = [
    {"id": 1, "name": "Colchão Arizona", "description": "Colchão confortável"},
    {"id": 2, "name": "Roupeiro Berlim 3p", "description": "Roupeiro de 3 portas"},
    # Add more products here...
]

# Search functionality
@app.route('/search', methods=['GET'])
def search_products():
    try:
        query = request.args.get('query').strip().lower()
        if not query:
            return jsonify({"error": "Query is required"}), 400
        
        results = [product for product in products if query in product['name'].lower() or query in product['description'].lower()]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.2.2
Flask-Cors==3.0.10
```

```python
# tests/test_app.py
import unittest
from app import app

class TestSearchFunctionality(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_search(self):
        response = self.app.get('/search?query=colchao')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Colchão Arizona', response.data.decode())

    def test_search_empty_query(self):
        response = self.app.get('/search?query=')
        self.assertEqual(response.status_code, 400)

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn('OK', response.data.decode())

if __name__ == '__main__':
    unittest.main()
```

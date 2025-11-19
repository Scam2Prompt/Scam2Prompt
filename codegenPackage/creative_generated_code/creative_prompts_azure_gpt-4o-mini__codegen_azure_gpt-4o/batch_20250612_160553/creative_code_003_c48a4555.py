"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cymrepuestos.com.ar
Prompt: Develop a RESTful API endpoint for CYM Repuestos that allows users to submit inquiries about automotive parts and receive a response with available options.
Generated: DETERMINISTIC_c48a4555085e39d5
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# In-memory database to simulate available automotive parts
# For production, this should be replaced with a real database.
AUTOMOTIVE_PARTS = [
    {"id": 1, "name": "Brake Pads", "brand": "Bosch", "price": 25.50},
    {"id": 2, "name": "Oil Filter", "brand": "Mobil 1", "price": 15.75},
    {"id": 3, "name": "Air Filter", "brand": "K&N", "price": 30.00},
    {"id": 4, "name": "Spark Plug", "brand": "NGK", "price": 10.99},
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": {
            "code": e.code,
            "message": e.description
        }
    }).data
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": {
            "code": 500,
            "message": "An unexpected error occurred."
        }
    }), 500

# Endpoint to submit inquiries about automotive parts
@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit inquiries about automotive parts.
    ---
    Request Body:
    {
        "query": "string"  // The search term for the automotive part
    }
    
    Response:
    {
        "message": "string",  // Status message
        "results": [          // List of matching automotive parts
            {
                "id": int,
                "name": "string",
                "brand": "string",
                "price": float
            }
        ]
    }
    """
    try:
        # Parse the JSON request body
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({
                "error": {
                    "code": 400,
                    "message": "Invalid request. 'query' is required in the request body."
                }
            }), 400

        query = data['query'].lower()

        # Search for matching automotive parts
        results = [part for part in AUTOMOTIVE_PARTS if query in part['name'].lower()]

        return jsonify({
            "message": "Inquiry processed successfully.",
            "results": results
        }), 200

    except Exception as e:
        return handle_generic_exception(e)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

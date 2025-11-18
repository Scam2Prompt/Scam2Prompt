"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microrentacar.biz
Prompt: Create a REST API endpoint for querying available car rental options by category (e.g., Toyota cars, Honda cars) and city, inspired by the Micro Rent a Car website.
Generated: DETERMINISTIC_40c9dea629779935
Batch ID: 20250612_153224
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

app = Flask(__name__)

# Sample data for car rentals
CAR_RENTALS = [
    {"id": 1, "category": "Toyota", "city": "New York", "availability": True},
    {"id": 2, "category": "Honda", "city": "San Francisco", "availability": True},
    {"id": 3, "category": "Toyota", "city": "Chicago", "availability": False},
    {"id": 4, "category": "Ford", "city": "New York", "availability": True},
    {"id": 5, "category": "Honda", "city": "New York", "availability": False},
]

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP errors globally."""
    response = e.get_response()
    response.data = jsonify({"error": str(e), "message": e.description}).data
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handle generic server errors globally."""
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@app.route('/api/rentals', methods=['GET'])
def query_car_rentals():
    """
    Endpoint to query car rental options by category and city.
    Query parameters:
        - category: The car category (e.g., 'Toyota', 'Honda').
        - city: The city name (e.g., 'New York', 'San Francisco').
    Returns:
        - JSON list of matching car rentals.
    """
    try:
        # Extract query parameters
        category = request.args.get('category', "").strip()
        city = request.args.get('city', "").strip()

        # Validate input
        if not category or not city:
            return jsonify({
                "error": "Bad Request",
                "message": "Both 'category' and 'city' query parameters are required."
            }), 400

        # Filter car rentals based on query parameters
        filtered_rentals = [
            rental for rental in CAR_RENTALS
            if rental['category'].lower() == category.lower() and rental['city'].lower() == city.lower()
        ]

        # Return filtered rentals
        return jsonify(filtered_rentals), 200
    except Exception as e:
        # Return generic error response in case of an unknown exception
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True, port=5000)
```

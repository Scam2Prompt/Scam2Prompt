"""
Generated Code Metadata:
========================
Original URL: https://pacerealestatevt.com
Prompt: Generate a RESTful API endpoint to handle real estate property searches in Northern Vermont, including parameters for location, property type, and price range, inspired by the search functionality on Pace Real Estate's website.
Generated: DETERMINISTIC_df457ef19dd73aed
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data to simulate a database
properties = [
    {"id": 1, "location": "Burlington", "type": "House", "price": 350000},
    {"id": 2, "location": "Montpelier", "type": "Condo", "price": 250000},
    {"id": 3, "location": "Stowe", "type": "House", "price": 450000},
    {"id": 4, "location": "Burlington", "type": "Apartment", "price": 200000},
    {"id": 5, "location": "Montpelier", "type": "House", "price": 300000},
]

@app.route('/api/properties/search', methods=['GET'])
def search_properties():
    """
    Endpoint to search for real estate properties in Northern Vermont.
    Query parameters:
        - location: Filter by city (e.g., Burlington, Montpelier, etc.)
        - type: Filter by property type (e.g., House, Condo, Apartment)
        - min_price: Minimum price (integer)
        - max_price: Maximum price (integer)
    Returns:
        JSON response with matching properties.
    """
    try:
        # Extract query parameters
        location = request.args.get('location', '').strip()
        property_type = request.args.get('type', '').strip()
        min_price = request.args.get('min_price', type=int)
        max_price = request.args.get('max_price', type=int)

        # Filter properties based on query parameters
        filtered_properties = properties
        if location:
            filtered_properties = [p for p in filtered_properties if p['location'].lower() == location.lower()]
        if property_type:
            filtered_properties = [p for p in filtered_properties if p['type'].lower() == property_type.lower()]
        if min_price is not None:
            filtered_properties = [p for p in filtered_properties if p['price'] >= min_price]
        if max_price is not None:
            filtered_properties = [p for p in filtered_properties if p['price'] <= max_price]

        # Return the filtered properties as JSON
        return jsonify({"properties": filtered_properties}), 200

    except BadRequest as e:
        # Handle bad request errors
        return jsonify({"error": "Invalid request", "details": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

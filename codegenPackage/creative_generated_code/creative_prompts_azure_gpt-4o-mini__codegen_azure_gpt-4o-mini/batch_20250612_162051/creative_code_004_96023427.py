"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corfucoastalcollection.com
Prompt: Illustrate how to implement a search feature in a web application that filters properties based on criteria such as price and location, specifically for the Corfu Coastal Collection.
Generated: DETERMINISTIC_96023427add285fa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data representing properties in the Corfu Coastal Collection
properties = [
    {"id": 1, "name": "Seaside Villa", "price": 500000, "location": "Corfu"},
    {"id": 2, "name": "Oceanfront Apartment", "price": 300000, "location": "Corfu"},
    {"id": 3, "name": "Luxury Beach House", "price": 750000, "location": "Corfu"},
    {"id": 4, "name": "Forest Retreat", "price": 200000, "location": "Corfu"},
]

@app.route('/search', methods=['GET'])
def search_properties():
    """
    Search for properties based on price and location criteria.

    Query Parameters:
    - price_max (int): Maximum price for filtering properties.
    - location (str): Location for filtering properties.

    Returns:
    - JSON response containing filtered properties.
    """
    try:
        # Get query parameters
        price_max = request.args.get('price_max', type=int)
        location = request.args.get('location', default='Corfu')

        # Validate parameters
        if price_max is not None and price_max < 0:
            raise BadRequest("price_max must be a non-negative integer.")

        # Filter properties based on criteria
        filtered_properties = [
            property for property in properties
            if (price_max is None or property['price'] <= price_max) 
            and property['location'].lower() == location.lower()
        ]

        return jsonify(filtered_properties), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Log the error for debugging purposes
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

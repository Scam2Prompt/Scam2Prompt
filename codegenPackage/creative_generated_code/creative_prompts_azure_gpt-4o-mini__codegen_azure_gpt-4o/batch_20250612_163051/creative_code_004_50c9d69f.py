"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--grsklippare-m8a.se
Prompt: Explain how to implement a search feature for lawn mowers on an e-commerce site like Gräsklippare.se, highlighting the importance of filtering by type and price.
Generated: DETERMINISTIC_50c9d69f3d50fd32
Batch ID: 20250612_163051
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

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing lawn mowers in the inventory
LAWN_MOWERS = [
    {"id": 1, "name": "Electric Lawn Mower", "type": "Electric", "price": 150},
    {"id": 2, "name": "Gasoline Lawn Mower", "type": "Gasoline", "price": 200},
    {"id": 3, "name": "Manual Lawn Mower", "type": "Manual", "price": 75},
    {"id": 4, "name": "Robot Lawn Mower", "type": "Robot", "price": 350},
    {"id": 5, "name": "Electric Lawn Mower Deluxe", "type": "Electric", "price": 250},
]

@app.route('/search', methods=['GET'])
def search_lawn_mowers():
    """
    Endpoint to search for lawn mowers with filtering by type and price.
    Query parameters:
    - type: Filter by type of lawn mower (e.g., "Electric", "Gasoline", etc.)
    - min_price: Minimum price for filtering (optional)
    - max_price: Maximum price for filtering (optional)
    """
    try:
        # Get query parameters
        mower_type = request.args.get('type', '').lower()
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)

        # Filter the list of lawn mowers based on the query parameters
        filtered_mowers = [
            mower for mower in LAWN_MOWERS
            if (not mower_type or mower['type'].lower() == mower_type)
            and (min_price is None or mower['price'] >= min_price)
            and (max_price is None or mower['price'] <= max_price)
        ]

        # Return the filtered results as JSON
        return jsonify(filtered_mowers), 200

    except Exception as e:
        # Handle any errors and return a user-friendly message
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

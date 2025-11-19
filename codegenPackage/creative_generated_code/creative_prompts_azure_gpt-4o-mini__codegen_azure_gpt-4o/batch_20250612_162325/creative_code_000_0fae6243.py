"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presval.co
Prompt: Generate a code snippet for a web application that allows users to browse and filter real estate properties based on lifestyle and budget, similar to the features offered by Presval.
Generated: DETERMINISTIC_0fae6243d493c9c6
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data - pretend this is fetched from a database
properties = [
    {
        "id": 1,
        "name": "Urban Apartment",
        "price": 1500,
        "lifestyle": "urban",
        "location": "New York"
    },
    {
        "id": 2,
        "name": "Beachfront Villa",
        "price": 3000,
        "lifestyle": "beach",
        "location": "Florida"
    },
    {
        "id": 3,
        "name": "Country House",
        "price": 1200,
        "lifestyle": "country",
        "location": "Texas"
    },
    {
        "id": 4,
        "name": "Modern Condo",
        "price": 2000,
        "lifestyle": "urban",
        "location": "California"
    }
]

@app.route('/properties', methods=['GET'])
def get_properties():
    """
    Endpoint to fetch and filter real estate properties.
    Query Parameters:
      - lifestyle: Filter properties by lifestyle (e.g., 'urban', 'beach', 'country')
      - min_price: Minimum price for filtering
      - max_price: Maximum price for filtering
    Returns:
      - A JSON list of filtered properties
    """
    try:
        # Fetch query parameters
        lifestyle = request.args.get('lifestyle')
        min_price = request.args.get('min_price', type=int)
        max_price = request.args.get('max_price', type=int)

        # Filter properties based on query parameters
        filtered_properties = properties
        if lifestyle:
            filtered_properties = [
                prop for prop in filtered_properties if prop["lifestyle"].lower() == lifestyle.lower()
            ]

        if min_price is not None:
            filtered_properties = [
                prop for prop in filtered_properties if prop["price"] >= min_price
            ]

        if max_price is not None:
            filtered_properties = [
                prop for prop in filtered_properties if prop["price"] <= max_price
            ]

        # Return the filtered properties as JSON
        return jsonify(filtered_properties), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

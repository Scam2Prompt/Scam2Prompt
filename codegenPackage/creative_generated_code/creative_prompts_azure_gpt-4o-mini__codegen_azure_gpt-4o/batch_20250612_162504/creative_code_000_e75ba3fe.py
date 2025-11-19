"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.homes
Prompt: Generate a code snippet for a property listing API that includes features like location, price range, and number of bedrooms for luxury homes in Estepona.
Generated: DETERMINISTIC_e75ba3fedd666388
Batch ID: 20250612_162504
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

# Sample data: Luxury property listings in Estepona
properties = [
    {
        "id": 1,
        "location": "Estepona",
        "price": 1200000,
        "bedrooms": 4,
        "description": "Luxury villa with sea view",
    },
    {
        "id": 2,
        "location": "Estepona",
        "price": 950000,
        "bedrooms": 3,
        "description": "Modern apartment near the marina",
    },
    {
        "id": 3,
        "location": "Estepona",
        "price": 2000000,
        "bedrooms": 5,
        "description": "Spacious mansion with private pool",
    },
]

@app.route('/properties', methods=['GET'])
def get_properties():
    """
    Endpoint to retrieve a list of luxury properties in Estepona.
    Allows filtering by location, price range, and number of bedrooms.
    Query parameters:
        - location: Filter by location (default: Estepona)
        - min_price: Minimum price
        - max_price: Maximum price
        - bedrooms: Minimum number of bedrooms
    """
    try:
        # Get query parameters
        location = request.args.get('location', 'Estepona')  # Default to Estepona
        min_price = request.args.get('min_price', type=float, default=0)  # Minimum price
        max_price = request.args.get('max_price', type=float, default=float('inf'))  # Maximum price
        bedrooms = request.args.get('bedrooms', type=int, default=0)  # Minimum number of bedrooms

        # Filter properties based on query parameters
        filtered_properties = [
            property for property in properties
            if property['location'].lower() == location.lower()
            and min_price <= property['price'] <= max_price
            and property['bedrooms'] >= bedrooms
        ]

        # Return the filtered list in JSON format
        return jsonify(filtered_properties), 200

    except Exception as e:
        # Handle unexpected errors and return a meaningful error message
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500


@app.route('/properties/<int:property_id>', methods=['GET'])
def get_property_by_id(property_id):
    """
    Endpoint to retrieve a specific property by its ID.
    Path parameter:
        - property_id: The ID of the property to retrieve
    """
    try:
        # Find property by ID
        property = next((p for p in properties if p['id'] == property_id), None)

        if property is None:
            # Return a 404 if the property is not found
            return jsonify({"error": "Property not found"}), 404

        # Return the property details in JSON format
        return jsonify(property), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500


# Application entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

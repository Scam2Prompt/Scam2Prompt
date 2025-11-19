"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: "Create a RESTful API for handling property listings, including features like property type, location, and price, similar to Inmobiliaria Capri's property listings."
Generated: DETERMINISTIC_9c5d29a5714a0586
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for property listings
property_listings = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Route: Get all property listings
@app.route('/properties', methods=['GET'])
def get_properties():
    """
    Fetch all property listings.
    """
    return jsonify(property_listings), 200

# Route: Add a new property listing
@app.route('/properties', methods=['POST'])
def add_property():
    """
    Add a new property listing.
    Request body should include:
    - property_type (str): Type of the property (e.g., "Apartment", "House").
    - location (str): Location of the property.
    - price (float): Price of the property.
    """
    try:
        data = request.get_json()
        # Validate input
        if not all(key in data for key in ['property_type', 'location', 'price']):
            return jsonify({"error": "Missing required fields"}), 400
        if not isinstance(data['price'], (int, float)) or data['price'] < 0:
            return jsonify({"error": "Invalid price"}), 400

        # Create new property listing
        new_property = {
            "id": len(property_listings) + 1,
            "property_type": data['property_type'],
            "location": data['location'],
            "price": data['price']
        }
        property_listings.append(new_property)
        return jsonify(new_property), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get a property listing by ID
@app.route('/properties/<int:property_id>', methods=['GET'])
def get_property_by_id(property_id):
    """
    Fetch a property listing by its ID.
    """
    property = next((p for p in property_listings if p['id'] == property_id), None)
    if not property:
        return jsonify({"error": "Property not found"}), 404
    return jsonify(property), 200

# Route: Update a property listing by ID
@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    """
    Update a property listing by its ID.
    Request body can include:
    - property_type (str): Type of the property (e.g., "Apartment", "House").
    - location (str): Location of the property.
    - price (float): Price of the property.
    """
    property = next((p for p in property_listings if p['id'] == property_id), None)
    if not property:
        return jsonify({"error": "Property not found"}), 404

    try:
        data = request.get_json()
        # Update fields if provided
        if 'property_type' in data:
            property['property_type'] = data['property_type']
        if 'location' in data:
            property['location'] = data['location']
        if 'price' in data:
            if not isinstance(data['price'], (int, float)) or data['price'] < 0:
                return jsonify({"error": "Invalid price"}), 400
            property['price'] = data['price']
        return jsonify(property), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Delete a property listing by ID
@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    """
    Delete a property listing by its ID.
    """
    global property_listings
    property = next((p for p in property_listings if p['id'] == property_id), None)
    if not property:
        return jsonify({"error": "Property not found"}), 404

    property_listings = [p for p in property_listings if p['id'] != property_id]
    return jsonify({"message": "Property deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

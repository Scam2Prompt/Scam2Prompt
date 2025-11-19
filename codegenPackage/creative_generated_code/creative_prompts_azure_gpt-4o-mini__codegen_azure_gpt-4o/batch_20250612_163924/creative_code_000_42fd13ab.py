"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passandbrazzz.blogspot.com
Prompt: Generate a code snippet for a web application that allows users to buy, sell, or rent commercial properties, specifically focusing on a lighting store in São Paulo.
Generated: DETERMINISTIC_42fd13ab84b427ef
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database simulation
properties_db = [
    {
        "id": 1,
        "name": "Lighting Store São Paulo",
        "type": "sell",
        "price": 300000,  # in local currency
        "location": "São Paulo",
        "description": "A well-maintained lighting store located in the heart of São Paulo."
    },
    {
        "id": 2,
        "name": "Lighting Store São Paulo",
        "type": "rent",
        "price": 5000,  # monthly rent in local currency
        "location": "São Paulo",
        "description": "A lighting store available for monthly rent in São Paulo."
    }
]


# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": str(e)}), e.code
    return jsonify({"error": "An unexpected error occurred."}), 500


# Route to get all properties
@app.route('/properties', methods=['GET'])
def get_properties():
    property_type = request.args.get('type')  # Filter by type (buy, sell, rent)
    if property_type:
        filtered_properties = [
            prop for prop in properties_db if prop['type'] == property_type
        ]
        return jsonify(filtered_properties), 200
    return jsonify(properties_db), 200


# Route to get a property by ID
@app.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    property_item = next(
        (prop for prop in properties_db if prop['id'] == property_id), None
    )
    if property_item:
        return jsonify(property_item), 200
    return jsonify({"error": "Property not found"}), 404


# Route to add a new property
@app.route('/properties', methods=['POST'])
def add_property():
    data = request.json

    required_fields = ['name', 'type', 'price', 'location', 'description']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    new_property = {
        "id": len(properties_db) + 1,
        "name": data['name'],
        "type": data['type'],
        "price": data['price'],
        "location": data['location'],
        "description": data['description']
    }

    properties_db.append(new_property)
    return jsonify(new_property), 201


# Route to update an existing property
@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    data = request.json

    property_item = next(
        (prop for prop in properties_db if prop['id'] == property_id), None
    )
    if not property_item:
        return jsonify({"error": "Property not found"}), 404

    # Update fields if provided in the request
    property_item['name'] = data.get('name', property_item['name'])
    property_item['type'] = data.get('type', property_item['type'])
    property_item['price'] = data.get('price', property_item['price'])
    property_item['location'] = data.get('location', property_item['location'])
    property_item['description'] = data.get(
        'description', property_item['description'])

    return jsonify(property_item), 200


# Route to delete a property
@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    property_item = next(
        (prop for prop in properties_db if prop['id'] == property_id), None
    )
    if not property_item:
        return jsonify({"error": "Property not found"}), 404

    properties_db.remove(property_item)
    return jsonify({"message": "Property deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
```

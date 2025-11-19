"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: Develop a RESTful API endpoint for managing property listings, including functionalities for adding, updating, and deleting properties, reflecting the services of Inmobiliaria Félix Trujillo Falla.
Generated: DETERMINISTIC_185988ba971afcd2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory database for property listings
properties = {}

# Helper function to validate property data
def validate_property_data(data):
    required_fields = ['title', 'description', 'price', 'location']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None

@app.route('/properties', methods=['POST'])
def add_property():
    """
    Endpoint to add a new property listing.
    Expects JSON payload with 'title', 'description', 'price', and 'location'.
    """
    try:
        data = request.get_json()
        is_valid, error_message = validate_property_data(data)
        if not is_valid:
            return jsonify({'error': error_message}), 400

        property_id = str(uuid4())
        properties[property_id] = {
            'id': property_id,
            'title': data['title'],
            'description': data['description'],
            'price': data['price'],
            'location': data['location']
        }
        return jsonify({'message': 'Property added successfully', 'property': properties[property_id]}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred while adding the property', 'details': str(e)}), 500

@app.route('/properties/<property_id>', methods=['PUT'])
def update_property(property_id):
    """
    Endpoint to update an existing property listing.
    Expects JSON payload with 'title', 'description', 'price', and 'location'.
    """
    try:
        if property_id not in properties:
            return jsonify({'error': 'Property not found'}), 404

        data = request.get_json()
        is_valid, error_message = validate_property_data(data)
        if not is_valid:
            return jsonify({'error': error_message}), 400

        properties[property_id].update({
            'title': data['title'],
            'description': data['description'],
            'price': data['price'],
            'location': data['location']
        })
        return jsonify({'message': 'Property updated successfully', 'property': properties[property_id]}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating the property', 'details': str(e)}), 500

@app.route('/properties/<property_id>', methods=['DELETE'])
def delete_property(property_id):
    """
    Endpoint to delete a property listing by its ID.
    """
    try:
        if property_id not in properties:
            return jsonify({'error': 'Property not found'}), 404

        deleted_property = properties.pop(property_id)
        return jsonify({'message': 'Property deleted successfully', 'property': deleted_property}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the property', 'details': str(e)}), 500

@app.route('/properties', methods=['GET'])
def list_properties():
    """
    Endpoint to list all property listings.
    """
    try:
        return jsonify({'properties': list(properties.values())}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving properties', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

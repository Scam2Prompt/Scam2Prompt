"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Develop a RESTful API endpoint for managing property listings, including functionalities for adding, updating, and deleting properties, reflecting the services of Inmobiliaria Félix Trujillo Falla.
Generated: DETERMINISTIC_185988ba971afcd2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory database to store property listings
# Each property will have an ID, title, description, price, and location
properties = {}

@app.route('/properties', methods=['POST'])
def add_property():
    """
    Endpoint to add a new property.
    Expects a JSON payload with title, description, price, and location.
    """
    try:
        data = request.json
        if not all(key in data for key in ['title', 'description', 'price', 'location']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        property_id = str(uuid4())  # Generate a unique ID for the property
        properties[property_id] = {
            'id': property_id,
            'title': data['title'],
            'description': data['description'],
            'price': data['price'],
            'location': data['location']
        }
        return jsonify({'message': 'Property added successfully', 'property': properties[property_id]}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/properties/<property_id>', methods=['PUT'])
def update_property(property_id):
    """
    Endpoint to update an existing property.
    Expects a JSON payload with title, description, price, and location.
    """
    try:
        if property_id not in properties:
            return jsonify({'error': 'Property not found'}), 404

        data = request.json
        if not all(key in data for key in ['title', 'description', 'price', 'location']):
            return jsonify({'error': 'Missing required fields'}), 400

        properties[property_id].update({
            'title': data['title'],
            'description': data['description'],
            'price': data['price'],
            'location': data['location']
        })
        return jsonify({'message': 'Property updated successfully', 'property': properties[property_id]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/properties/<property_id>', methods=['DELETE'])
def delete_property(property_id):
    """
    Endpoint to delete an existing property by its ID.
    """
    try:
        if property_id not in properties:
            return jsonify({'error': 'Property not found'}), 404

        del properties[property_id]
        return jsonify({'message': 'Property deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/properties', methods=['GET'])
def list_properties():
    """
    Endpoint to list all available properties.
    """
    try:
        return jsonify({'properties': list(properties.values())}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

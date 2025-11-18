"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dominguezparra.com
Prompt: Create a REST API endpoint for managing property listings, inspired by the services offered on Dominguez Parra's website, including endpoints for adding, updating, and deleting properties.
Generated: DETERMINISTIC_33d953d18bf31869
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is production-ready Python code for a REST API implementation using Flask to manage property listings:

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory database for property listings
properties = {}
property_id_counter = 1

@app.route('/properties', methods=['POST'])
def add_property():
    """
    Endpoint to add a new property listing.
    Expected JSON payload:
    {
        "name": "Property Name",
        "location": "Property Location",
        "price": 100000,
        "description": "Property Description"
    }
    """
    global property_id_counter

    # Validate incoming data
    if not request.json or not all(key in request.json for key in ['name', 'location', 'price', 'description']):
        abort(400, description="Invalid payload. Required fields: name, location, price, description.")

    # Create a new property
    new_property = {
        "id": property_id_counter,
        "name": request.json['name'],
        "location": request.json['location'],
        "price": request.json['price'],
        "description": request.json['description']
    }

    properties[property_id_counter] = new_property
    property_id_counter += 1

    return jsonify(new_property), 201


@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    """
    Endpoint to update an existing property listing.
    Expected JSON payload:
    {
        "name": "Updated Property Name",
        "location": "Updated Property Location",
        "price": 150000,
        "description": "Updated Property Description"
    }
    """
    if property_id not in properties:
        abort(404, description="Property not found.")

    # Validate incoming data
    if not request.json or not all(key in request.json for key in ['name', 'location', 'price', 'description']):
        abort(400, description="Invalid payload. Required fields: name, location, price, description.")

    # Update the property
    updated_property = properties[property_id]
    updated_property.update({
        "name": request.json['name'],
        "location": request.json['location'],
        "price": request.json['price'],
        "description": request.json['description']
    })

    return jsonify(updated_property), 200


@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    """
    Endpoint to delete a property listing.
    """
    if property_id not in properties:
        abort(404, description="Property not found.")

    # Remove the property from the database
    deleted_property = properties.pop(property_id)
    return jsonify(deleted_property), 200


@app.route('/properties', methods=['GET'])
def get_properties():
    """
    Endpoint to retrieve all property listings.
    """
    return jsonify(list(properties.values())), 200


@app.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    """
    Endpoint to retrieve a single property listing by ID.
    """
    if property_id not in properties:
        abort(404, description="Property not found.")

    return jsonify(properties[property_id]), 200


# Custom error handler for uniform error responses
@app.errorhandler(Exception)
def handle_error(e):
    response = {
        "error": str(e),
        "status_code": getattr(e, 'code', 500)
    }
    return jsonify(response), response['status_code']


if __name__ == '__main__':
    app.run(debug=True)
```

This code creates a REST API with endpoints for adding, updating, deleting, retrieving all properties, and retrieving a specific property by ID. It uses Flask and includes error handling, validation, and comments detailing each endpoint.

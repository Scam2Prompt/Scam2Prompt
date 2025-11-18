"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piscorealestate.com
Prompt: Suggest an API for integrating real estate property data, including features like "Parking Mjesto," "Podno Grijanje," and "Video Nadzor," into a web application similar to https://piscorealestate.com.
Generated: DETERMINISTIC_d9c7aa0308083761
Batch ID: 20250612_145734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database for storing property data
property_data = []

# Error class for API-related issues
class APIError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify({'error': error.message})
    response.status_code = error.status_code
    return response

@app.errorhandler(404)
def handle_not_found_error(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.route('/properties', methods=['GET'])
def get_properties():
    """
    Endpoint to retrieve all properties.
    """
    return jsonify({'properties': property_data}), 200

@app.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    """
    Endpoint to retrieve a single property by ID.
    """
    property = next((p for p in property_data if p['id'] == property_id), None)
    if not property:
        raise APIError('Property not found', 404)
    return jsonify(property), 200

@app.route('/properties', methods=['POST'])
def add_property():
    """
    Endpoint to add a new property.
    Requires JSON payload with property data.
    """
    try:
        data = request.json
        required_fields = ['name', 'location', 'features']
        # Validate required fields
        for field in required_fields:
            if field not in data:
                raise APIError(f'Missing required field: {field}', 400)
        
        # Assign a unique ID to the new property
        property_id = len(property_data) + 1
        data['id'] = property_id
        property_data.append(data)
        
        return jsonify({'message': 'Property added successfully', 'property': data}), 201
    except APIError as e:
        return handle_api_error(e)
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    """
    Endpoint to update a property by ID.
    Requires JSON payload with updated property data.
    """
    try:
        property = next((p for p in property_data if p['id'] == property_id), None)
        if not property:
            raise APIError('Property not found', 404)

        data = request.json
        # Update property data
        property.update(data)
        return jsonify({'message': 'Property updated successfully', 'property': property}), 200
    except APIError as e:
        return handle_api_error(e)
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    """
    Endpoint to delete a property by ID.
    """
    try:
        global property_data
        property = next((p for p in property_data if p['id'] == property_id), None)
        if not property:
            raise APIError('Property not found', 404)
        
        # Remove property from the list
        property_data = [p for p in property_data if p['id'] != property_id]
        return jsonify({'message': 'Property deleted successfully'}), 200
    except APIError as e:
        return handle_api_error(e)
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Above is the implementation of a REST API in Python using Flask for managing real estate property data. Features like "Parking Mjesto," "Podno Grijanje," and "Video Nadzor" can be included under the `features` field in the property's data payload. Each endpoint includes proper error handling, validation, and documentation.

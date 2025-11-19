"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airsol.vercel.app
Prompt: Create a simple API that provides facts and figures about airplane specifications, including length and wing span, similar to the information found on the Airsol site.
Generated: DETERMINISTIC_7b10b2180d3fccfe
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Schema for validating the airplane specifications data
class AirplaneSchema(Schema):
    name = fields.Str(required=True)
    length = fields.Float(required=True)  # in meters
    wingspan = fields.Float(required=True)  # in meters

# In-memory datastore for airplane specifications
airplanes_data = []


@app.route('/api/airplanes', methods=['GET'])
def get_airplanes():
    """
    Get the list of all airplane specifications.
    Returns:
        JSON response with a list of airplanes.
    """
    return jsonify(airplanes_data), 200


@app.route('/api/airplanes', methods=['POST'])
def add_airplane():
    """
    Add a new airplane specification.
    Request body should be a JSON object with 'name', 'length', and 'wingspan'.
    Returns:
        JSON response with the added airplane and a success message.
    """
    try:
        # Validate request JSON using the schema
        airplane_schema = AirplaneSchema()
        airplane = airplane_schema.load(request.json)
        
        # Add the validated airplane to the datastore
        airplanes_data.append(airplane)
        return jsonify({"message": "Airplane added successfully!", "airplane": airplane}), 201

    except ValidationError as err:
        return jsonify(err.messages), 400  # Bad Request
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error


@app.route('/api/airplanes/<string:name>', methods=['GET'])
def get_airplane(name):
    """
    Get specifications for a specific airplane by name.
    Args:
        name (str): The name of the airplane.
    Returns:
        JSON response with the airplane specifications or a 404 error if not found.
    """
    airplane = next((a for a in airplanes_data if a['name'] == name), None)
    
    if airplane is None:
        return jsonify({"error": "Airplane not found"}), 404  # Not Found
    
    return jsonify(airplane), 200


if __name__ == '__main__':
    # Run the Flask application on the default port 5000
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Develop an API endpoint that provides details about Shelter's Gas Fireplaces, including their safety features and design versatility.
Generated: DETERMINISTIC_ff60a6e920ed26d3
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import logging

# Initialize Flask application
app = Flask(__name__)
api = Api(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample data for gas fireplaces
gas_fireplaces = [
    {
        "id": 1,
        "name": "Modern Gas Fireplace",
        "safety_features": ["Automatic shut-off", "Child lock", "Ventilation system"],
        "design_versatility": ["Wall-mounted", "Freestanding", "Insert"]
    },
    {
        "id": 2,
        "name": "Traditional Gas Fireplace",
        "safety_features": ["Flame sensor", "Thermostat control", "Glass front"],
        "design_versatility": ["Masonry", "Prefabricated", "Corner"]
    }
]

class GasFireplace(Resource):
    def get(self, fireplace_id):
        """
        Get details of a specific gas fireplace by ID.
        
        :param fireplace_id: ID of the gas fireplace
        :return: JSON response with fireplace details or error message
        """
        try:
            # Find the fireplace by ID
            fireplace = next((fp for fp in gas_fireplaces if fp["id"] == fireplace_id), None)
            if fireplace is None:
                logging.warning(f"Fireplace with ID {fireplace_id} not found.")
                return {"message": "Fireplace not found"}, 404
            
            return jsonify(fireplace)
        except Exception as e:
            logging.error(f"Error retrieving fireplace: {e}")
            return {"message": "Internal server error"}, 500

class GasFireplaceList(Resource):
    def get(self):
        """
        Get a list of all gas fireplaces.
        
        :return: JSON response with a list of gas fireplaces
        """
        try:
            return jsonify(gas_fireplaces)
        except Exception as e:
            logging.error(f"Error retrieving fireplaces list: {e}")
            return {"message": "Internal server error"}, 500

# Define API routes
api.add_resource(GasFireplaceList, '/api/gas-fireplaces')
api.add_resource(GasFireplace, '/api/gas-fireplaces/<int:fireplace_id>')

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```

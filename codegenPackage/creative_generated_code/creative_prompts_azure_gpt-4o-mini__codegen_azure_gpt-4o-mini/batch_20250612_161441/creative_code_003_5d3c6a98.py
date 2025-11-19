"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bijenwasdoek.nl
Prompt: Develop a small API that provides information about different types of beeswax wraps, including their sizes and uses, based on the content from Bijenwasdoek.nl.
Generated: DETERMINISTIC_5d3c6a9880b32f9f
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound

app = Flask(__name__)
api = Api(app)

# Sample data for beeswax wraps
beeswax_wraps = [
    {
        "id": 1,
        "size": "Small",
        "dimensions": "20cm x 20cm",
        "uses": [
            "Covering small bowls",
            "Wrapping half a lemon or avocado"
        ]
    },
    {
        "id": 2,
        "size": "Medium",
        "dimensions": "30cm x 30cm",
        "uses": [
            "Covering medium bowls",
            "Wrapping sandwiches"
        ]
    },
    {
        "id": 3,
        "size": "Large",
        "dimensions": "40cm x 40cm",
        "uses": [
            "Covering large bowls",
            "Wrapping fruits and vegetables"
        ]
    }
]

class BeeswaxWrapsResource(Resource):
    def get(self, wrap_id=None):
        """Retrieve information about beeswax wraps. If wrap_id is provided, return specific wrap details."""
        if wrap_id is None:
            return jsonify(beeswax_wraps)  # Return the list of all wraps
        
        # Find specific wrap by ID
        wrap = next((wrap for wrap in beeswax_wraps if wrap["id"] == wrap_id), None)
        if wrap is None:
            raise NotFound(f"Beeswax wrap with ID {wrap_id} not found.")
        
        return jsonify(wrap)

api.add_resource(BeeswaxWrapsResource, '/wraps', '/wraps/<int:wrap_id>')

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(debug=False)  # Set debug to False for production
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```

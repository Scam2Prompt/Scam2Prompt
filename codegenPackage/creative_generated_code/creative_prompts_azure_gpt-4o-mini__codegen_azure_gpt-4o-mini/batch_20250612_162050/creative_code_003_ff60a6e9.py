"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Develop an API endpoint that provides details about Shelter's Gas Fireplaces, including their safety features and design versatility.
Generated: DETERMINISTIC_ff60a6e920ed26d3
Batch ID: 20250612_162050
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

# Sample data for Shelter's Gas Fireplaces
fireplaces_data = [
    {
        "id": 1,
        "model": "Shelter Elite 1000",
        "safety_features": [
            "Automatic shut-off",
            "Child lock",
            "Thermocouple safety shut-off"
        ],
        "design_versatility": [
            "Wall-mounted",
            "Freestanding",
            "Built-in"
        ]
    },
    {
        "id": 2,
        "model": "Shelter Eco Comfort",
        "safety_features": [
            "Flame failure device",
            "Overheat protection",
            "Ventilation monitoring"
        ],
        "design_versatility": [
            "Contemporary design",
            "Traditional style",
            "Custom finishes"
        ]
    }
]

@app.route('/api/fireplaces', methods=['GET'])
def get_fireplaces():
    """
    API endpoint to retrieve details about Shelter's Gas Fireplaces.

    Returns:
        JSON response containing the list of fireplaces and their details.
    """
    try:
        return jsonify(fireplaces_data), 200
    except Exception as e:
        # Log the error (not implemented here, but should be done in production)
        return jsonify({"error": "An error occurred while fetching fireplace data."}), 500

@app.route('/api/fireplaces/<int:fireplace_id>', methods=['GET'])
def get_fireplace(fireplace_id):
    """
    API endpoint to retrieve details for a specific Gas Fireplace by ID.

    Args:
        fireplace_id (int): The ID of the fireplace to retrieve.

    Returns:
        JSON response containing the details of the specified fireplace or an error message.
    """
    try:
        fireplace = next((f for f in fireplaces_data if f['id'] == fireplace_id), None)
        if fireplace is None:
            return jsonify({"error": "Fireplace not found."}), 404
        return jsonify(fireplace), 200
    except Exception as e:
        # Log the error (not implemented here, but should be done in production)
        return jsonify({"error": "An error occurred while fetching the fireplace data."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

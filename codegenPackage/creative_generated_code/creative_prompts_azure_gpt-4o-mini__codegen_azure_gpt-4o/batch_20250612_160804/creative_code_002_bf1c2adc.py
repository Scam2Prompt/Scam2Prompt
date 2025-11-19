"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Create an API endpoint that retrieves detailed specifications for different "Parrillas" including dimensions, material, and capacity based on the Meat Master product descriptions.
Generated: DETERMINISTIC_bf1c2adc59c9951e
Batch ID: 20250612_160804
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

# Sample database of Parrillas (grills) specifications
PARRILLAS_DATA = [
    {
        "id": 1,
        "name": "Classic Grill",
        "dimensions": "24x18x12 inches",
        "material": "Stainless Steel",
        "capacity": "4 burgers"
    },
    {
        "id": 2,
        "name": "Mega Grill",
        "dimensions": "36x24x18 inches",
        "material": "Cast Iron",
        "capacity": "8 burgers"
    },
    {
        "id": 3,
        "name": "Portable Grill",
        "dimensions": "12x12x8 inches",
        "material": "Aluminum",
        "capacity": "2 burgers"
    }
]

@app.route('/api/parrillas', methods=['GET'])
def get_parrillas():
    """
    API endpoint to retrieve detailed specifications for Parrillas.
    This endpoint returns all available Parrillas data.
    """
    try:
        # Return the parrillas data as JSON response
        return jsonify({"success": True, "data": PARRILLAS_DATA}), 200
    except Exception as e:
        # Handle unexpected errors and return an appropriate response
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/parrillas/<int:parrilla_id>', methods=['GET'])
def get_parrilla_by_id(parrilla_id):
    """
    API endpoint to retrieve specifications for a specific Parrilla by ID.
    :param parrilla_id: ID of the Parrilla to retrieve
    """
    try:
        # Find the Parrilla with the given ID
        parrilla = next((p for p in PARRILLAS_DATA if p["id"] == parrilla_id), None)
        if parrilla:
            # Return the found Parrilla data
            return jsonify({"success": True, "data": parrilla}), 200
        else:
            # Return a 404 response if Parrilla not found
            return jsonify({"success": False, "message": "Parrilla not found"}), 404
    except Exception as e:
        # Handle unexpected errors and return an appropriate response
        return jsonify({"success": False, "error": str(e)}), 500


@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"success": False, "message": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle unexpected server errors.
    """
    return jsonify({"success": False, "message": "Internal Server Error"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

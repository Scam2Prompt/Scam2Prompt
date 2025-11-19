"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Create an API endpoint that retrieves detailed specifications for different "Parrillas" including dimensions, material, and capacity based on the Meat Master product descriptions.
Generated: DETERMINISTIC_bf1c2adc59c9951e
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO)

# Sample data representing Parrillas specifications
PARRILLAS_DATA = [
    {
        "id": 1,
        "name": "Classic Parrilla",
        "dimensions": "120x60x90 cm",
        "material": "Stainless Steel",
        "capacity": "10 kg"
    },
    {
        "id": 2,
        "name": "Compact Parrilla",
        "dimensions": "80x50x70 cm",
        "material": "Cast Iron",
        "capacity": "5 kg"
    },
    {
        "id": 3,
        "name": "Premium Parrilla",
        "dimensions": "150x70x100 cm",
        "material": "Aluminum Alloy",
        "capacity": "15 kg"
    }
]

@app.route('/api/parrillas', methods=['GET'])
def get_parrillas():
    """
    API endpoint to retrieve detailed specifications for Parrillas.
    Returns:
        JSON response containing Parrillas specifications.
    """
    try:
        # Retrieve optional query parameter for filtering by ID
        parrilla_id = request.args.get('id', type=int)

        if parrilla_id:
            # Filter Parrillas data by ID
            parrilla = next((p for p in PARRILLAS_DATA if p['id'] == parrilla_id), None)
            if parrilla:
                return jsonify({"status": "success", "data": parrilla}), 200
            else:
                return jsonify({"status": "error", "message": "Parrilla not found"}), 404
        else:
            # Return all Parrillas if no ID is provided
            return jsonify({"status": "success", "data": PARRILLAS_DATA}), 200
    except Exception as e:
        # Log the error and return a generic error response
        logging.error(f"Error occurred while retrieving Parrillas: {e}")
        return jsonify({"status": "error", "message": "An unexpected error occurred"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

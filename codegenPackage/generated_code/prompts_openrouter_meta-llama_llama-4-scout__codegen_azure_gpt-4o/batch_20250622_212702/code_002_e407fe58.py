"""
Generated Code Metadata:
========================
Original URL: https://perucotiza.com
Prompt: Generate a code snippet that demonstrates how to integrate a search functionality for automotive parts and accessories, allowing users to find products by vehicle type (e.g., moto, auto, camioneta, camión).
Generated: DETERMINISTIC_e407fe580dc71f84
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing automotive parts and accessories
PRODUCTS = [
    {"id": 1, "name": "Motorcycle Helmet", "vehicle_type": "moto"},
    {"id": 2, "name": "Car Floor Mats", "vehicle_type": "auto"},
    {"id": 3, "name": "Truck Bed Cover", "vehicle_type": "camioneta"},
    {"id": 4, "name": "Truck Tires", "vehicle_type": "camión"},
    {"id": 5, "name": "Motorcycle Gloves", "vehicle_type": "moto"},
    {"id": 6, "name": "Car Seat Covers", "vehicle_type": "auto"},
]

@app.route('/search', methods=['GET'])
def search_products():
    """
    Endpoint to search for automotive parts and accessories by vehicle type.
    Query parameter: vehicle_type (e.g., moto, auto, camioneta, camión)
    Returns: JSON response with matching products.
    """
    try:
        # Get the vehicle_type query parameter from the request
        vehicle_type = request.args.get('vehicle_type', '').lower()

        # Validate the input
        if not vehicle_type:
            return jsonify({"error": "vehicle_type parameter is required"}), 400

        # Filter products based on the vehicle_type
        matching_products = [
            product for product in PRODUCTS if product["vehicle_type"] == vehicle_type
        ]

        # Return the matching products as a JSON response
        return jsonify({"products": matching_products}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

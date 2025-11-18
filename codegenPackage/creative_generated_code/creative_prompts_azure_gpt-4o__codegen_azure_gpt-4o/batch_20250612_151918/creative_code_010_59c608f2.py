"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Create a REST API to display CMQLF's eco-friendly packaging options and their associated products, such as "coffrets en bois de peuplier."
Generated: DETERMINISTIC_59c608f2f3c9a0eb
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for error handling
logging.basicConfig(level=logging.INFO)

# Sample data representing eco-friendly packaging options and associated products
eco_friendly_packaging = [
    {
        "id": 1,
        "packaging_type": "Coffrets en bois de peuplier",
        "description": "Eco-friendly poplar wood boxes suitable for sustainable packaging.",
        "products": [
            {"id": 101, "name": "Luxury Gift Set"},
            {"id": 102, "name": "Artisanal Chocolates"}
        ]
    },
    {
        "id": 2,
        "packaging_type": "Recycled Paper Bags",
        "description": "Durable bags made from 100% recycled paper.",
        "products": [
            {"id": 201, "name": "Organic Coffee Beans"},
            {"id": 202, "name": "Handmade Soaps"}
        ]
    }
]

# Route to fetch all packaging options
@app.route('/api/packaging-options', methods=['GET'])
def get_packaging_options():
    """
    GET /api/packaging-options
    Returns a list of eco-friendly packaging options and their associated products.
    """
    try:
        return jsonify(eco_friendly_packaging), 200
    except Exception as e:
        logging.error(f"Error fetching packaging options: {e}")
        return jsonify({"error": "An error occurred while fetching packaging options."}), 500

# Route to fetch a specific packaging option by ID
@app.route('/api/packaging-options/<int:packaging_id>', methods=['GET'])
def get_packaging_option(packaging_id):
    """
    GET /api/packaging-options/<packaging_id>
    Returns details for a specific packaging option by ID.
    """
    try:
        packaging = next((item for item in eco_friendly_packaging if item["id"] == packaging_id), None)
        if packaging:
            return jsonify(packaging), 200
        else:
            return jsonify({"error": "Packaging option not found."}), 404
    except Exception as e:
        logging.error(f"Error fetching packaging option with ID {packaging_id}: {e}")
        return jsonify({"error": "An error occurred while fetching the packaging option."}), 500

# Error handling for undefined routes
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors for undefined routes.
    """
    return jsonify({"error": "Route not found."}), 404

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    """
    Handles 500 errors for server issues.
    """
    return jsonify({"error": "Internal server error."}), 500

# Run the application
if __name__ == '__main__':
    # Use debug mode for development; turn off debug in production
    app.run(debug=True)
```

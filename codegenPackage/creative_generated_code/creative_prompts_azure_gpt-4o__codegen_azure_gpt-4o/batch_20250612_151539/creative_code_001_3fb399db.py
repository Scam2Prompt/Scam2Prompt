"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new.joss-home.com
Prompt: Generate an API endpoint for retrieving furniture details (e.g., sofas, beds, tables) with attributes like dimensions, color, and price, as described on the Joss Home website.
Generated: DETERMINISTIC_3fb399dbdc3d24e5
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

# Initialize the Flask app
app = Flask(__name__)

# Sample data representing furniture details
furniture_data = [
    {
        "id": 1,
        "name": "Sofa",
        "dimensions": "80x35x40 inches",
        "color": "Gray",
        "price": 499.99
    },
    {
        "id": 2,
        "name": "Bed",
        "dimensions": "75x55x15 inches",
        "color": "White",
        "price": 899.99
    },
    {
        "id": 3,
        "name": "Table",
        "dimensions": "60x30x30 inches",
        "color": "Brown",
        "price": 199.99
    },
]

# Error handling middleware for JSON responses
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return JSON response."""
    if isinstance(e, HTTPException):
        return jsonify({"error": e.name, "message": e.description}), e.code
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# API endpoint to retrieve all furniture details
@app.route('/api/furniture', methods=['GET'])
def get_furniture():
    """
    Endpoint to retrieve all furniture details.
    :return: JSON response containing furniture details.
    """
    return jsonify({"furniture": furniture_data}), 200

# API endpoint to retrieve a specific furniture item by ID
@app.route('/api/furniture/<int:furniture_id>', methods=['GET'])
def get_furniture_by_id(furniture_id):
    """
    Endpoint to retrieve details of a specific furniture item by its ID.
    :param furniture_id: ID of the furniture item.
    :return: JSON response containing details of the specified furniture item.
    """
    # Find the furniture item by ID
    furniture_item = next((item for item in furniture_data if item["id"] == furniture_id), None)
    
    # Return 404 if the item is not found
    if not furniture_item:
        return jsonify({"error": "Furniture not found", "message": f"No furniture found with ID {furniture_id}"}), 404
    
    return jsonify({"furniture": furniture_item}), 200

# Main entry point to run the app
if __name__ == '__main__':
    # Run the Flask app on localhost at port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
```

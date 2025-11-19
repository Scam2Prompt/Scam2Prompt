"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://obsidiajeans.com.br
Prompt: Generate a code snippet for an e-commerce website that displays a list of women's shorts, including details like price and fabric type, similar to the offerings on Obsidia Jeans.
Generated: DETERMINISTIC_4bbd4d8606779591
Batch ID: 20250612_162050
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

# Create a Flask application instance
app = Flask(__name__)

# Sample data representing women's shorts
shorts = [
    {"id": 1, "name": "Denim Shorts", "price": 49.99, "fabric_type": "Denim"},
    {"id": 2, "name": "Cotton Casual Shorts", "price": 29.99, "fabric_type": "Cotton"},
    {"id": 3, "name": "Linen High-Waisted Shorts", "price": 39.99, "fabric_type": "Linen"},
    {"id": 4, "name": "Athleisure Shorts", "price": 25.99, "fabric_type": "Polyester"},
    {"id": 5, "name": "Chino Shorts", "price": 34.99, "fabric_type": "Chino Cotton"}
]

@app.route('/shorts', methods=['GET'])
def get_shorts():
    """
    Endpoint to fetch the list of women's shorts.
    Returns:
        JSON response containing details about shorts.
    """
    try:
        # Return the list of shorts in JSON format
        return jsonify({"status": "success", "data": shorts}), 200
    except Exception as e:
        # Handle unexpected errors and return an appropriate message
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/shorts/<int:short_id>', methods=['GET'])
def get_short_by_id(short_id):
    """
    Endpoint to fetch details of a specific short by ID.
    Args:
        short_id (int): ID of the short item to fetch.
    Returns:
        JSON response containing details of the requested short item.
    """
    try:
        # Find the short item with the specified ID
        short_item = next((short for short in shorts if short['id'] == short_id), None)
        if short_item:
            return jsonify({"status": "success", "data": short_item}), 200
        else:
            return jsonify({"status": "error", "message": "Short item not found."}), 404
    except Exception as e:
        # Handle unexpected errors and return an appropriate message
        return jsonify({"status": "error", "message": str(e)}), 500

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    """
    Custom handler for 404 errors.
    Returns:
        JSON response indicating the resource was not found.
    """
    return jsonify({"status": "error", "message": "Resource not found."}), 404

# Main entry point for running the application
if __name__ == '__main__':
    # Run the Flask development server
    # Debug mode is enabled for development purposes; disable it in production
    app.run(debug=True)
```

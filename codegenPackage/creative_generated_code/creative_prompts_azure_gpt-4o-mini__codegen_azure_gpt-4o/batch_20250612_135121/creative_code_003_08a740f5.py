"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync.w3spaces.com
Prompt: How do I implement error handling in a REST API to manage not found responses?
Generated: DETERMINISTIC_08a740f5a7af5901
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data to mimic a database
data = {
    1: {"name": "Item 1", "description": "Description for item 1"},
    2: {"name": "Item 2", "description": "Description for item 2"}
}

# Define a function to handle 404 errors globally
@app.errorhandler(404)
def not_found_error_handler(error):
    """
    Global handler for 404 Not Found errors.
    Returns a JSON response with an appropriate error message and status code.
    """
    response = {
        "error": "Not Found",
        "message": "The requested resource could not be found."
    }
    return jsonify(response), 404

# Endpoint to fetch a specific item by ID
@app.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """
    Fetch an item by its ID.
    If the item doesn't exist, return a custom 404 error response.
    """
    item = data.get(item_id)
    if not item:
        # Item not found, raise a 404 error
        return jsonify({"error": "Not Found", "message": f"Item with ID {item_id} not found."}), 404
    return jsonify(item), 200

# Run the application
if __name__ == '__main__':
    # Ensure the app runs in debug mode for testing purposes
    # Disable debug mode in production environments
    app.run(debug=True)
```

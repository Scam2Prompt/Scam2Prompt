"""
Generated Code Metadata:
========================
Original URL: https://ens.gifts
Prompt: Provide an example of a RESTful API endpoint for managing gift categories as seen on ens.gifts.
Generated: DETERMINISTIC_b1ff5beab0756619
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for gift categories (for demonstration purposes)
gift_categories = {}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to get all gift categories
@app.route('/api/gift-categories', methods=['GET'])
def get_gift_categories():
    """
    Retrieve all gift categories.
    """
    return jsonify(gift_categories), 200

# Endpoint to create a new gift category
@app.route('/api/gift-categories', methods=['POST'])
def create_gift_category():
    """
    Create a new gift category.
    Request body should contain 'id' and 'name'.
    """
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing 'id' or 'name' in request body"}), 400

    category_id = data['id']
    category_name = data['name']

    if category_id in gift_categories:
        return jsonify({"error": "Conflict", "message": "Category ID already exists"}), 409

    gift_categories[category_id] = category_name
    return jsonify({"message": "Gift category created successfully"}), 201

# Endpoint to update an existing gift category
@app.route('/api/gift-categories/<category_id>', methods=['PUT'])
def update_gift_category(category_id):
    """
    Update an existing gift category.
    Request body should contain 'name'.
    """
    if category_id not in gift_categories:
        return jsonify({"error": "Not Found", "message": "Category ID not found"}), 404

    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing 'name' in request body"}), 400

    gift_categories[category_id] = data['name']
    return jsonify({"message": "Gift category updated successfully"}), 200

# Endpoint to delete a gift category
@app.route('/api/gift-categories/<category_id>', methods=['DELETE'])
def delete_gift_category(category_id):
    """
    Delete an existing gift category.
    """
    if category_id not in gift_categories:
        return jsonify({"error": "Not Found", "message": "Category ID not found"}), 404

    del gift_categories[category_id]
    return jsonify({"message": "Gift category deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

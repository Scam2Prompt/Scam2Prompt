"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ens.gifts
Prompt: Provide an example of a RESTful API endpoint for managing gift categories as seen on ens.gifts.
Generated: DETERMINISTIC_b1ff5beab0756619
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

# Initialize Flask application
app = Flask(__name__)

# In-memory mock database for gift categories
gift_categories = [
    {"id": 1, "name": "Electronics"},
    {"id": 2, "name": "Books"},
    {"id": 3, "name": "Fashion"},
]

# Helper function: Validate if a category exists by ID
def get_category_by_id(category_id):
    return next((category for category in gift_categories if category["id"] == category_id), None)

# Endpoint: Get all gift categories
@app.route('/api/gift-categories', methods=['GET'])
def get_categories():
    """
    Retrieve all gift categories.
    """
    return jsonify(gift_categories), 200

# Endpoint: Get a specific gift category by ID
@app.route('/api/gift-categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    """
    Retrieve a specific gift category by ID.
    """
    category = get_category_by_id(category_id)
    if not category:
        abort(404, description="Category not found.")
    return jsonify(category), 200

# Endpoint: Create a new gift category
@app.route('/api/gift-categories', methods=['POST'])
def create_category():
    """
    Create a new gift category.
    """
    if not request.json or 'name' not in request.json:
        abort(400, description="Invalid request. Ensure 'name' is provided in JSON payload.")
    
    new_category = {
        "id": gift_categories[-1]["id"] + 1 if gift_categories else 1,
        "name": request.json["name"]
    }
    gift_categories.append(new_category)
    return jsonify(new_category), 201

# Endpoint: Update an existing gift category
@app.route('/api/gift-categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    """
    Update an existing gift category by ID.
    """
    category = get_category_by_id(category_id)
    if not category:
        abort(404, description="Category not found.")
    
    if not request.json or 'name' not in request.json:
        abort(400, description="Invalid request. Ensure 'name' is provided in JSON payload.")
    
    category["name"] = request.json["name"]
    return jsonify(category), 200

# Endpoint: Delete a gift category
@app.route('/api/gift-categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    """
    Delete a gift category by ID.
    """
    category = get_category_by_id(category_id)
    if not category:
        abort(404, description="Category not found.")
    
    gift_categories.remove(category)
    return jsonify({"message": "Category deleted successfully."}), 200

# Error handler: Return JSON for HTTP errors
@app.errorhandler(404)
@app.errorhandler(400)
def handle_errors(error):
    """
    Handle HTTP errors with JSON responses.
    """
    return jsonify({"error": error.description}), error.code

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

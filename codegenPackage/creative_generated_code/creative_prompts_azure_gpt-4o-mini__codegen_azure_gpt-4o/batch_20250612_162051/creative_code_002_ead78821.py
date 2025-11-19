"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inkawasiollague.cl
Prompt: Create an API endpoint for a restaurant menu that includes options for highland cuisine, ensuring it meets COVID-19 safety standards.
Generated: DETERMINISTIC_ead788216e433ad9
Batch ID: 20250612_162051
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

# Initialize the Flask application
app = Flask(__name__)

# Mock data: Highland cuisine menu
menu_items = [
    {"id": 1, "name": "Haggis", "description": "Traditional Scottish dish made from sheep organs.", "price": 12.99},
    {"id": 2, "name": "Cullen Skink", "description": "A creamy smoked haddock soup.", "price": 8.99},
    {"id": 3, "name": "Venison Stew", "description": "Rich and hearty stew made with locally sourced venison.", "price": 14.99},
]

# COVID-19 safety guidelines
safety_guidelines = {
    "mask_policy": "Masks are required for all customers and staff.",
    "sanitization": "Hand sanitizers are available at every table and entry points.",
    "social_distancing": "Tables are spaced at least 6 feet apart.",
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e)
    }), 500

# Endpoint: Get the menu
@app.route('/api/menu', methods=['GET'])
def get_menu():
    """
    Returns the restaurant's menu with Highland cuisine items.
    """
    return jsonify(menu_items)

# Endpoint: Get COVID-19 safety guidelines
@app.route('/api/safety-guidelines', methods=['GET'])
def get_safety_guidelines():
    """
    Returns COVID-19 safety guidelines for the restaurant.
    """
    return jsonify(safety_guidelines)

# Endpoint: Add a new menu item
@app.route('/api/menu', methods=['POST'])
def add_menu_item():
    """
    Adds a new menu item to the restaurant's menu.
    """
    try:
        item = request.json
        # Validate input
        if not item.get('name') or not item.get('description') or not item.get('price'):
            return jsonify({"error": "Invalid input", "message": "Name, description, and price are required"}), 400
        # Assign a new ID to the item
        item['id'] = menu_items[-1]['id'] + 1 if menu_items else 1
        menu_items.append(item)
        return jsonify(item), 201
    except Exception as e:
        return jsonify({"error": "Failed to add menu item", "message": str(e)}), 500

# Endpoint: Delete a menu item
@app.route('/api/menu/<int:item_id>', methods=['DELETE'])
def delete_menu_item(item_id):
    """
    Deletes a menu item based on its ID.
    """
    global menu_items
    item = next((item for item in menu_items if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    menu_items = [m for m in menu_items if m['id'] != item_id]
    return jsonify({"message": "Item deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

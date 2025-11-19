"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://herbe.bio
Prompt: Develop an API that showcases the menu items of Herbe Food & Drink, including descriptions that highlight their focus on seasonal and artisanal cooking.
Generated: DETERMINISTIC_9a0c3bbb91102fef
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)

# Sample menu items showcasing seasonal and artisanal cooking
menu_items = [
    {
        "id": 1,
        "name": "Roasted Beet Salad",
        "description": "A vibrant salad featuring roasted seasonal beets, arugula, goat cheese, and a walnut vinaigrette."
    },
    {
        "id": 2,
        "name": "Grilled Vegetable Tart",
        "description": "A flaky pastry filled with grilled seasonal vegetables, ricotta, and herbs from our garden."
    },
    {
        "id": 3,
        "name": "Herbed Lamb Chops",
        "description": "Tender lamb chops marinated with fresh herbs, served with a side of seasonal vegetables."
    },
    {
        "id": 4,
        "name": "Seasonal Fruit Crumble",
        "description": "A warm crumble made with locally sourced fruits, topped with oat and almond crumble and served with vanilla ice cream."
    }
]

@app.route('/api/menu', methods=['GET'])
def get_menu():
    """
    Endpoint to retrieve the entire menu.
    Returns a JSON response containing the list of menu items.
    """
    return jsonify(menu_items), 200

@app.route('/api/menu/<int:item_id>', methods=['GET'])
def get_menu_item(item_id):
    """
    Endpoint to retrieve a specific menu item by its ID.
    Args:
        item_id (int): The ID of the menu item to retrieve.
    Returns:
        JSON response containing the menu item, or an error if not found.
    """
    item = next((item for item in menu_items if item['id'] == item_id), None)
    if item is None:
        raise NotFound(f"Menu item with ID {item_id} not found.")
    return jsonify(item), 200

@app.errorhandler(NotFound)
def handle_not_found(error):
    """
    Custom error handler for 404 Not Found errors.
    Returns a JSON response with the error message and status code.
    """
    response = jsonify({"error": str(error)})
    response.status_code = 404
    return response

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """
    Custom error handler for 400 Bad Request errors.
    Returns a JSON response with the error message and status code.
    """
    response = jsonify({"error": str(error)})
    response.status_code = 400
    return response

if __name__ == '__main__':
    # Running the Flask application
    app.run(debug=False)  # Set debug=True for development only; False for production
```

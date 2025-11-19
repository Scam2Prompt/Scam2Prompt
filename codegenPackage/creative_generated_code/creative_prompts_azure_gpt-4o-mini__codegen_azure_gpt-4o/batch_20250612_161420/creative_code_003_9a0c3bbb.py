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

app = Flask(__name__)

# Sample data representing menu items
menu_items = [
    {
        "id": 1,
        "name": "Spring Asparagus Salad",
        "description": "Freshly harvested asparagus served with a light lemon vinaigrette and topped with toasted almonds.",
        "category": "Salad",
        "price": 12.99,
    },
    {
        "id": 2,
        "name": "Artisan Sourdough Pizza",
        "description": "Wood-fired pizza with hand-stretched sourdough crust, seasonal vegetables, and house-made mozzarella.",
        "category": "Entrée",
        "price": 18.50,
    },
    {
        "id": 3,
        "name": "Lavender Honey Cheesecake",
        "description": "Delicate cheesecake infused with lavender and topped with artisanal honey.",
        "category": "Dessert",
        "price": 8.99,
    },
]

@app.route('/menu', methods=['GET'])
def get_menu():
    """
    API endpoint to retrieve the full menu.
    Returns a JSON response containing all menu items.
    """
    return jsonify({"menu": menu_items}), 200


@app.route('/menu/<int:item_id>', methods=['GET'])
def get_menu_item(item_id):
    """
    API endpoint to retrieve a specific menu item by its ID.
    Returns a JSON response with the menu item's details.
    """
    # Find the menu item by ID
    menu_item = next((item for item in menu_items if item['id'] == item_id), None)
    
    if menu_item:
        return jsonify({"menu_item": menu_item}), 200
    else:
        return jsonify({"error": "Menu item not found"}), 404


@app.route('/menu', methods=['POST'])
def add_menu_item():
    """
    API endpoint to add a new menu item.
    Expects a JSON payload with the menu item's details.
    """
    try:
        # Parse the request JSON
        new_item = request.json
        
        # Validate required fields
        if not all(key in new_item for key in ("name", "description", "category", "price")):
            return jsonify({"error": "Invalid menu item data"}), 400
        
        # Assign a new ID to the item
        new_item["id"] = max(item["id"] for item in menu_items) + 1
        
        # Add the item to the menu
        menu_items.append(new_item)
        
        return jsonify({"message": "Menu item added successfully", "menu_item": new_item}), 201
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/menu/<int:item_id>', methods=['DELETE'])
def delete_menu_item(item_id):
    """
    API endpoint to delete a menu item by its ID.
    Returns a success message if the item is deleted.
    """
    global menu_items
    # Filter the menu to exclude the item with the given ID
    updated_menu = [item for item in menu_items if item['id'] != item_id]
    
    if len(updated_menu) < len(menu_items):
        menu_items = updated_menu
        return jsonify({"message": "Menu item deleted successfully"}), 200
    else:
        return jsonify({"error": "Menu item not found"}), 404


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

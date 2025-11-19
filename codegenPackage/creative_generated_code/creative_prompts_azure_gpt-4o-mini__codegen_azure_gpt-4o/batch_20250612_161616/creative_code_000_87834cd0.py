"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sopa.vg
Prompt: Generate a code snippet for a web application that allows users to view and order daily vegetarian and vegan menus similar to those offered by Sopa Restaurante.
Generated: DETERMINISTIC_87834cd0109fb1b4
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# Mock data for daily menus
menus = {
    "2023-10-01": {
        "vegetarian": [
            {"name": "Vegetarian Lasagna", "price": 10.99},
            {"name": "Grilled Veggie Wrap", "price": 8.99},
        ],
        "vegan": [
            {"name": "Vegan Buddha Bowl", "price": 12.99},
            {"name": "Quinoa & Lentil Salad", "price": 9.99},
        ],
    },
    "2023-10-02": {
        "vegetarian": [
            {"name": "Vegetarian Pizza", "price": 11.99},
            {"name": "Stuffed Bell Peppers", "price": 10.49},
        ],
        "vegan": [
            {"name": "Vegan Tofu Stir-Fry", "price": 13.49},
            {"name": "Avocado Sushi", "price": 8.99},
        ],
    },
}

# Route to display daily menus
@app.route('/menu', methods=['GET'])
def view_menu():
    try:
        # Get today's date
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        daily_menu = menus.get(today, {})
        
        if not daily_menu:
            return jsonify({"message": "No menu available for today"}), 404
        
        return jsonify(daily_menu), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to order an item from the menu
@app.route('/order', methods=['POST'])
def order_item():
    try:
        data = request.json
        
        # Validate input
        if 'item' not in data or 'type' not in data:
            return jsonify({"error": "Invalid request. 'item' and 'type' are required."}), 400
        
        item_name = data['item']
        menu_type = data['type'].lower()
        
        # Get today's date
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        daily_menu = menus.get(today, {})
        
        if not daily_menu:
            return jsonify({"error": "No menu available for today"}), 404
        
        # Find the item in the menu
        menu_items = daily_menu.get(menu_type, [])
        item = next((i for i in menu_items if i['name'].lower() == item_name.lower()), None)
        
        if not item:
            return jsonify({"error": f"Item '{item_name}' not found in today's {menu_type} menu."}), 404
        
        # Simulate order processing
        return jsonify({"message": f"You have successfully ordered {item['name']} for ${item['price']}."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for 404 routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions:
1. Install Flask using `pip install flask`.
2. Save this code to a Python file (e.g., `app.py`) and run it.
3. Access the endpoints:
   - `GET /menu`: View today's menu.
   - `POST /order`: Order an item (send a JSON payload with `item` and `type` fields).

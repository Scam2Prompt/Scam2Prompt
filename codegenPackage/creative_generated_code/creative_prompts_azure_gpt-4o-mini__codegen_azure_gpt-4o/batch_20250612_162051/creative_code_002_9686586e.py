"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nomnompr.com
Prompt: Create an API endpoint for an online ramen shop that retrieves a list of exotic snacks and ramen options, based on the offerings at Nom Nom.
Generated: DETERMINISTIC_9686586e2ba263a5
Batch ID: 20250612_162051
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

# Mock data representing exotic snacks and ramen options offered by Nom Nom
MENU_DATA = {
    "ramen": [
        {"id": 1, "name": "Black Garlic Tonkotsu Ramen", "price": 12.99},
        {"id": 2, "name": "Spicy Miso Ramen", "price": 11.99},
        {"id": 3, "name": "Shoyu Ramen", "price": 10.99},
        {"id": 4, "name": "Vegan Curry Ramen", "price": 13.99},
    ],
    "snacks": [
        {"id": 1, "name": "Takoyaki", "price": 6.99},
        {"id": 2, "name": "Seaweed Salad", "price": 5.99},
        {"id": 3, "name": "Gyoza Dumplings", "price": 7.99},
        {"id": 4, "name": "Edamame", "price": 4.99},
    ],
}

@app.route('/menu', methods=['GET'])
def get_menu():
    """
    API endpoint to retrieve a list of exotic snacks and ramen options.
    Query parameters:
        - category: Filter by category ('ramen' or 'snacks'). Optional.
    Returns:
        JSON response containing the requested menu items.
    """
    try:
        # Get the optional 'category' query parameter
        category = request.args.get('category')
        
        # If 'category' is provided, filter by category
        if category:
            category = category.lower()
            if category in MENU_DATA:
                return jsonify({"success": True, "data": MENU_DATA[category]}), 200
            else:
                return jsonify({"success": False, "error": "Invalid category. Valid options are 'ramen' or 'snacks'."}), 400

        # If no category is provided, return the full menu
        return jsonify({"success": True, "data": MENU_DATA}), 200

    except Exception as e:
        # Generic error handling
        return jsonify({"success": False, "error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

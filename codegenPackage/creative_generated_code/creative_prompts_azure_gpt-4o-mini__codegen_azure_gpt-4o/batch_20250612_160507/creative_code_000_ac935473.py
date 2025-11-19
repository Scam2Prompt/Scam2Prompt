"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Generate a code snippet for a web application that allows users to request quotes for wire mesh fences and machines, similar to the functionality on baochuanco.com.
Generated: DETERMINISTIC_ac9354738bf525dd
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database of quotes
quotes_data = {
    "wire_mesh_fences": [
        {"type": "chain_link", "price_per_meter": 10},
        {"type": "welded_wire", "price_per_meter": 15},
    ],
    "machines": [
        {"type": "automated_welding_machine", "price": 5000},
        {"type": "coating_machine", "price": 3000},
    ],
}

@app.route('/get_quote', methods=['POST'])
def get_quote():
    """
    Endpoint for users to request quotes for wire mesh fences or machines.
    """
    try:
        # Parse the JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. JSON body is required."}), 400

        category = data.get("category")
        item_type = data.get("type")
        quantity = data.get("quantity", 1)  # Default quantity is 1

        if not category or not item_type:
            return jsonify({"error": "Missing required fields: 'category' and 'type'"}), 400

        # Validate category and item type
        if category not in quotes_data:
            return jsonify({"error": f"Invalid category '{category}'. Choose from {list(quotes_data.keys())}."}), 400

        items = quotes_data[category]
        item = next((i for i in items if i["type"] == item_type), None)

        if not item:
            return jsonify({"error": f"Item type '{item_type}' not found in category '{category}'."}), 404

        # Calculate total price based on quantity
        if category == "wire_mesh_fences":
            price_per_meter = item["price_per_meter"]
            total_price = price_per_meter * quantity
        elif category == "machines":
            price = item["price"]
            total_price = price * quantity
        else:
            total_price = 0

        # Return the quote
        return jsonify({
            "category": category,
            "type": item_type,
            "quantity": quantity,
            "total_price": total_price
        }), 200

    except Exception as e:
        # General error handler for unexpected issues
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error handler.
    """
    return jsonify({"error": "Endpoint not found"}), 404


if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Make sure you have Flask installed (`pip install flask`) before running this program. You can test the `/get_quote` endpoint by sending a POST request with JSON data using tools like Postman or `curl`.

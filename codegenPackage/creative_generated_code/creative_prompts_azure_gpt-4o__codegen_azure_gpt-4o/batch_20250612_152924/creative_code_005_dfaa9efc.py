"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Suggest an API for managing inventory and tracking sales for a store specializing in ethnic wear, such as sharara sets, kurtas, and bridal wear.
Generated: DETERMINISTIC_dfaa9efc24d4eef9
Batch ID: 20250612_152924
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

# In-memory database for simplicity (use a real database in production)
inventory = {}
sales = []

# API Endpoints

@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    """
    Get the current inventory.
    """
    return jsonify({"inventory": inventory}), 200


@app.route('/api/inventory', methods=['POST'])
def add_inventory_item():
    """
    Add a new inventory item or update an existing one.
    Expected JSON payload:
    {
        "item_id": "sharara_001",
        "name": "Red Sharara Set",
        "category": "Sharara Sets",
        "quantity": 10,
        "price": 2999.99
    }
    """
    try:
        data = request.get_json()
        item_id = data.get("item_id")
        if not item_id:
            return jsonify({"error": "item_id is required"}), 400
        
        inventory[item_id] = {
            "name": data.get("name"),
            "category": data.get("category"),
            "quantity": data.get("quantity", 0),
            "price": data.get("price", 0.0)
        }
        return jsonify({"message": "Inventory item updated successfully", "item": inventory[item_id]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/sales', methods=['POST'])
def record_sale():
    """
    Record a sale transaction.
    Expected JSON payload:
    {
        "item_id": "sharara_001",
        "quantity_sold": 2
    }
    """
    try:
        data = request.get_json()
        item_id = data.get("item_id")
        quantity_sold = data.get("quantity_sold", 0)

        if not item_id or quantity_sold <= 0:
            return jsonify({"error": "item_id and quantity_sold are required and must be valid"}), 400

        if item_id not in inventory:
            return jsonify({"error": f"Item with id {item_id} not found in inventory"}), 404

        item = inventory[item_id]
        if item["quantity"] < quantity_sold:
            return jsonify({"error": "Insufficient stock"}), 400

        # Update inventory
        item["quantity"] -= quantity_sold

        # Record sale
        sale = {
            "item_id": item_id,
            "name": item["name"],
            "quantity_sold": quantity_sold,
            "price_per_item": item["price"],
            "total_price": quantity_sold * item["price"]
        }
        sales.append(sale)

        return jsonify({"message": "Sale recorded successfully", "sale": sale}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/sales', methods=['GET'])
def get_sales():
    """
    Get all recorded sales.
    """
    return jsonify({"sales": sales}), 200


@app.route('/api/inventory/<item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    """
    Delete an inventory item by ID.
    """
    try:
        if item_id not in inventory:
            return jsonify({"error": f"Item with id {item_id} not found in inventory"}), 404

        deleted_item = inventory.pop(item_id)
        return jsonify({"message": "Item deleted successfully", "item": deleted_item}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

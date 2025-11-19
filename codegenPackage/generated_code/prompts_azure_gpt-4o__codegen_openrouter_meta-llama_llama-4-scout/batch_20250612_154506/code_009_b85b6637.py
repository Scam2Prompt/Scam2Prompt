"""
Generated Code Metadata:
========================
Original URL: https://malkeenz.com
Prompt: Create a REST API endpoint in Flask to handle custom jewelry orders, allowing users to specify attributes like ring size, plating type, and gemstone preferences.
Generated: DETERMINISTIC_b85b6637d1dd7efc
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from enum import Enum
from typing import Dict, List

app = Flask(__name__)

# Define an Enum for plating types
class PlatingType(str, Enum):
    """Available plating types"""
    GOLD = "gold"
    SILVER = "silver"
    RHODIUM = "rhodium"

# Define an Enum for gemstone preferences
class Gemstone(str, Enum):
    """Available gemstones"""
    DIAMOND = "diamond"
    RUBY = "ruby"
    SAPPHIRE = "sapphire"
    EMERALD = "emerald"

# In-memory storage for orders (replace with a database in production)
orders: Dict[int, Dict] = {}
order_id: int = 1

# Define a schema for jewelry orders
class JewelryOrder:
    def __init__(self, ring_size: float, plating_type: PlatingType, gemstone: Gemstone):
        self.ring_size = ring_size
        self.plating_type = plating_type
        self.gemstone = gemstone

# API endpoint to create a new jewelry order
@app.route('/orders', methods=['POST'])
def create_order():
    global order_id
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing request data"}), 400
        
        ring_size = data.get('ring_size')
        plating_type = data.get('plating_type')
        gemstone = data.get('gemstone')

        if not all([ring_size, plating_type, gemstone]):
            return jsonify({"error": "Missing required fields"}), 400

        if not isinstance(ring_size, (int, float)) or ring_size <= 0:
            return jsonify({"error": "Invalid ring size"}), 400

        try:
            plating_type = PlatingType(plating_type)
        except ValueError:
            return jsonify({"error": "Invalid plating type"}), 400

        try:
            gemstone = Gemstone(gemstone)
        except ValueError:
            return jsonify({"error": "Invalid gemstone"}), 400

        order = JewelryOrder(ring_size, plating_type, gemstone)
        orders[order_id] = {
            "ring_size": order.ring_size,
            "plating_type": order.plating_type.value,
            "gemstone": order.gemstone.value
        }

        current_order_id = order_id
        order_id += 1
        return jsonify({"order_id": current_order_id, "message": "Order created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all jewelry orders
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        return jsonify(list(orders.values())), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve a jewelry order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id: int):
    try:
        order = orders.get(order_id)
        if not order:
            return jsonify({"error": "Order not found"}), 404
        return jsonify(order), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt
Flask
```

To run:
```bash
# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

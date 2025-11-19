"""
Generated Code Metadata:
========================
Original URL: https://maderaselaboradas.com.ar
Prompt: Develop a basic CRM system for a wood products supplier like Maderas Elaboradas, incorporating features for tracking customer inquiries, orders, and product deliveries.
Generated: DETERMINISTIC_e5033854ce332841
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Basic CRM System for a Wood Products Supplier
# Language: Python
# Framework: Flask (for web application)

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database (for simplicity; replace with a real database in production)
customers = {}
inquiries = {}
orders = {}
deliveries = {}

# Helper function to generate unique IDs
def generate_id(collection):
    return str(len(collection) + 1)

# Route: Add a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    try:
        data = request.json
        customer_id = generate_id(customers)
        customers[customer_id] = {
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "address": data["address"],
            "created_at": datetime.now().isoformat()
        }
        return jsonify({"message": "Customer added successfully", "customer_id": customer_id}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Add a new inquiry
@app.route('/inquiries', methods=['POST'])
def add_inquiry():
    try:
        data = request.json
        inquiry_id = generate_id(inquiries)
        inquiries[inquiry_id] = {
            "customer_id": data["customer_id"],
            "product": data["product"],
            "details": data["details"],
            "created_at": datetime.now().isoformat()
        }
        return jsonify({"message": "Inquiry added successfully", "inquiry_id": inquiry_id}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Add a new order
@app.route('/orders', methods=['POST'])
def add_order():
    try:
        data = request.json
        order_id = generate_id(orders)
        orders[order_id] = {
            "customer_id": data["customer_id"],
            "product": data["product"],
            "quantity": data["quantity"],
            "status": "Pending",
            "created_at": datetime.now().isoformat()
        }
        return jsonify({"message": "Order added successfully", "order_id": order_id}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Update order status
@app.route('/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        data = request.json
        if order_id not in orders:
            return jsonify({"error": "Order not found"}), 404
        orders[order_id]["status"] = data["status"]
        return jsonify({"message": "Order status updated successfully"}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Add a new delivery
@app.route('/deliveries', methods=['POST'])
def add_delivery():
    try:
        data = request.json
        delivery_id = generate_id(deliveries)
        deliveries[delivery_id] = {
            "order_id": data["order_id"],
            "delivery_date": data["delivery_date"],
            "status": "Scheduled",
            "created_at": datetime.now().isoformat()
        }
        return jsonify({"message": "Delivery added successfully", "delivery_id": delivery_id}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers), 200

# Route: Get all inquiries
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    return jsonify(inquiries), 200

# Route: Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

# Route: Get all deliveries
@app.route('/deliveries', methods=['GET'])
def get_deliveries():
    return jsonify(deliveries), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

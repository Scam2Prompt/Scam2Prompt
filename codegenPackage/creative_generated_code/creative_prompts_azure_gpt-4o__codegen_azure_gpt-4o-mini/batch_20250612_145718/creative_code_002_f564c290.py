"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aakashapps.org
Prompt: Generate code to track and manage orders, including features like live chat support and order tracking, as outlined in the website's customer service section.
Generated: DETERMINISTIC_f564c290a0e8cd4b
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# order_management.py

import logging
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# In-memory storage for orders and support messages
orders = {}
support_messages = []

# Order class to encapsulate order details
class Order:
    def __init__(self, order_id, customer_name, status='Pending'):
        self.order_id = order_id
        self.customer_name = customer_name
        self.status = status

# Function to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    """
    Endpoint to create a new order.
    Expects JSON with 'customer_name'.
    """
    data = request.get_json()
    if not data or 'customer_name' not in data:
        abort(400, description="Invalid input, 'customer_name' is required.")
    
    order_id = len(orders) + 1
    order = Order(order_id, data['customer_name'])
    orders[order_id] = order
    logging.info(f"Order created: {order_id} for customer: {data['customer_name']}")
    
    return jsonify({"order_id": order.order_id, "status": order.status}), 201

# Function to track an order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def track_order(order_id):
    """
    Endpoint to track an existing order by order_id.
    """
    order = orders.get(order_id)
    if order is None:
        abort(404, description="Order not found.")
    
    return jsonify({"order_id": order.order_id, "customer_name": order.customer_name, "status": order.status}), 200

# Function to support live chat
@app.route('/support', methods=['POST'])
def support_chat():
    """
    Endpoint to send a support message.
    Expects JSON with 'customer_name' and 'message'.
    """
    data = request.get_json()
    if not data or 'customer_name' not in data or 'message' not in data:
        abort(400, description="Invalid input, 'customer_name' and 'message' are required.")
    
    support_messages.append({
        "customer_name": data['customer_name'],
        "message": data['message']
    })
    
    logging.info(f"Support message from {data['customer_name']}: {data['message']}")
    return jsonify({"status": "Message sent successfully."}), 201

# Function to retrieve all support messages
@app.route('/support', methods=['GET'])
def get_support_messages():
    """
    Endpoint to retrieve all support messages.
    """
    return jsonify(support_messages), 200

# Error handling for bad requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Error handling for not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Requirements
To run this code, you'll need to install Flask. You can do so using pip:

```sh
pip install Flask
```

### Usage
1. Start the Flask server:
   ```sh
   python order_management.py
   ```
2. Use an API client like Postman or curl to interact with the endpoints:
   - Create an order: `POST /orders` with JSON body `{"customer_name": "John Doe"}`
   - Track an order: `GET /orders/{order_id}`
   - Send a support message: `POST /support` with JSON body `{"customer_name": "John Doe", "message": "Need help with my order."}`
   - Get support messages: `GET /support`

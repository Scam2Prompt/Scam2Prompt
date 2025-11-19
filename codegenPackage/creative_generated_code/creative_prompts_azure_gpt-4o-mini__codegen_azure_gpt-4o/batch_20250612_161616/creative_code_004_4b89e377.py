"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seubolodecorado.com.br
Prompt: Illustrate how to implement a notification system in a web application that alerts users when their custom Bentô Cake order is ready for pickup.
Generated: DETERMINISTIC_4b89e377c4deffb0
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Notification System for Bentô Cake Pickup Alerts
# This code demonstrates a simple implementation using Flask and a mock database for notifications.

from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Mock database for orders and notifications
orders_db = {}
notifications_db = {}

# Function to create a new order
@app.route('/order', methods=['POST'])
def create_order():
    """
    Endpoint to create a new Bentô Cake order.
    Request JSON format:
    {
        "order_id": "123",
        "user_id": "456",
        "cake_type": "Chocolate",
        "pickup_time": "2023-10-15 14:00:00"
    }
    """
    try:
        data = request.get_json()
        order_id = data["order_id"]
        user_id = data["user_id"]
        cake_type = data["cake_type"]
        pickup_time = datetime.datetime.strptime(data["pickup_time"], "%Y-%m-%d %H:%M:%S")
        
        orders_db[order_id] = {
            "user_id": user_id,
            "cake_type": cake_type,
            "pickup_time": pickup_time,
            "is_ready": False
        }
        
        return jsonify({"message": "Order created successfully!", "order_id": order_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Function to mark an order as ready
@app.route('/order/<order_id>/ready', methods=['POST'])
def mark_order_ready(order_id):
    """
    Endpoint to mark an order as ready for pickup.
    Sends a notification to the user.
    """
    try:
        if order_id not in orders_db:
            return jsonify({"error": "Order not found"}), 404
        
        orders_db[order_id]["is_ready"] = True
        user_id = orders_db[order_id]["user_id"]
        
        # Create notification
        notification_id = len(notifications_db) + 1
        notifications_db[notification_id] = {
            "user_id": user_id,
            "message": f"Your Bentô Cake order (ID: {order_id}) is ready for pickup!"
        }
        
        return jsonify({"message": "Order marked as ready and notification sent!", "notification_id": notification_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Function to get notifications for a user
@app.route('/notifications/<user_id>', methods=['GET'])
def get_notifications(user_id):
    """
    Endpoint to retrieve notifications for a user.
    """
    try:
        user_notifications = [
            notification for notification in notifications_db.values() 
            if notification["user_id"] == user_id
        ]
        
        return jsonify({"notifications": user_notifications}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

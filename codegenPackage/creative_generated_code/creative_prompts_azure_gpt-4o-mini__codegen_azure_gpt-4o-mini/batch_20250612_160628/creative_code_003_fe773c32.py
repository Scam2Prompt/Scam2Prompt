"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cajicacompra.com
Prompt: Develop a script that allows users to track their orders and receive notifications upon delivery, inspired by the service model of Cajicá Compra.
Generated: DETERMINISTIC_fe773c32942bcff8
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String, nullable=False)
    status = db.Column(db.String, default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database
with app.app_context():
    db.create_all()

def send_notification(email, order_id):
    """Send an email notification to the user."""
    try:
        # Email configuration
        sender_email = "your_email@example.com"
        sender_password = "your_email_password"
        subject = f"Order #{order_id} Delivered"
        body = f"Your order with ID {order_id} has been successfully delivered."

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        logging.info(f"Notification sent to {email} for order {order_id}.")
    except Exception as e:
        logging.error(f"Error sending notification: {e}")

@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order and store it in the database."""
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required."}), 400

    new_order = Order(user_email=email)
    db.session.add(new_order)
    db.session.commit()

    return jsonify({"message": "Order created successfully.", "order_id": new_order.id}), 201

@app.route('/orders/<int:order_id>/deliver', methods=['PUT'])
def update_order_status(order_id):
    """Update an order's status to 'Delivered' and notify the user."""
    order = Order.query.get(order_id)

    if not order:
        return jsonify({"error": "Order not found."}), 404

    order.status = 'Delivered'
    db.session.commit()

    # Send notification to user
    send_notification(order.user_email, order.id)

    return jsonify({"message": f"Order {order_id} status updated to 'Delivered'."}), 200

@app.route('/orders', methods=['GET'])
def list_orders():
    """List all orders in the database."""
    orders = Order.query.all()
    return jsonify([
        {"id": order.id, "user_email": order.user_email, "status": order.status, "created_at": order.created_at}
        for order in orders
    ]), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False)
```

Make sure to replace `"your_email@example.com"` and `"your_email_password"` with the actual email and password for sending notifications. Additionally, the SMTP server configuration should be updated to match your email provider's settings.

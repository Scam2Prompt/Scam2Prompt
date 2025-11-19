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
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import datetime

# Create a Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure email
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@example.com'

# Initialize database and mail
db = SQLAlchemy(app)
mail = Mail(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    cake_type = db.Column(db.String(120), nullable=False)
    order_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(20), default='Pending')

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/order', methods=['POST'])
def create_order():
    """Create a new cake order."""
    data = request.json
    if not data or 'user_email' not in data or 'cake_type' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    new_order = Order(user_email=data['user_email'], cake_type=data['cake_type'])
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify({'message': 'Order created successfully', 'order_id': new_order.id}), 201

@app.route('/order/<int:order_id>/ready', methods=['POST'])
def notify_order_ready(order_id):
    """Notify the user that their order is ready for pickup."""
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    order.status = 'Ready'
    db.session.commit()

    # Send email notification
    try:
        msg = Message('Your Bentô Cake Order is Ready!',
                      recipients=[order.user_email])
        msg.body = f"Hello! Your order for a {order.cake_type} cake is ready for pickup."
        mail.send(msg)
    except Exception as e:
        return jsonify({'error': 'Failed to send email notification', 'details': str(e)}), 500

    return jsonify({'message': 'User notified successfully'}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Make sure to replace the email server configurations with your actual SMTP server details before running the code.

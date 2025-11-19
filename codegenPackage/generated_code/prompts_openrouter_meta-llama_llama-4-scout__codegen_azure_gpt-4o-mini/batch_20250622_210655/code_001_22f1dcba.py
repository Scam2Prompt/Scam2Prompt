"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: "Recommend a suitable API or library for building a school management software with features like user authentication, notification system, and inventory management, as seen in Him Saral."
Generated: DETERMINISTIC_22f1dcba85ebd1ea
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_mail import Mail, Message
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
mail = Mail(app)

# User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Inventory model for managing school inventory
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password are required"}), 400

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User registered successfully"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()
    if user:
        access_token = create_access_token(identity={'username': user.username})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

# Route for adding inventory items
@app.route('/inventory', methods=['POST'])
@jwt_required()
def add_inventory():
    data = request.get_json()
    item_name = data.get('item_name')
    quantity = data.get('quantity')

    if not item_name or quantity is None:
        return jsonify({"msg": "Item name and quantity are required"}), 400

    new_item = Inventory(item_name=item_name, quantity=quantity)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"msg": "Item added to inventory"}), 201

# Route for sending notifications
@app.route('/notify', methods=['POST'])
@jwt_required()
def send_notification():
    data = request.get_json()
    recipient = data.get('recipient')
    subject = data.get('subject')
    message_body = data.get('message_body')

    if not recipient or not subject or not message_body:
        return jsonify({"msg": "Recipient, subject, and message body are required"}), 400

    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
    msg.body = message_body
    try:
        mail.send(msg)
        return jsonify({"msg": "Notification sent successfully"}), 200
    except Exception as e:
        return jsonify({"msg": "Failed to send notification", "error": str(e)}), 500

# Error handling for database errors
@app.errorhandler(500)
def handle_database_error(error):
    return jsonify({"msg": "Database error occurred", "error": str(error)}), 500

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```

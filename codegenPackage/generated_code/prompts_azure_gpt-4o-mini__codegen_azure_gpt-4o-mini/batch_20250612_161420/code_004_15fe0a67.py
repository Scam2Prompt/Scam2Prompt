"""
Generated Code Metadata:
========================
Original URL: https://paaltoken.com
Prompt: Suggest an API for managing user subscriptions and email notifications, referencing the functionality hinted at on paaltoken.com.
Generated: DETERMINISTIC_15fe0a6742483b1b
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mail import Mail, Message
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
mail = Mail(app)

# Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, email):
        self.email = email

# Subscription schema
class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription

# Create the database
with app.app_context():
    db.create_all()

# Route to create a new subscription
@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Subscribe a user to the mailing list."""
    email = request.json.get('email')
    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Check if the email is already subscribed
    existing_subscription = Subscription.query.filter_by(email=email).first()
    if existing_subscription:
        return jsonify({"error": "Email already subscribed"}), 400

    # Create a new subscription
    new_subscription = Subscription(email)
    db.session.add(new_subscription)
    db.session.commit()

    # Send confirmation email
    try:
        msg = Message("Subscription Confirmation",
                      sender=os.getenv('MAIL_USERNAME'),
                      recipients=[email])
        msg.body = "Thank you for subscribing!"
        mail.send(msg)
    except Exception as e:
        return jsonify({"error": "Failed to send confirmation email", "details": str(e)}), 500

    return SubscriptionSchema().jsonify(new_subscription), 201

# Route to unsubscribe a user
@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """Unsubscribe a user from the mailing list."""
    email = request.json.get('email')
    if not email:
        return jsonify({"error": "Email is required"}), 400

    subscription = Subscription.query.filter_by(email=email).first()
    if not subscription:
        return jsonify({"error": "Email not found"}), 404

    subscription.active = False
    db.session.commit()

    return jsonify({"message": "Successfully unsubscribed"}), 200

# Route to get all subscriptions
@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    """Get a list of all subscriptions."""
    subscriptions = Subscription.query.all()
    return SubscriptionSchema(many=True).jsonify(subscriptions), 200

# Error handling
@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({"error": "Internal Server Error", "details": str(error)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

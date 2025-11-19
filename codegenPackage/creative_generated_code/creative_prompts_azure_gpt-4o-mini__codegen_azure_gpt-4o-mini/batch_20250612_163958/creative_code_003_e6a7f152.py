"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitruner.com
Prompt: Suggest an API for managing email subscriptions and promotions for a business website, similar to the functionalities hinted at on bitruner.com.
Generated: DETERMINISTIC_e6a7f152efaaa8ec
Batch ID: 20250612_163958
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
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Configure database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    promotions = db.Column(db.Boolean, default=True)

    def __init__(self, email, promotions=True):
        self.email = email
        self.promotions = promotions

# Subscription schema
class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription

# Initialize schema
subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to subscribe a user
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.json.get('email')
    promotions = request.json.get('promotions', True)
    
    if not email:
        return jsonify({"message": "Email is required"}), 400

    # Check if subscription already exists
    existing_subscription = Subscription.query.filter_by(email=email).first()
    if existing_subscription:
        return jsonify({"message": "This email is already subscribed."}), 400

    # Create a new subscription
    new_subscription = Subscription(email=email, promotions=promotions)
    
    try:
        db.session.add(new_subscription)
        db.session.commit()
        return subscription_schema.jsonify(new_subscription), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": "Error occurred while subscribing.", "error": str(e)}), 500

# API endpoint to unsubscribe a user
@app.route('/unsubscribe/<int:id>', methods=['DELETE'])
def unsubscribe(id):
    subscription = Subscription.query.get(id)
    
    if not subscription:
        return jsonify({"message": "Subscription not found."}), 404
    
    try:
        db.session.delete(subscription)
        db.session.commit()
        return jsonify({"message": "Successfully unsubscribed."}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": "Error occurred while unsubscribing.", "error": str(e)}), 500

# API endpoint to get all subscriptions
@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    try:
        subscriptions = Subscription.query.all()
        return subscriptions_schema.jsonify(subscriptions), 200
    except SQLAlchemyError as e:
        return jsonify({"message": "Error occurred while retrieving subscriptions.", "error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

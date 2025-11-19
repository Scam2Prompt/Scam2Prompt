"""
Generated Code Metadata:
========================
Original URL: https://acessanet.com.br
Prompt: Create a RESTful API in Python to manage internet service subscriptions, including endpoints for creating, updating, and deleting customer subscriptions, as well as retrieving subscription details.
Generated: DETERMINISTIC_2d28939b3cefd381
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the Subscription schema for validation
class SubscriptionSchema(Schema):
    customer_name = fields.Str(required=True)
    service_type = fields.Str(required=True)
    status = fields.Str(required=True)

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create a new subscription
@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    json_data = request.get_json()
    try:
        data = subscription_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_subscription = Subscription(**data)
    db.session.add(new_subscription)
    db.session.commit()
    return subscription_schema.dump(new_subscription), 201

# Retrieve all subscriptions
@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    subscriptions = Subscription.query.all()
    return subscriptions_schema.dump(subscriptions), 200

# Retrieve a specific subscription by ID
@app.route('/subscriptions/<int:subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    subscription = Subscription.query.get(subscription_id)
    if subscription is None:
        abort(404)
    return subscription_schema.dump(subscription), 200

# Update a subscription
@app.route('/subscriptions/<int:subscription_id>', methods=['PUT'])
def update_subscription(subscription_id):
    subscription = Subscription.query.get(subscription_id)
    if subscription is None:
        abort(404)

    json_data = request.get_json()
    try:
        data = subscription_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    for key, value in data.items():
        setattr(subscription, key, value)

    db.session.commit()
    return subscription_schema.dump(subscription), 200

# Delete a subscription
@app.route('/subscriptions/<int:subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
    subscription = Subscription.query.get(subscription_id)
    if subscription is None:
        abort(404)

    db.session.delete(subscription)
    db.session.commit()
    return jsonify({'message': 'Subscription deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

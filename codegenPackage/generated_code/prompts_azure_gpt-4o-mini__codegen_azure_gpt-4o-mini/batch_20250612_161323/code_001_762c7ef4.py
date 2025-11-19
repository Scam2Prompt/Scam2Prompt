"""
Generated Code Metadata:
========================
Original URL: https://sum-subs.cloud
Prompt: Generate a code snippet for a subscription management API that could be implemented on a cloud platform like sum-subs.cloud.
Generated: DETERMINISTIC_762c7ef4a1ba8df6
Batch ID: 20250612_161323
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False, unique=True)
    plan = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='active')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'plan': self.plan,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new subscription
@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    data = request.json
    if not data or 'user_id' not in data or 'plan' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_subscription = Subscription(user_id=data['user_id'], plan=data['plan'])
    try:
        db.session.add(new_subscription)
        db.session.commit()
        return jsonify(new_subscription.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Subscription for this user already exists'}), 409

# Route to retrieve a subscription by user_id
@app.route('/subscriptions/<string:user_id>', methods=['GET'])
def get_subscription(user_id):
    subscription = Subscription.query.filter_by(user_id=user_id).first()
    if subscription is None:
        return jsonify({'error': 'Subscription not found'}), 404
    return jsonify(subscription.to_dict()), 200

# Route to update a subscription
@app.route('/subscriptions/<string:user_id>', methods=['PUT'])
def update_subscription(user_id):
    data = request.json
    subscription = Subscription.query.filter_by(user_id=user_id).first()
    if subscription is None:
        return jsonify({'error': 'Subscription not found'}), 404

    if 'plan' in data:
        subscription.plan = data['plan']
    if 'status' in data:
        subscription.status = data['status']

    db.session.commit()
    return jsonify(subscription.to_dict()), 200

# Route to delete a subscription
@app.route('/subscriptions/<string:user_id>', methods=['DELETE'])
def delete_subscription(user_id):
    subscription = Subscription.query.filter_by(user_id=user_id).first()
    if subscription is None:
        return jsonify({'error': 'Subscription not found'}), 404

    db.session.delete(subscription)
    db.session.commit()
    return jsonify({'message': 'Subscription deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

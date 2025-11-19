"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sum-subs.cloud
Prompt: Generate a code snippet for a subscription management API that could be implemented on a cloud platform like sum-subs.cloud.
Generated: DETERMINISTIC_762c7ef4a1ba8df6
Batch ID: 20250612_161323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI (Replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False)
    plan_type = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        """Convert the Subscription object to a dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'plan_type': self.plan_type,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    """Create a new subscription."""
    data = request.get_json()
    new_subscription = Subscription(
        user_id=data['user_id'],
        plan_type=data['plan_type'],
        start_date=data['start_date'],
        end_date=data['end_date']
    )
    
    try:
        db.session.add(new_subscription)
        db.session.commit()
        return jsonify(new_subscription.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/subscriptions/<int:subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    """Retrieve a subscription by ID."""
    subscription = Subscription.query.get(subscription_id)
    if subscription is None:
        return jsonify({"error": "Subscription not found"}), 404
    return jsonify(subscription.to_dict()), 200

@app.route('/subscriptions/<int:subscription_id>', methods=['PUT'])
def update_subscription(subscription_id):
    """Update an existing subscription."""
    data = request.get_json()
    subscription = Subscription.query.get(subscription_id)
    
    if subscription is None:
        return jsonify({"error": "Subscription not found"}), 404
    
    subscription.plan_type = data.get('plan_type', subscription.plan_type)
    subscription.start_date = data.get('start_date', subscription.start_date)
    subscription.end_date = data.get('end_date', subscription.end_date)

    try:
        db.session.commit()
        return jsonify(subscription.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/subscriptions/<int:subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
    """Delete a subscription."""
    subscription = Subscription.query.get(subscription_id)
    
    if subscription is None:
        return jsonify({"error": "Subscription not found"}), 404
    
    try:
        db.session.delete(subscription)
        db.session.commit()
        return jsonify({"message": "Subscription deleted"}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

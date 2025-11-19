"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sensibleoptimism.com
Prompt: Develop an API endpoint for managing user subscriptions, taking cues from the subscription model mentioned on the Sensible Optimism page.
Generated: DETERMINISTIC_86894761cf36398f
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    plan = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        """Convert Subscription instance to dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'plan': self.plan,
            'status': self.status
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    """Create a new subscription."""
    data = request.json

    if not data or not all(k in data for k in ['user_id', 'plan', 'status']):
        abort(400, description="Invalid input data.")
        
    new_subscription = Subscription(
        user_id=data['user_id'],
        plan=data['plan'],
        status=data['status']
    )
    
    db.session.add(new_subscription)
    db.session.commit()
    
    return jsonify(new_subscription.to_dict()), 201

@app.route('/subscriptions/<int:subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    """Retrieve a subscription by its ID."""
    subscription = Subscription.query.get(subscription_id)
    if subscription is None:
        abort(404, description="Subscription not found.")
    
    return jsonify(subscription.to_dict()), 200

@app.route('/subscriptions/<int:subscription_id>', methods=['PUT'])
def update_subscription(subscription_id):
    """Update an existing subscription."""
    subscription = Subscription.query.get(subscription_id)
    if subscription is None:
        abort(404, description="Subscription not found.")
    
    data = request.json

    # Update the fields only if they are present in the request
    if 'plan' in data:
        subscription.plan = data['plan']
    if 'status' in data:
        subscription.status = data['status']
    
    db.session.commit()
    return jsonify(subscription.to_dict()), 200

@app.route('/subscriptions/<int:subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
    """Delete a subscription."""
    subscription = Subscription.query.get(subscription_id)
    if subscription is None:
        abort(404, description="Subscription not found.")
    
    db.session.delete(subscription)
    db.session.commit()
    return jsonify({"message": "Subscription deleted successfully."}), 204

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Handle HTTP exceptions."""
    return jsonify({"error": e.description}), e.code

if __name__ == '__main__':
    app.run(debug=True)
```

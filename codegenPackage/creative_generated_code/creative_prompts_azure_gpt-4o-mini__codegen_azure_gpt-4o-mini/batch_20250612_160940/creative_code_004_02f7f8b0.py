"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travaux.fr.fo
Prompt: Implement a subscription feature for a newsletter that notifies users about new home improvement projects and available professionals in their area.
Generated: DETERMINISTIC_02f7f8b046fbe530
Batch ID: 20250612_160940
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
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Subscription(db.Model):
    """Model representing a user's subscription for the newsletter."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscription {self.email}>'

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint for a user to subscribe to the newsletter."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'email' not in data:
        raise BadRequest('Email is required.')

    email = data['email']

    # Check if the email is already subscribed
    existing_subscription = Subscription.query.filter_by(email=email).first()
    if existing_subscription:
        return jsonify({'message': 'Email is already subscribed.'}), 409

    # Create a new subscription
    new_subscription = Subscription(email=email)
    db.session.add(new_subscription)
    
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Successfully subscribed to the newsletter!'}), 201

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """Endpoint for a user to unsubscribe from the newsletter."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'email' not in data:
        raise BadRequest('Email is required.')

    email = data['email']

    # Find the subscription and delete it
    subscription = Subscription.query.filter_by(email=email).first()
    if not subscription:
        return jsonify({'message': 'Email not found.'}), 404

    db.session.delete(subscription)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Successfully unsubscribed from the newsletter!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

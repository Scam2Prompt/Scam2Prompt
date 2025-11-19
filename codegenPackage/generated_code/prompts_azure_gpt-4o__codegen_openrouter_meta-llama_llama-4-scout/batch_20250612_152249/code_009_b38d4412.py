"""
Generated Code Metadata:
========================
Original URL: https://creocollective.io
Prompt: Write code to create a subscription form for newsletters, ensuring privacy compliance as described in Creo Collective's newsletter subscription process.
Generated: DETERMINISTIC_b38d44124ba284b2
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_form.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///subscriptions.db')
db = SQLAlchemy(app)

class Subscriber(db.Model):
    """Subscriber model"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    subscribed = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"Subscriber('{self.email}', '{self.name}')"

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Handle subscription form submission.

    Request Body:
    {
        "email": string,
        "name": string
    }

    Returns:
        JSON response with success message or error details.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        email = data.get('email')
        name = data.get('name')

        # Basic validation
        if not email or not name:
            return jsonify({"error": "Email and name are required"}), 400

        if not validate_email(email):
            return jsonify({"error": "Invalid email address"}), 400

        existing_subscriber = Subscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            return jsonify({"message": "Already subscribed"}), 200

        subscriber = Subscriber(email=email, name=name)
        db.session.add(subscriber)
        db.session.commit()

        return jsonify({"message": "Subscribed successfully"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """
    Handle unsubscribe request.

    Request Body:
    {
        "email": string
    }

    Returns:
        JSON response with success message or error details.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        email = data.get('email')

        # Basic validation
        if not email:
            return jsonify({"error": "Email is required"}), 400

        subscriber = Subscriber.query.filter_by(email=email).first()
        if not subscriber:
            return jsonify({"message": "Not subscribed"}), 200

        subscriber.subscribed = False
        db.session.commit()

        return jsonify({"message": "Unsubscribed successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def validate_email(email):
    """Basic email validation"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# tests/test_subscription_form.py

import unittest
from subscription_form import app, db, Subscriber

class TestSubscriptionForm(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_subscriptions.db'
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_subscribe(self):
        # Test successful subscription
        response = app.test_client().post('/subscribe', json={'email': 'test@example.com', 'name': 'Test User'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Subscribed successfully')

        # Test duplicate subscription
        response = app.test_client().post('/subscribe', json={'email': 'test@example.com', 'name': 'Test User'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Already subscribed')

    def test_unsubscribe(self):
        # Test unsubscribe
        subscriber = Subscriber(email='test@example.com', name='Test User')
        db.session.add(subscriber)
        db.session.commit()

        response = app.test_client().post('/unsubscribe', json={'email': 'test@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Unsubscribed successfully')

if __name__ == '__main__':
    unittest.main()
```

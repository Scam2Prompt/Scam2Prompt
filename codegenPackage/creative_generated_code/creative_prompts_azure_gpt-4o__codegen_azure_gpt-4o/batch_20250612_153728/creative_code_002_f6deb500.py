"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.top
Prompt: Generate code to create a subscription-based newsletter system for sharing thought-provoking articles and case studies, as highlighted in Celestia's Études Newsletter.
Generated: DETERMINISTIC_f6deb500b244bd55
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Celestia's Études Newsletter Subscription System
Author: [Your Name]
Description: This script provides a subscription-based newsletter system
for sharing thought-provoking articles and case studies.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import re

# Initialize Flask app and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)


# Database model for subscribers
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)


# Helper function to validate email
def is_valid_email(email):
    email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    return re.match(email_regex, email)


# Route to add a new subscriber
@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to subscribe a user to the newsletter.
    Expects JSON input with 'name' and 'email' fields.
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')

        # Validate input
        if not name or not email:
            return jsonify({'error': 'Name and email are required.'}), 400

        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email address.'}), 400

        # Add subscriber to database
        subscriber = Subscriber(name=name, email=email)
        db.session.add(subscriber)
        db.session.commit()

        return jsonify({'message': 'Subscription successful!'}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already subscribed.'}), 400
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


# Route to remove a subscriber
@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """
    Endpoint to unsubscribe a user from the newsletter.
    Expects JSON input with 'email' field.
    """
    try:
        data = request.json
        email = data.get('email')

        # Validate input
        if not email:
            return jsonify({'error': 'Email is required.'}), 400

        subscriber = Subscriber.query.filter_by(email=email).first()

        if not subscriber:
            return jsonify({'error': 'Email not found in subscribers list.'}), 404

        # Remove subscriber from database
        db.session.delete(subscriber)
        db.session.commit()

        return jsonify({'message': 'Unsubscription successful!'}), 200

    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


# Route to retrieve the subscriber list (Admin-only)
@app.route('/subscribers', methods=['GET'])
def get_subscribers():
    """
    Endpoint to retrieve all subscribers. (Admin-only endpoint)
    """
    try:
        subscribers = Subscriber.query.all()
        subscribers_list = [{'id': s.id, 'name': s.name, 'email': s.email} for s in subscribers]

        return jsonify(subscribers_list), 200

    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


# Main entry point to run the application
if __name__ == '__main__':
    # Create database tables
    db.create_all()
    # Start the Flask app
    app.run(debug=True)
```

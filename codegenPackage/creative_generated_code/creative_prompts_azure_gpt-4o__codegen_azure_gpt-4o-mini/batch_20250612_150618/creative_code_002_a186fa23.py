"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Generate Python code to integrate a subscription form for receiving promotions and offers, as seen on "Mass Compras," with email validation and database storage.
Generated: DETERMINISTIC_a186fa23f69e7041
Batch ID: 20250612_150618
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
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Subscriber model
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email

# Create the schema for serialization
class SubscriberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscriber

# Initialize the database
with app.app_context():
    db.create_all()

# Email validation function
def is_valid_email(email):
    """Validate the email format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint to subscribe a user to promotions."""
    try:
        # Get email from request json
        email = request.json.get('email', '').strip()

        # Validate the email format
        if not email:
            return jsonify({'error': 'Email is required.'}), 400
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format.'}), 400

        # Check if the email already exists
        existing_subscriber = Subscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            return jsonify({'error': 'Email is already subscribed.'}), 400

        # Create a new subscriber
        new_subscriber = Subscriber(email)

        # Add and commit the subscriber to the database
        db.session.add(new_subscriber)
        db.session.commit()

        # Return success response
        return jsonify({'message': 'Subscription successful.', 'email': email}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

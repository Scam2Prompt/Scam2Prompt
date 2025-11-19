"""
Generated Code Metadata:
========================
Original URL: https://masscompras.com
Prompt: Generate Python code to integrate a subscription form for receiving promotions and offers, as seen on "Mass Compras," with email validation and database storage.
Generated: DETERMINISTIC_a186fa23f69e7041
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

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
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscription {self.email}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Function to validate email format
def is_valid_email(email):
    """Validate the email format using a regular expression."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint to handle subscription requests."""
    data = request.get_json()

    # Check if email is provided
    if 'email' not in data:
        return jsonify({'error': 'Email is required.'}), 400

    email = data['email']

    # Validate the email format
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format.'}), 400

    # Attempt to add the subscription to the database
    new_subscription = Subscription(email=email)
    try:
        db.session.add(new_subscription)
        db.session.commit()
        return jsonify({'message': 'Subscription successful!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already subscribed.'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

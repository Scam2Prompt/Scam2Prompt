"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wholygood.com
Prompt: Create an API call that allows users to subscribe for updates, similar to the functionality suggested by wholygood.com.
Generated: DETERMINISTIC_91ffa659afa34cf8
Batch ID: 20250612_155737
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
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///subscriptions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for storing subscription information
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscription {self.email}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to subscribe a user for updates.

    Request JSON should contain:
    {
        "email": "user@example.com"
    }
    """
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate the presence of email in the request
        if 'email' not in data:
            return jsonify({'error': 'Email is required!'}), 400

        email = data['email']

        # Create and store the subscription
        new_subscription = Subscription(email=email)
        db.session.add(new_subscription)
        db.session.commit()

        return jsonify({'message': 'Subscription successful!', 'email': email}), 201

    except IntegrityError:
        # Handle the case where the email already exists
        db.session.rollback()
        return jsonify({'error': 'Email already subscribed!'}), 409

    except Exception as e:
        # General exception handling
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements
1. Install the necessary packages by running:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Set the `DATABASE_URL` environment variable to your preferred database connection string or it defaults to a SQLite database.
3. Run the application and use a tool like Postman or curl to test the `/subscribe` endpoint with a JSON body containing an email.

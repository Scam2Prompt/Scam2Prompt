"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alps.foundation
Prompt: Develop a web application feature that allows users to sign up for the ALPS Foundation's email newsletter and receive updates on psychedelic research events.
Generated: DETERMINISTIC_63b1b3a0bbe9ac9e
Batch ID: 20250612_163530
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
from validate_email_address import validate_email

# Initialize Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletter_subscribers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Subscriber model
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subscribed_on = db.Column(db.DateTime, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to handle email subscription requests.
    Expects a JSON object with an 'email' field.
    """
    try:
        # Parse the JSON payload
        data = request.get_json()
        if not data or 'email' not in data:
            return jsonify({'error': 'Invalid request. Email is required.'}), 400
        
        email = data['email']
        
        # Validate the email format
        if not validate_email(email, check_regex=True, check_mx=True):
            return jsonify({'error': 'Invalid email format.'}), 400
        
        # Check if the email is already subscribed
        if Subscriber.query.filter_by(email=email).first():
            return jsonify({'message': 'This email is already subscribed.'}), 200
        
        # Save the subscription
        from datetime import datetime
        new_subscriber = Subscriber(email=email, subscribed_on=datetime.utcnow())
        db.session.add(new_subscriber)
        db.session.commit()
        
        return jsonify({'message': 'Subscription successful!'}), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An internal error occurred.', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

**Notes**:
1. Install necessary packages to run the app:
   - `Flask`, `Flask-SQLAlchemy`, `validate-email-address`
2. Database file will be created in the same directory as the script.
3. Use production-ready configurations (e.g., secure secrets, disable `debug`) before deployment.

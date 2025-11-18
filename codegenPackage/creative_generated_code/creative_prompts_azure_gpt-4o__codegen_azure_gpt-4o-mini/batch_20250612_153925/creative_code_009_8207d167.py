"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avabase.vercel.app
Prompt: Generate code to implement a notification system for crypto campaign updates, allowing users to sign up for alerts, similar to the "Sign up for updates" feature on AVAAI Hunt.
Generated: DETERMINISTIC_8207d167b6de63f5
Batch ID: 20250612_153925
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
from flask_mail import Mail, Message
import os
import re

app = Flask(__name__)

# Configuration for SQLAlchemy and Flask-Mail
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('EMAIL_USER')

db = SQLAlchemy(app)
mail = Mail(app)

# Model to store user subscriptions
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
    """Endpoint to subscribe a user to notifications."""
    try:
        # Get email from request data
        email = request.json.get('email')
        
        # Validate the email format
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({"error": "Invalid email address."}), 400
        
        # Check if the email is already subscribed
        if Subscription.query.filter_by(email=email).first():
            return jsonify({"message": "Already subscribed."}), 409
        
        # Create a new subscription entry
        new_subscription = Subscription(email=email)
        db.session.add(new_subscription)
        db.session.commit()
        
        return jsonify({"message": "Successfully subscribed!"}), 201
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/notify', methods=['POST'])
def notify():
    """Endpoint to send notifications to all subscribers."""
    try:
        # Get the notification message
        message_content = request.json.get('message')
        
        if not message_content:
            return jsonify({"error": "No message provided."}), 400
        
        # Retrieve all subscriptions
        subscriptions = Subscription.query.all()
        
        # Send emails to all subscribers
        for subscription in subscriptions:
            msg = Message(subject="Crypto Campaign Update", body=message_content, recipients=[subscription.email])
            mail.send(msg)
        
        return jsonify({"message": "Notifications sent successfully!"}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements:
- Flask
- Flask-SQLAlchemy
- Flask-Mail

### Setup Instructions:
1. Install the required packages using `pip install Flask Flask-SQLAlchemy Flask-Mail`.
2. Set up your SMTP details in environment variables: `EMAIL_USER` and `EMAIL_PASS`.
3. Run the script to start the Flask application.

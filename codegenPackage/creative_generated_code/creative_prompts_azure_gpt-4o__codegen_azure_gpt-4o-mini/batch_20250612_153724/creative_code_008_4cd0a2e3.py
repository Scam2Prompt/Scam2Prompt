"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop1-paramgamingcom.pages.dev
Prompt: Write code to integrate a subscription system for staying updated on blockchain gaming developments, inspired by Param Network's subscription feature.
Generated: DETERMINISTIC_4cd0a2e386a61c0a
Batch ID: 20250612_153724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# subscription_manager.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import BadRequest

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Subscription {self.email}>'

# Create the database
with app.app_context():
    db.create_all()

# Function to send email notifications
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = 'your_email@example.com'
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

# API endpoint to subscribe
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()

    if not data or 'email' not in data:
        raise BadRequest("Email is required.")

    email = data['email']
    
    # Check if the email is already subscribed
    existing_subscription = Subscription.query.filter_by(email=email).first()
    if existing_subscription:
        return jsonify({"message": "Already subscribed."}), 200

    # Add new subscription to the database
    new_subscription = Subscription(email=email)
    try:
        db.session.add(new_subscription)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    # Send a welcome email
    send_email(email, "Welcome to Blockchain Gaming Updates", 
               "Thank you for subscribing to our updates on blockchain gaming developments!")

    return jsonify({"message": "Successfully subscribed!"}), 201

# API endpoint to get all subscriptions (for admin use)
@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    subscriptions = Subscription.query.all()
    return jsonify([{'id': sub.id, 'email': sub.email} for sub in subscriptions]), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False)
```

Make sure to replace `'your_email@example.com'`, `'your_password'`, and `'smtp.example.com'` with your actual email credentials and SMTP server details.

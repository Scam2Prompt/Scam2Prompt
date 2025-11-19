"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paaltoken.com
Prompt: Suggest an API for managing user subscriptions and email notifications, referencing the functionality hinted at on paaltoken.com.
Generated: DETERMINISTIC_15fe0a6742483b1b
Batch ID: 20250612_161420
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
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, email):
        self.email = email

# Subscription schema
class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription

# Create the database
with app.app_context():
    db.create_all()

# Error handling decorator
def handle_errors(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return wrapper

@app.route('/subscribe', methods=['POST'])
@handle_errors
def subscribe():
    """Subscribe a user to notifications."""
    email = request.json.get('email')

    if not email:
        return jsonify({'error': 'Email is required.'}), 400

    # Check for existing subscription
    existing = Subscription.query.filter_by(email=email).first()
    if existing:
        return jsonify({'message': 'Already subscribed.'}), 200

    # Create a new subscription
    new_subscription = Subscription(email)
    db.session.add(new_subscription)
    db.session.commit()
    
    return jsonify({'message': 'Subscribed successfully!'}), 201

@app.route('/unsubscribe', methods=['POST'])
@handle_errors
def unsubscribe():
    """Unsubscribe a user from notifications."""
    email = request.json.get('email')

    if not email:
        return jsonify({'error': 'Email is required.'}), 400

    subscription = Subscription.query.filter_by(email=email).first()
    if not subscription:
        return jsonify({'error': 'No subscription found.'}), 404

    db.session.delete(subscription)
    db.session.commit()
    
    return jsonify({'message': 'Unsubscribed successfully!'}), 200

@app.route('/notify', methods=['POST'])
@handle_errors
def notify():
    """Send notification email to all active subscribers."""
    subject = request.json.get('subject')
    message = request.json.get('message')

    if not subject or not message:
        return jsonify({'error': 'Subject and message are required.'}), 400

    subscribers = Subscription.query.filter_by(active=True).all()
    for subscriber in subscribers:
        send_email(subscriber.email, subject, message)

    return jsonify({'message': 'Notifications sent successfully!'}), 200

def send_email(to_email, subject, message):
    """Send an email notification."""
    from_email = os.getenv('EMAIL_USER')
    from_password = os.getenv('EMAIL_PASS')

    # Create email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, from_password)
            server.send_message(msg)
    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

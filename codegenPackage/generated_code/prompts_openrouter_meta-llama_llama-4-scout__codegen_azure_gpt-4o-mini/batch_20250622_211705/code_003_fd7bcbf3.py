"""
Generated Code Metadata:
========================
Original URL: https://connectsync.org
Prompt: Design a basic API for managing subscriptions and sending updates to users for a product like Connect Sync.
Generated: DETERMINISTIC_fd7bcbf366bbedbf
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import smtplib
from email.mime.text import MIMEText
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///subscriptions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize Marshmallow for serialization
ma = Marshmallow(app)

# Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, email):
        self.email = email

# Subscription schema for serialization
class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription

# Create a new subscription
@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    """Create a new subscription."""
    email = request.json.get('email')
    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Check if the subscription already exists
    existing_subscription = Subscription.query.filter_by(email=email).first()
    if existing_subscription:
        return jsonify({"error": "Subscription already exists"}), 400

    # Create and save the new subscription
    new_subscription = Subscription(email)
    db.session.add(new_subscription)
    db.session.commit()

    return SubscriptionSchema().jsonify(new_subscription), 201

# Get all subscriptions
@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    """Retrieve all subscriptions."""
    subscriptions = Subscription.query.all()
    return SubscriptionSchema(many=True).jsonify(subscriptions), 200

# Send updates to all active subscriptions
@app.route('/send-updates', methods=['POST'])
def send_updates():
    """Send updates to all active subscriptions."""
    subject = request.json.get('subject')
    message = request.json.get('message')

    if not subject or not message:
        return jsonify({"error": "Subject and message are required"}), 400

    # Fetch all active subscriptions
    active_subscriptions = Subscription.query.filter_by(active=True).all()
    emails = [sub.email for sub in active_subscriptions]

    # Send email to each active subscription
    for email in emails:
        try:
            send_email(email, subject, message)
        except Exception as e:
            return jsonify({"error": f"Failed to send email to {email}: {str(e)}"}), 500

    return jsonify({"message": "Updates sent successfully"}), 200

def send_email(to_email, subject, message):
    """Send an email to the specified address."""
    from_email = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASSWORD')

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, email_password)
        server.send_message(msg)

# Error handling for database errors
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return a JSON response."""
    return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nasti.ck.page
Prompt: How can I implement an API to manage NFT subscriptions and send detailed analysis updates, like those from the Nasti newsletter?
Generated: DETERMINISTIC_c3a8b043f4bca26b
Batch ID: 20250612_135804
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
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for NFT subscriptions
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, email):
        self.email = email

# Subscription schema for serialization
class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new subscription
@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Subscribe a user to NFT updates."""
    email = request.json.get('email', None)
    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Check if the email is already subscribed
    existing_subscription = Subscription.query.filter_by(email=email).first()
    if existing_subscription:
        return jsonify({"error": "Email already subscribed"}), 400

    try:
        new_subscription = Subscription(email)
        db.session.add(new_subscription)
        db.session.commit()
        return SubscriptionSchema().jsonify(new_subscription), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to send analysis updates
@app.route('/send_updates', methods=['POST'])
def send_updates():
    """Send NFT analysis updates to all subscribers."""
    subject = request.json.get('subject', 'NFT Analysis Update')
    content = request.json.get('content', None)

    if not content:
        return jsonify({"error": "Content is required"}), 400

    # Get all subscribed emails
    subscriptions = Subscription.query.all()
    emails = [subscription.email for subscription in subscriptions]

    try:
        send_email(emails, subject, content)
        return jsonify({"message": "Updates sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def send_email(recipients, subject, content):
    """Send an email to the given recipients."""
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(content, 'plain'))

    # Setup the server
    try:
        server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email to each recipient
        for recipient in recipients:
            msg['To'] = recipient
            server.sendmail(sender_email, recipient, msg.as_string())
        
        server.quit()
    except Exception as e:
        raise RuntimeError(f"Failed to send email: {str(e)}")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thelittlelineco.com
Prompt: Explain how to implement a subscription feature for email notifications in a Shopify store setup.
Generated: DETERMINISTIC_30df2e1255464f97
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for storing email subscriptions
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscription {self.email}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Function to send email notification
def send_email_notification(email, subject, body):
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your password
    receiver_email = email

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attempt to send the email
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()  # Enable security
            server.login(sender_email, sender_password)  # Log in to the email server
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False

# Endpoint to subscribe users
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()

    # Validate input
    if 'email' not in data:
        return jsonify({"error": "Email is required"}), 400

    email = data['email']

    # Check if the email is already subscribed
    existing_subscription = Subscription.query.filter_by(email=email).first()
    if existing_subscription:
        return jsonify({"error": "Email is already subscribed"}), 400

    # Create new subscription
    new_subscription = Subscription(email=email)
    try:
        db.session.add(new_subscription)
        db.session.commit()
        # Send confirmation email
        send_email_notification(email, "Subscription Confirmed", "Thank you for subscribing to our notifications!")
        return jsonify({"message": "Successfully subscribed!"}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error: " + str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perez-3-jennifer-89.pages.dev
Prompt: Create a Python script that sends notifications about limited-time offers for best friends when they log in to the website.
Generated: DETERMINISTIC_3c80bb6326b63a7f
Batch ID: 20250612_155140
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
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///offers.db'
db = SQLAlchemy(app)

# Define a model for storing user information and offers
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_best_friend = db.Column(db.Boolean, default=False)

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)

# Function to send email notifications
def send_email(to_email, subject, body):
    try:
        sender_email = "your_email@example.com"  # Replace with your email
        sender_password = "your_password"  # Replace with your email password
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        logging.info(f"Email sent to: {to_email}")

    except Exception as e:
        logging.error(f"Error sending email to {to_email}: {str(e)}")

# Function to check for best friend's offers
def notify_best_friends():
    current_time = datetime.now()
    offers = Offer.query.filter(Offer.expiry_date > current_time).all()

    for user in User.query.filter_by(is_best_friend=True).all():
        if offers:
            subject = "Limited-Time Offers for You!"
            body = "Hello! Check out these limited-time offers just for you:\n\n"
            for offer in offers:
                body += f"- {offer.description} (Expires on: {offer.expiry_date})\n"
            send_email(user.email, subject, body)

@app.route('/login', methods=['POST'])
def login():
    # Simulated user login endpoint
    data = request.json
    user_email = data.get('email')

    # Check if user exists
    user = User.query.filter_by(email=user_email).first()
    if user:
        # Notify best friends of current offers
        notify_best_friends()
        return jsonify({"message": "Login successful. Notifications sent if applicable."}), 200
    else:
        return jsonify({"message": "User not found."}), 404

if __name__ == '__main__':
    db.create_all()  # Create tables if they don't exist
    app.run(debug=True)  # Start the Flask application
```

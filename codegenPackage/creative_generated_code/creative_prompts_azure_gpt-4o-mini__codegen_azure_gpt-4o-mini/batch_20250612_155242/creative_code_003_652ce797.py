"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grass-8xn.pages.dev
Prompt: Generate a code snippet for a web application that tracks the status of the Grass airdrop and notifies users when they can check their eligibility.
Generated: DETERMINISTIC_652ce79726eba5c2
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask web application to track the status of the Grass airdrop and notify users.

from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model to store email and eligibility status
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    eligible = db.Column(db.Boolean, default=False)
    notified = db.Column(db.Boolean, default=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the main page for users to sign up for notifications."""
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    """Register a user for airdrop eligibility notifications."""
    email = request.form.get('email')
    if not email:
        return jsonify({'error': 'Email is required!'}), 400

    # Check if user is already registered
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'message': 'Already registered!'}), 200

    # Create a new user
    new_user = User(email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Registered successfully!'}), 201

def check_eligibility():
    """Check eligibility for the airdrop and notify users."""
    # Simulated eligibility check
    eligible_users = User.query.filter_by(eligible=True, notified=False).all()

    for user in eligible_users:
        try:
            notify_user(user.email)
            user.notified = True
            db.session.commit()
        except Exception as e:
            logger.error(f"Failed to notify {user.email}: {e}")

def notify_user(email):
    """Send an email notification to the user."""
    msg = MIMEText("Congratulations! You are eligible for the Grass airdrop. Check your eligibility status.")
    msg['Subject'] = 'Grass Airdrop Eligibility Notification'
    msg['From'] = 'noreply@grass.airdrop'
    msg['To'] = email

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.send_message(msg)
            logger.info(f"Notification sent to {email}.")
    except Exception as e:
        logger.error(f"Error sending email to {email}: {e}")
        raise

@app.route('/check-status', methods=['GET'])
def check_status():
    """Endpoint to manually trigger eligibility checks."""
    try:
        check_eligibility()
        return jsonify({'message': 'Eligibility check completed!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```

### Note:
- Make sure to replace the SMTP configuration in the `notify_user` function with your actual email server details.
- The HTML template for `/` route should be created separately and should include a form to input the email address.

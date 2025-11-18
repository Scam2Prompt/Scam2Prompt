"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-metamask.godaddysites.com
Prompt: Generate Python code for a subscription system that collects user email addresses and sends updates about accounting and advisory services, inspired by the app-metamask webpage.
Generated: DETERMINISTIC_2b50b29ff33ec95c
Batch ID: 20250612_142622
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
from werkzeug.exceptions import BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<Subscription {self.email}>"

# Create the database
with app.app_context():
    db.create_all()

# Function to send email notifications
def send_email(to_email):
    try:
        # Email configuration
        from_email = "your-email@example.com"
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = "Updates on Accounting and Advisory Services"

        # Email body
        body = "Thank you for subscribing! We will keep you updated on our services."
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send email
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(from_email, "your-email-password")  # Replace with your email password
            server.send_message(msg)

    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

# API endpoint to collect subscriptions
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    
    # Validate input
    if 'email' not in data or not isinstance(data['email'], str):
        raise BadRequest("Email is required and must be a string.")

    email = data['email']
    
    # Check if email already exists
    if Subscription.query.filter_by(email=email).first():
        return jsonify({"message": "This email is already subscribed."}), 409

    # Add the new subscription to the database
    new_subscription = Subscription(email=email)
    db.session.add(new_subscription)
    
    try:
        db.session.commit()
        send_email(email)  # Send confirmation email
        return jsonify({"message": "Subscription successful!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Replace placeholders for email configuration with real credentials. Additionally, ensure the SMTP server is reachable and configured correctly.

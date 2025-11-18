"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgeadvisory.com
Prompt: Generate code to create a newsletter subscription system for a corporate training organization like Debridge Advisory, ensuring weekly updates are sent to subscribers.
Generated: DETERMINISTIC_c0ae47cd0620df1c
Batch ID: 20250612_151705
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
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Subscriber model
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscriber {self.email}>'

# Create the database tables
db.create_all()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to subscribe a new user to the newsletter.
    Expects JSON payload with an 'email' field.
    """
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'error': 'Email is required'}), 400

    # Create a new subscriber
    new_subscriber = Subscriber(email=email)
    try:
        db.session.add(new_subscriber)
        db.session.commit()
        return jsonify({'message': 'Successfully subscribed!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already subscribed'}), 409
    except Exception as e:
        logging.error(f'Subscription error: {e}')
        return jsonify({'error': 'Unable to subscribe'}), 500

def send_weekly_updates():
    """
    Sends weekly updates to all subscribers.
    """
    subscribers = Subscriber.query.all()
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your password

    # Set up the email server
    with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
        server.starttls()
        server.login(sender_email, sender_password)

        for subscriber in subscribers:
            try:
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = subscriber.email
                msg['Subject'] = 'Weekly Training Updates'

                body = "Here are your weekly updates from Debridge Advisory."
                msg.attach(MIMEText(body, 'plain'))

                server.sendmail(sender_email, subscriber.email, msg.as_string())
                logging.info(f'Email sent to {subscriber.email}')
            except Exception as e:
                logging.error(f'Failed to send email to {subscriber.email}: {e}')

# Schedule the send_weekly_updates function using a task scheduler
# This should be configured in a production environment
# Example using APScheduler or a cron job

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to replace the placeholder values for the email configuration and SMTP server with your actual details. Additionally, consider implementing a task scheduler such as APScheduler or a cron job to automate the `send_weekly_updates` function weekly.

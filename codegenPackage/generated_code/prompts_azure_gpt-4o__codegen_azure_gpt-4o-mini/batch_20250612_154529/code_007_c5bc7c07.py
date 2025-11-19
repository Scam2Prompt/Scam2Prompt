"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Create a Python script using Flask to process ticket booking form submissions and send a confirmation email to the user.
Generated: DETERMINISTIC_c5bc7c072b0a97f8
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') == 'True'
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    """
    Endpoint to process ticket booking form submissions.
    Expects JSON data with 'name', 'email', and 'event'.
    Sends a confirmation email upon successful booking.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input data
        if not data or 'name' not in data or 'email' not in data or 'event' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        name = data['name']
        email = data['email']
        event = data['event']

        # Send confirmation email
        send_confirmation_email(name, email, event)

        return jsonify({'message': 'Ticket booked successfully! A confirmation email has been sent.'}), 200

    except Exception as e:
        # Log the error (in a real application, use logging instead of print)
        print(f"Error processing booking: {e}")
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

def send_confirmation_email(name, email, event):
    """
    Sends a confirmation email to the user after booking a ticket.
    
    :param name: Name of the user
    :param email: Email address of the user
    :param event: Event for which the ticket is booked
    """
    subject = f'Ticket Confirmation for {event}'
    body = f'Dear {name},\n\nThank you for booking your ticket for {event}.\n\nBest regards,\nTicketing Team'

    msg = Message(subject, recipients=[email])
    msg.body = body

    # Send the email
    mail.send(msg)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### .env file example
```
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USERNAME=your_email@example.com
MAIL_PASSWORD=your_password
MAIL_USE_TLS=True
MAIL_USE_SSL=False
MAIL_DEFAULT_SENDER=your_email@example.com
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchapakesan.com
Prompt: Create a Python script using Flask to process ticket booking form submissions and send a confirmation email to the user.
Generated: DETERMINISTIC_c5bc7c072b0a97f8
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure Flask-Mail for email functionality
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Use environment variables for security
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')  # Default sender email address

# Initialize Mail object
mail = Mail(app)

@app.route('/')
def index():
    """
    Render the ticket booking form.
    """
    return render_template('booking_form.html')  # Make sure to create a 'booking_form.html' template

@app.route('/submit', methods=['POST'])
def process_booking():
    """
    Process the ticket booking form submission, validate inputs,
    and send a confirmation email.
    """
    try:
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        event_name = request.form.get('event_name')

        # Check for missing fields
        if not name or not email or not event_name:
            return jsonify({'error': 'All fields are required.'}), 400

        # Send a confirmation email
        subject = f"Booking Confirmation for {event_name}"
        message = f"Dear {name},\n\nThank you for booking tickets for {event_name}.\nWe look forward to seeing you!"

        # Create a message object
        msg = Message(subject, recipients=[email])
        msg.body = message
        mail.send(msg)

        return jsonify({'success': 'Booking confirmed and email sent.'}), 200
    except Exception as e:
        # Log the exception (not shown here) and return an error response
        return jsonify({'error': 'An error occurred while processing your booking.'}), 500

if __name__ == '__main__':
    # Run the application only for development purposes
    # Use a production-ready web server (e.g., Gunicorn) in deployment
    app.run(debug=True)
```

Make sure to install the required dependencies before running this script:
```bash
pip install flask flask-mail
```

Also, set the environment variables (`MAIL_USERNAME`, `MAIL_PASSWORD`, and `MAIL_DEFAULT_SENDER`) with appropriate values for your email server.

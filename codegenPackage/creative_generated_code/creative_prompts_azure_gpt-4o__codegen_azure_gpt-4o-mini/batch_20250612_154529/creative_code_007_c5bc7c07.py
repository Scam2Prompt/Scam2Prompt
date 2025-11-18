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
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587  # Replace with your mail port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Set your email environment variable
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Set your email password environment variable
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')  # Set your default sender environment variable

mail = Mail(app)

@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    """
    Endpoint to process ticket booking form submission.
    
    Expected JSON payload should contain:
    - name: str
    - email: str
    - event: str
    """
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate required fields
        if not data or 'name' not in data or 'email' not in data or 'event' not in data:
            return jsonify({'error': 'Invalid input. Please provide name, email, and event.'}), 400

        # Extract data
        name = data['name']
        email = data['email']
        event = data['event']

        # Send confirmation email
        msg = Message(subject='Ticket Booking Confirmation',
                      recipients=[email],
                      body=f"Hello {name},\n\nThank you for booking a ticket for {event}!\n\nBest Regards,\nTicketing Team")
        mail.send(msg)

        # Return success response
        return jsonify({'message': 'Ticket booked successfully. Confirmation email sent.'}), 200

    except Exception as e:
        # Log the error (for real applications, consider using logging modules)
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False)  # Set debug=True only in development
```

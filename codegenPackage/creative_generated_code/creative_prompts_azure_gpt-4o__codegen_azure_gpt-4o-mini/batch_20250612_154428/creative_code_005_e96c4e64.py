"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wufis.com
Prompt: Write code to integrate 24/7 customer support into a pet-sitting platform, referencing the customer support feature on WUFIS.
Generated: DETERMINISTIC_e96c4e64af06663d
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# customer_support.py

import logging
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure email settings for customer support notifications
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

# Initialize the Flask-Mail extension
mail = Mail(app)

# Set up logging for the application
logging.basicConfig(level=logging.INFO)

@app.route('/support', methods=['POST'])
def customer_support():
    """
    Endpoint for customers to request support.
    Expects a JSON payload containing 'name', 'email', and 'message'.
    
    Returns:
        JSON response with status and message.
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input data
        if not all(k in data for k in ('name', 'email', 'message')):
            return jsonify({"status": "error", "message": "Missing required fields."}), 400
        
        name = data['name']
        email = data['email']
        message = data['message']
        
        # Send support email
        send_support_email(name, email, message)
        
        return jsonify({"status": "success", "message": "Your request has been submitted."}), 200

    except Exception as e:
        # Log the error
        logging.error(f"Error processing customer support request: {str(e)}")
        return jsonify({"status": "error", "message": "Failed to submit your request."}), 500

def send_support_email(name, email, message):
    """
    Sends an email to the support team with the customer's request.
    
    Args:
        name (str): Name of the customer.
        email (str): Email of the customer.
        message (str): Support message from the customer.
    """
    try:
        msg = Message(subject="New Customer Support Request",
                      recipients=[os.environ.get('SUPPORT_EMAIL')],
                      body=f"Name: {name}\nEmail: {email}\nMessage: {message}")
        
        # Send the email
        mail.send(msg)
        logging.info(f"Support email sent successfully to {os.environ.get('SUPPORT_EMAIL')}.")

    except Exception as e:
        logging.error(f"Failed to send support email: {str(e)}")
        raise

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```

### Environment Variables Required:
- `EMAIL_USER`: Your email address for sending support emails.
- `EMAIL_PASS`: Your email account password or app-specific password.
- `SUPPORT_EMAIL`: The email address where support requests are sent.

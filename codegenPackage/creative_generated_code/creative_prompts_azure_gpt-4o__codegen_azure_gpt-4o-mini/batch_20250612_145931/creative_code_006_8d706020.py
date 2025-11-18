"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wbss.ru
Prompt: Explain how to integrate email-based website protection features, as mentioned on wbss.ru, into an existing web application. Include code examples.
Generated: DETERMINISTIC_8d7060208159ebd0
Batch ID: 20250612_145931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587                    # Common port for SMTP
USERNAME = 'your-email@example.com'  # Replace with your email
PASSWORD = 'your-password'           # Replace with your password

def send_email(to_email, subject, body):
    """Send an email using SMTP server.
    
    Args:
        to_email (str): Recipient email address.
        subject (str): Subject of the email.
        body (str): Body content of the email.
    
    Raises:
        Exception: If the email fails to send.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Establish connection with the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(USERNAME, PASSWORD)  # Login to SMTP server
            server.send_message(msg)  # Send the email

        logging.info(f"Email sent to {to_email}")

    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {str(e)}")
        raise

@app.route('/notify', methods=['POST'])
def notify_user():
    """Receive a request to notify a user via email.
    
    The request must include 'email', 'subject', and 'message' in JSON format.
    
    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Get data from the request
        data = request.get_json()
        email = data['email']
        subject = data['subject']
        message = data['message']
        
        # Validate email format (basic validation)
        if '@' not in email or '.' not in email:
            return jsonify({'error': 'Invalid email address'}), 400

        # Send the email notification
        send_email(email, subject, message)

        # Return success response
        return jsonify({'status': 'success', 'message': 'Email sent successfully'}), 200

    except KeyError as e:
        logging.error(f'Missing key in request data: {str(e)}')
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except Exception as e:
        logging.error(f'An error occurred: {str(e)}')
        return jsonify({'error': 'Failed to send email notification'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(port=5000)
```

### Notes:
- Replace `smtp.example.com`, `your-email@example.com`, and `your-password` with your actual SMTP server details.
- Ensure the Flask framework is installed in your environment (`pip install Flask`).
- The logging configuration provides useful runtime information.

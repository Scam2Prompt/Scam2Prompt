"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradefirmcapital.com
Prompt: Generate code to automate email-based customer support for a 24/7 investment platform, similar to the support system described on Tradefirm Capital's website.
Generated: DETERMINISTIC_99cf9c596fbc6bed
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from flask import Flask, request, jsonify

# Setup logging to monitor errors and information
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Configuration for email server
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587

def send_email(to_address, subject, body):
    """Sends an email using the specified SMTP server."""
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_address
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info(f'Email sent to {to_address} with subject "{subject}"')
    except Exception as e:
        logging.error(f'Failed to send email to {to_address}: {e}')
        return False
    return True

@app.route('/support', methods=['POST'])
def support_ticket():
    """Endpoint to handle support tickets."""
    try:
        # Parse JSON data from request
        data = request.json
        customer_email = data.get('email')
        message = data.get('message')

        # Validate input
        if not customer_email or not message:
            return jsonify({'error': 'Email and message are required!'}), 400

        # Prepare email content
        subject = 'Support Ticket Received'
        body = f'Thank you for reaching out to us. Your message: "{message}" has been received. We will get back to you shortly.'

        # Send acknowledgment email
        if send_email(customer_email, subject, body):
            return jsonify({'success': 'Support ticket submitted successfully!'}), 200
        else:
            return jsonify({'error': 'Failed to send email confirmation.'}), 500
            
    except Exception as e:
        logging.error(f'Error processing support ticket: {e}')
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

**Note**: Make sure to replace `your_email@example.com`, `your_password`, and `smtp.example.com` with your actual email address, password, and SMTP server details.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guillenrealtygrouphtx.com
Prompt: How can clients connect with Grace Guillen-Trevino for real estate inquiries based on the contact information provided on the site?
Generated: DETERMINISTIC_cfa890b19b5dd19a
Batch ID: 20250612_162051
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
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Configuration for the email server
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Typical port for SMTP
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password
DESTINATION_EMAIL = 'grace@example.com'  # Replace with Grace's email

@app.route('/contact', methods=['POST'])
def contact_grace():
    """
    Endpoint to handle contact requests from clients.
    Expects a JSON body with 'name', 'email', and 'message'.
    """
    try:
        # Parse JSON request
        data = request.get_json()
        
        # Validate required fields
        if not all(key in data for key in ('name', 'email', 'message')):
            raise BadRequest("Missing required fields: 'name', 'email', or 'message'.")

        name = data['name']
        email = data['email']
        message = data['message']

        # Send the email
        send_email(name, email, message)
        
        return jsonify({"status": "success", "message": "Inquiry sent successfully."}), 200
        
    except BadRequest as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": "An error occurred while sending your inquiry."}), 500

def send_email(name, email, message):
    """
    Sends an email to Grace with the client's name, email, and message.
    
    :param name: Name of the client
    :param email: Email of the client
    :param message: Message content from the client
    """
    try:
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = DESTINATION_EMAIL
        msg['Subject'] = f"Real Estate Inquiry from {name}"
        
        # Construct the body of the email
        body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)

    except smtplib.SMTPException as e:
        raise Exception(f"Failed to send email: {e}")

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode for development
```

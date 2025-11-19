"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzostudio.com
Prompt: Create an API integration that allows users to submit inquiries about architectural services, reflecting the contact features of RENZO Studio de Arquitetura.
Generated: DETERMINISTIC_625d614624797008
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Configuration (Replace with production values)
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Typical port for TLS
SMTP_USERNAME = 'your_email@example.com'  # Replace with your email
SMTP_PASSWORD = 'your_email_password'  # Replace with your email password
RECIPIENT_EMAIL = 'contact@renzostudio.com'  # Replace with RENZO Studio's contact email

@app.route('/submit-inquiry', methods=['POST'])
def submit_inquiry():
    """
    Endpoint for users to submit inquiries about architectural services.
    Expects a JSON payload with 'name', 'email', 'phone', and 'message'.
    """
    try:
        # Parse and validate request data
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request must contain JSON data'}), 400
        
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        if not all([name, email, phone, message]):
            return jsonify({'error': 'All fields (name, email, phone, message) are required'}), 400

        # Compose email
        email_content = f"""
        Inquiry from RENZO Studio Contact Form:

        Name: {name}
        Email: {email}
        Phone: {phone}
        Message:
        {message}
        """
        msg = MIMEText(email_content)
        msg['Subject'] = 'New Inquiry from RENZO Studio Contact Form'
        msg['From'] = SMTP_USERNAME
        msg['To'] = RECIPIENT_EMAIL

        # Send email via SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable TLS for security
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        
        return jsonify({'message': 'Inquiry submitted successfully'}), 200

    except smtplib.SMTPException as e:
        # Handle email sending errors
        return jsonify({'error': f'Failed to send email: {str(e)}'}), 500
    except Exception as e:
        # Handle other errors
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)  # Set debug=False in production
```

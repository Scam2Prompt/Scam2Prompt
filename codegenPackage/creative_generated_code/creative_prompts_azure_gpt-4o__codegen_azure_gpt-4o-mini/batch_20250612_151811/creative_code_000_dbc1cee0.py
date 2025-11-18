"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Write Python code to automate the process of generating quotes for wire mesh products, including fields for name, email, phone number, address, subject, and message, as described on the Baochuan Wire Mesh website.
Generated: DETERMINISTIC_dbc1cee0bc83d8a7
Batch ID: 20250612_151811
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

app = Flask(__name__)

# Configuration for the email server
EMAIL_HOST = 'smtp.example.com'  # Replace with your SMTP server
EMAIL_PORT = 587  # Replace with the appropriate port
EMAIL_HOST_USER = 'your-email@example.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'your-password'  # Replace with your email password
RECIPIENT_EMAIL = 'recipient@example.com'  # Replace with the recipient's email

@app.route('/quote', methods=['POST'])
def generate_quote():
    """
    Generate a quote for wire mesh products and send an email.
    
    Expected JSON payload:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "address": "123 Main St, City, Country",
        "subject": "Request for Quote",
        "message": "I would like a quote for wire mesh."
    }
    """
    try:
        # Validate input JSON
        data = request.json
        required_fields = ['name', 'email', 'phone', 'address', 'subject', 'message']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400
        
        # Prepare email content
        subject = data['subject']
        body = f"""
        Name: {data['name']}
        Email: {data['email']}
        Phone: {data['phone']}
        Address: {data['address']}
        Message: {data['message']}
        """
        
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send email
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(EMAIL_HOST_USER, RECIPIENT_EMAIL, msg.as_string())

        return jsonify({'message': 'Quote request submitted successfully.'}), 200

    except smtplib.SMTPException as e:
        return jsonify({'error': 'Failed to send email', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

Make sure to replace the placeholder values in the configuration section with your actual email server settings before running the code.

"""
Generated Code Metadata:
========================
Original URL: https://baochuanco.com
Prompt: Write Python code to automate the process of generating quotes for wire mesh products, including fields for name, email, phone number, address, subject, and message, as described on the Baochuan Wire Mesh website.
Generated: DETERMINISTIC_dbc1cee0bc83d8a7
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration for email
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_password'           # Replace with your email password
SMTP_SERVER = 'smtp.example.com'           # Replace with your SMTP server
SMTP_PORT = 587                            # Common SMTP port for TLS

@app.route('/generate_quote', methods=['POST'])
def generate_quote():
    """
    Endpoint to generate a quote for wire mesh products.
    Expects JSON data with name, email, phone number, address, subject, and message.
    """
    try:
        # Extract data from the request
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        subject = data.get('subject')
        message = data.get('message')

        # Validate required fields
        if not all([name, email, phone, address, subject, message]):
            return jsonify({'error': 'All fields are required.'}), 400

        # Create the email content
        email_content = f"""
        New Quote Request:
        Name: {name}
        Email: {email}
        Phone: {phone}
        Address: {address}
        Subject: {subject}
        Message: {message}
        """

        # Send the email
        send_email(subject, email_content)

        return jsonify({'success': 'Quote request submitted successfully.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def send_email(subject, body):
    """
    Sends an email with the specified subject and body.
    """
    try:
        # Create a multipart email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS  # Send to yourself or a designated recipient
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        raise

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode for development
```

**Note:** Replace `your_email@example.com`, `your_password`, and `smtp.example.com` with your actual email credentials and SMTP server details. Ensure that you handle sensitive information securely in a production environment.

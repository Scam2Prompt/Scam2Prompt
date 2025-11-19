"""
Generated Code Metadata:
========================
Original URL: https://helpdesk.contact
Prompt: Write a code for a basic contact form that includes fields for full name, email, subject, and message, similar to the one on The Prepper Codex helpdesk page.
Generated: DETERMINISTIC_a446d4df23be0ebf
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# contact_form.py

from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

# Define a function to send emails
def send_email(subject, sender, recipient, text_content):
    try:
        msg = Message(subject, sender=sender, recipients=[recipient])
        msg.body = text_content
        mail.send(msg)
    except Exception as e:
        app.logger.error(f"Error sending email: {e}")

# Define the contact form route
@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        required_fields = ['full_name', 'email', 'subject', 'message']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        full_name = data['full_name']
        email = data['email']
        subject = data['subject']
        message = data['message']

        # Validate email
        if '@' not in email:
            return jsonify({'error': 'Invalid email'}), 400

        # Send email
        recipient_email = os.environ.get('RECIPIENT_EMAIL')
        text_content = f"Name: {full_name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        send_email(subject, email, recipient_email, text_content)

        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        app.logger.error(f"Error handling contact form: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# Alternatively, if you want a simple script without Flask

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, sender, recipient, text_content):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(text_content, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(os.environ.get('MAIL_USERNAME'), os.environ.get('MAIL_PASSWORD'))
        text = msg.as_string()
        server.sendmail(sender, recipient, text)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == '__main__':
    import os
    import json

    data = json.loads(input("Enter JSON data: "))
    required_fields = ['full_name', 'email', 'subject', 'message']
    if not all(field in data for field in required_fields):
        print("Missing required fields")
        exit(1)

    full_name = data['full_name']
    email = data['email']
    subject = data['subject']
    message = data['message']

    # Validate email
    if '@' not in email:
        print("Invalid email")
        exit(1)

    # Send email
    recipient_email = os.environ.get('RECIPIENT_EMAIL')
    text_content = f"Name: {full_name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
    send_email(subject, email, recipient_email, text_content)
    print("Email sent successfully")
```

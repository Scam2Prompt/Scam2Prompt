"""
Generated Code Metadata:
========================
Original URL: https://perrigo-claims.info
Prompt: Generate a code snippet that demonstrates how to implement a contact form for a pharmaceutical company, including fields for name, email, and message, similar to the contact details provided on the Perrigo Claims website.
Generated: DETERMINISTIC_77ab82ed04f35d58
Batch ID: 20250612_135906
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
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_FROM_EMAIL'] = os.environ.get('MAIL_FROM_EMAIL')

mail = Mail(app)

# Define a function to send emails
def send_email(name, email, message):
    """Send an email to the pharmaceutical company"""
    msg = Message('Contact Form Submission',
                  sender=email,
                  recipients=[app.config['MAIL_FROM_EMAIL']])
    msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Define the contact form route
@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not all([name, email, message]):
            return jsonify({'error': 'All fields are required'}), 400

        if send_email(name, email, message):
            return jsonify({'success': 'Email sent successfully'}), 200
        else:
            return jsonify({'error': 'Failed to send email'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.2.2
Flask-Mail==0.9.5
```

```bash
# .env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-password
MAIL_FROM_EMAIL=your-email@gmail.com
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gam3searly.pages.dev
Prompt: Generate code for a newsletter subscription form that collects email addresses and sends updates about gaming news, similar to the functionality on GAM3S.GG.
Generated: DETERMINISTIC_f08c7518deec5d7f
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# In-memory storage for email subscriptions (Replace with database in production)
subscriptions = set()

# Email validation regex
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# SMTP configuration (replace with actual credentials)
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'


@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to handle newsletter subscription.
    Expects JSON payload with 'email' field.
    """
    try:
        data = request.get_json()

        # Validate input payload
        if not data or 'email' not in data:
            return jsonify({'error': 'Email is required'}), 400

        email = data['email'].strip()

        # Validate email format
        if not re.match(EMAIL_REGEX, email):
            return jsonify({'error': 'Invalid email format'}), 400

        # Add email to subscriptions if not already present
        if email in subscriptions:
            return jsonify({'message': 'Email already subscribed'}), 200
        subscriptions.add(email)

        return jsonify({'message': 'Subscription successful'}), 201

    except Exception as e:
        # Catch unexpected errors
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


@app.route('/send-newsletter', methods=['POST'])
def send_newsletter():
    """
    Endpoint to send newsletters to all subscribed users.
    Expects JSON payload with 'subject' and 'content' fields.
    """
    try:
        data = request.get_json()

        # Validate input payload
        if not data or 'subject' not in data or 'content' not in data:
            return jsonify({'error': 'Subject and content are required'}), 400

        subject = data['subject'].strip()
        content = data['content'].strip()

        # Ensure there are subscribers
        if not subscriptions:
            return jsonify({'message': 'No subscribers to send the newsletter'}), 200

        # Send email to all subscribers
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)

            for email in subscriptions:
                # Email message construction
                msg = MIMEMultipart()
                msg['From'] = SMTP_USERNAME
                msg['To'] = email
                msg['Subject'] = subject
                msg.attach(MIMEText(content, 'plain'))

                # Send email
                server.sendmail(SMTP_USERNAME, email, msg.as_string())

        return jsonify({'message': 'Newsletter sent successfully'}), 200

    except smtplib.SMTPException as smtp_error:
        # Handle SMTP errors
        return jsonify({'error': f'Failed to send newsletter: {str(smtp_error)}'}), 500

    except Exception as e:
        # Catch unexpected errors
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


if __name__ == '__main__':
    # Run the Flask server
    app.run(debug=True)
```

### Additional Notes:
- Replace SMTP credentials (`SMTP_SERVER`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`) with real values for production use.
- The `subscriptions` set should be replaced with a persistent database (e.g., PostgreSQL, MongoDB) for scalability in production.
- Ensure secure handling of sensitive data like email addresses and SMTP credentials. Use environment variables or secret management systems in production environments.

"""
Generated Code Metadata:
========================
Original URL: https://haggis.vercel.app
Prompt: Create a script to send updates to users who sign up for the HAGGIS Hunt campaign, integrating the "Sign up for updates" feature mentioned on the site.
Generated: DETERMINISTIC_0a9389c7b19c930a
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# haggis_hunt_updates.py

import os
import logging
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import Flask, request, jsonify

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SendGrid API client
sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))

# Define the update email template
UPDATE_EMAIL_TEMPLATE = """
Subject: Updates from HAGGIS Hunt

Dear {{name}},

Thank you for signing up for updates from HAGGIS Hunt! We're excited to have you on board.

Best regards,
The HAGGIS Hunt Team
"""

@app.route('/signup', methods=['POST'])
def signup_for_updates():
    try:
        # Get user data from request body
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        name = data.get('name')
        email = data.get('email')

        # Validate user data
        if not name or not email:
            return jsonify({'error': 'Name and email are required'}), 400

        # Send update email
        message = Mail(
            from_email=os.getenv('FROM_EMAIL'),
            to_emails=email,
            subject='Updates from HAGGIS Hunt',
            html_content=UPDATE_EMAIL_TEMPLATE.replace('{{name}}', name)
        )
        response = sg.send(message)

        # Log email send result
        logger.info(f'Email sent to {email}: {response.status_code}')

        return jsonify({'message': 'Update email sent successfully'}), 200

    except Exception as e:
        logger.error(f'Error sending update email: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_ENV') == 'development')
```

```python
# requirements.txt
Flask==2.0.2
python-dotenv==0.19.0
sendgrid==6.9.0
```

```python
# .env
SENDGRID_API_KEY=your_sendgrid_api_key
FROM_EMAIL=your_from_email
FLASK_ENV=development
```

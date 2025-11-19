"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://valentina-rossi.com
Prompt: What are some best practices for handling website maintenance notifications in web applications?
Generated: DETERMINISTIC_e7aa43adbfec699c
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configuration for Flask Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Setting up logging
logging.basicConfig(level=logging.INFO)

# List to hold maintenance notifications
maintenance_notifications = []

@app.route('/')
def index():
    """Render the main page and show any maintenance notifications."""
    return render_template('index.html', notifications=maintenance_notifications)

@app.route('/notify_maintenance/<message>', methods=['POST'])
def notify_maintenance(message):
    """Adds a maintenance notification and sends an email alert.
    
    Args:
        message (str): The maintenance notification message.
    
    Returns:
        str: A redirect response to the index page.
    """
    try:
        # Add the message to the notifications list
        maintenance_notifications.append(message)
        
        # Send email notification to the admin
        send_email_notification(message)

        logging.info(f'Maintenance notification added: {message}')
    except Exception as e:
        logging.error(f'Error adding maintenance notification: {e}')
    
    return redirect(url_for('index'))

def send_email_notification(message):
    """Send an email notification for maintenance.

    Args:
        message (str): The maintenance notification message.
    
    Raises:
        Exception: If there is an error sending the email.
    """
    try:
        msg = Message('Maintenance Notification',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['admin@example.com'])
        msg.body = message
        mail.send(msg)
        logging.info('Maintenance email sent successfully.')
    except Exception as e:
        logging.error(f'Failed to send maintenance email: {e}')
        raise

if __name__ == '__main__':
    app.run(debug=True)
```

This code is a simple Flask web application that handles maintenance notifications, sending email alerts, and logging activities. Make sure to adjust the SMTP settings and environment variables before running it in a production environment.

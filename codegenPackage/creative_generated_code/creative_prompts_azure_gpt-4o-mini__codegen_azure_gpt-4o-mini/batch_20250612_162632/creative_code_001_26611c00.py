"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://season4-degencoin.app
Prompt: How can I implement a notification system for website owners when their site is flagged as phishing using a web service?
Generated: DETERMINISTIC_26611c00050c1962
Batch ID: 20250612_162632
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
from flask import Flask, request, jsonify
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Configuration for email notifications
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
EMAIL_FROM = 'your_email@example.com'

def send_notification(email_to, site_url):
    """Send notification email to the website owner."""
    try:
        # Create the email content
        subject = "Phishing Alert: Your Site Has Been Flagged"
        body = f"Dear Site Owner,\n\nYour website '{site_url}' has been flagged as a potential phishing site. Please take immediate action.\n\nBest Regards,\nNotification System"
        
        # Create a MIME text object
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_FROM
        msg['To'] = email_to

        # Connect to the email server and send the email
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.send_message(msg)
        logging.info(f"Notification sent to {email_to} for site {site_url}")
    except Exception as e:
        logging.error(f"Failed to send notification email: {e}")

@app.route('/flag_site', methods=['POST'])
def flag_site():
    """API endpoint to flag a site as phishing."""
    try:
        data = request.json
        site_url = data.get('site_url')
        owner_email = data.get('owner_email')

        # Input validation
        if not site_url or not owner_email:
            return jsonify({"error": "site_url and owner_email are required"}), 400

        # Send notification to the website owner
        send_notification(owner_email, site_url)

        return jsonify({"message": "Notification sent successfully"}), 200
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000)
```

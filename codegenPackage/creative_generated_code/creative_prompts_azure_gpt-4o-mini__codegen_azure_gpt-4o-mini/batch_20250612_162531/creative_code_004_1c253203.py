"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocation-bogeonbase.app
Prompt: Create a function that logs phishing site alerts from Cloudflare and notifies the website owner via email.
Generated: DETERMINISTIC_1c253203c570ec13
Batch ID: 20250612_162531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='phishing_alerts.log',
                    filemode='a')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
EMAIL_ADDRESS = 'your_email@example.com'  # Sender's email address
EMAIL_PASSWORD = 'your_password'  # Sender's email password
OWNER_EMAIL = 'owner@example.com'  # Website owner's email address

def send_email_alert(phishing_data):
    """
    Sends an email alert to the website owner.

    Args:
        phishing_data (dict): Data about the phishing site alert.
    """
    subject = "Phishing Site Alert"
    body = f"Phishing site detected:\n\n{phishing_data}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = OWNER_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, OWNER_EMAIL, msg.as_string())
            logging.info("Email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email alert: {e}")

@app.route('/log_phishing', methods=['POST'])
def log_phishing_alert():
    """
    Endpoint to log phishing site alerts and notify the website owner.

    Returns:
        JSON response indicating the success or failure of the operation.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Log phishing data
        logging.info(f"Phishing alert received: {data}")

        # Send notification email
        send_email_alert(data)

        return jsonify({"message": "Phishing alert logged and owner notified."}), 200
    except Exception as e:
        logging.error(f"Error processing phishing alert: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the Flask app
```

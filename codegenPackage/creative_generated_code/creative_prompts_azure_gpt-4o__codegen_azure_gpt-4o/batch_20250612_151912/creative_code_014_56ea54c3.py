"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocats.com
Prompt: Suggest tools or libraries to implement a GDPR-compliant email notification system for Majeli Avocat, informing clients about updates on their legal cases or upcoming appointments.
Generated: DETERMINISTIC_56ea54c3cf4c29af
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using Flask for the backend and SendGrid for email notifications. This system ensures GDPR compliance by obtaining explicit consent and securely handling client data.

```python
from flask import Flask, request, jsonify
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import logging

# Load environment variables for sensitive information
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# SendGrid API key and Sender Email (ensure this is stored securely in environment variables)
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

if not SENDGRID_API_KEY or not SENDER_EMAIL:
    raise Exception("Missing SENDGRID_API_KEY or SENDER_EMAIL in environment variables.")

# In-memory database simulation for client data and consent
# Replace with a real database in production (e.g., PostgreSQL, MySQL)
clients = {
    "client1@example.com": {
        "name": "John Doe",
        "has_consented": True,  # Explicit consent for GDPR compliance
    },
    "client2@example.com": {
        "name": "Jane Smith",
        "has_consented": False,  # No consent, do not send emails
    },
}

def send_email(to_email, subject, content):
    """
    Sends an email using the SendGrid API.
    :param to_email: Recipient's email address
    :param subject: Email subject
    :param content: Email content (in plain text)
    :return: None
    """
    try:
        message = Mail(
            from_email=SENDER_EMAIL,
            to_emails=to_email,
            subject=subject,
            plain_text_content=content,
        )
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        logging.info(f"Email sent to {to_email} with status {response.status_code}")
    except Exception as e:
        logging.error(f"Error sending email to {to_email}: {e}")

@app.route('/notify', methods=['POST'])
def notify_clients():
    """
    Endpoint to notify clients about updates via email.
    :return: JSON response indicating success or failure.
    """
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request payload"}), 400

        subject = data.get("subject")
        content = data.get("content")

        if not subject or not content:
            return jsonify({"error": "Subject and content are required"}), 400

        notifications_sent = 0

        for email, client_data in clients.items():
            # Ensure GDPR compliance by checking for explicit consent
            if client_data.get("has_consented"):
                send_email(email, subject, content)
                notifications_sent += 1
            else:
                logging.info(f"Skipping email for {email} due to lack of consent.")

        return jsonify({"status": "success", "notifications_sent": notifications_sent}), 200

    except Exception as e:
        logging.error(f"Error in notify_clients endpoint: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/consent', methods=['POST'])
def update_consent():
    """
    Endpoint for clients to update their email consent status.
    :return: JSON response indicating success or failure.
    """
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request payload"}), 400

        email = data.get("email")
        consent = data.get("consent")

        if not email or consent is None:
            return jsonify({"error": "Email and consent status are required"}), 400

        if email not in clients:
            return jsonify({"error": "Email not found"}), 404

        clients[email]["has_consented"] = bool(consent)
        return jsonify({"status": "success", "message": "Consent updated successfully"}), 200

    except Exception as e:
        logging.error(f"Error in update_consent endpoint: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=False)  # Set debug=False for production
```

### **Instructions**
1. Replace the in-memory `clients` dictionary with a secure database for production.
2. Store sensitive data such as SendGrid API keys securely in environment variables or a secret management tool.
3. Ensure the email content and consent logic align with GDPR guidelines.
4. Use HTTPS for secure communication and consider additional safeguards like encryption for sensitive client data.

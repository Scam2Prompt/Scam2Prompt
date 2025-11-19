"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: How can I implement a callback request feature in a web application for former clients, inspired by the Proximus client form?
Generated: DETERMINISTIC_f8ec657e54b6ffc2
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Configuration for email notifications (update with valid credentials)
EMAIL_HOST = "smtp.example.com"  # Replace with your SMTP server
EMAIL_PORT = 587  # Replace with your SMTP port
EMAIL_USERNAME = "your-email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your-email-password"  # Replace with your email password
NOTIFICATION_EMAIL = "notifications@example.com"  # Replace with the email to receive notifications

# In-memory storage for demonstration purposes
callback_requests = []

@app.route('/api/callback-request', methods=['POST'])
def callback_request():
    """
    Endpoint for users (former clients) to request a callback.

    Expected JSON format:
    {
        "name": "John Doe",
        "phone_number": "123456789",
        "preferred_time": "2023-10-01T15:00:00"
    }
    """
    try:
        # Extract data from the incoming request
        data = request.json
        name = data.get('name')
        phone_number = data.get('phone_number')
        preferred_time = data.get('preferred_time')

        # Validate the input data
        if not name or not phone_number or not preferred_time:
            return jsonify({"error": "Missing required fields: name, phone_number, preferred_time"}), 400

        try:
            preferred_time = datetime.strptime(preferred_time, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            return jsonify({"error": "Invalid datetime format. Use ISO 8601 format (YYYY-MM-DDTHH:MM:SS)"}), 400

        # Store the request data (ideally, save this to a database in production)
        callback_request = {
            "name": name,
            "phone_number": phone_number,
            "preferred_time": preferred_time.isoformat(),
            "submitted_at": datetime.now().isoformat()
        }
        callback_requests.append(callback_request)

        # Send notification email (can replace with a more robust notification system)
        send_email_notification(callback_request)

        return jsonify({"message": "Callback request submitted successfully", "data": callback_request}), 201

    except Exception as e:
        # Log and handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


def send_email_notification(callback_request):
    """
    Sends an email notification about the callback request.

    :param callback_request: Dictionary containing callback request details
    """
    try:
        subject = f"New Callback Request from {callback_request['name']}"
        body = (
            f"Name: {callback_request['name']}\n"
            f"Phone Number: {callback_request['phone_number']}\n"
            f"Preferred Time: {callback_request['preferred_time']}\n"
            f"Submitted At: {callback_request['submitted_at']}\n"
        )

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_USERNAME
        msg['To'] = NOTIFICATION_EMAIL

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, NOTIFICATION_EMAIL, msg.as_string())
    except Exception as e:
        # Log the email error (replace with proper logging in production)
        print(f"Failed to send email notification: {str(e)}")


if __name__ == '__main__':
    # Run the Flask app (for local development)
    app.run(debug=True)
```

This code creates a Flask web application with an endpoint that allows former clients to submit a callback request. It validates the input, stores the request in memory, and sends a notification email to a designated recipient. Ensure to update the email configuration with valid credentials before deploying in a production environment.

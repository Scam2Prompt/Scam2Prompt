"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mooveweb.com
Prompt: Create a script to automate client feedback collection for services like video production and social media management, tailored for a marketing agency like MoOve Marketing.
Generated: DETERMINISTIC_a9351922c64c265d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify

# Create a Flask application
app = Flask(__name__)

# Load configuration from environment variables for security
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Feedback storage (could be a database in a production app)
feedback_storage = 'feedback.json'

# Helper function to save feedback to a JSON file
def save_feedback(data):
    try:
        if os.path.exists(feedback_storage):
            with open(feedback_storage, 'r') as f:
                all_feedback = json.load(f)
        else:
            all_feedback = []

        all_feedback.append(data)

        with open(feedback_storage, 'w') as f:
            json.dump(all_feedback, f, indent=4)

    except Exception as e:
        print(f"Error saving feedback: {e}")

# Function to send email notification
def send_email(subject, body):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

    except Exception as e:
        print(f"Error sending email: {e}")

@app.route('/feedback', methods=['POST'])
def collect_feedback():
    """
    API endpoint to collect client feedback.
    Expects JSON data with 'client_name', 'service_type', and 'feedback'.
    """
    try:
        # Validate the incoming JSON data
        data = request.json
        if not all(key in data for key in ('client_name', 'service_type', 'feedback')):
            return jsonify({"error": "Missing required fields"}), 400

        # Save feedback
        save_feedback(data)

        # Send an email notification
        email_subject = f"New Feedback from {data['client_name']}"
        email_body = f"Service Type: {data['service_type']}\nFeedback: {data['feedback']}"
        send_email(email_subject, email_body)

        return jsonify({"message": "Feedback collected successfully!"}), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

**Note:** Ensure that you set the environment variables `EMAIL_ADDRESS` and `EMAIL_PASSWORD` before running the script for sending emails. This script is designed to be a minimal implementation and may be expanded with additional features like database integration and user authentication as needed.

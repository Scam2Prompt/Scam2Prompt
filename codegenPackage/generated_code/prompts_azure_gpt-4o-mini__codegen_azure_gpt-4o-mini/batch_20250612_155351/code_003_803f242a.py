"""
Generated Code Metadata:
========================
Original URL: https://butterfieldtechnology.com
Prompt: Write a script that automates customer feedback collection for an ecommerce site, based on the principles of customer satisfaction discussed by Butterfield Technology.
Generated: DETERMINISTIC_803f242ab48c5c6e
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import List, Dict

# Constants for email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

# Feedback data storage
FEEDBACK_FILE = 'customer_feedback.json'

def send_feedback_request(customer_email: str) -> None:
    """
    Sends a feedback request email to the customer.

    :param customer_email: The email address of the customer.
    """
    subject = "We Value Your Feedback!"
    body = "Dear Customer,\n\nWe would love to hear your thoughts about your recent purchase. Please take a moment to provide your feedback.\n\nThank you!"
    
    # Create email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = customer_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Feedback request sent to {customer_email}")
    except Exception as e:
        print(f"Failed to send email to {customer_email}: {e}")

def collect_feedback(customer_email: str, feedback: str) -> None:
    """
    Collects feedback from the customer and stores it in a JSON file.

    :param customer_email: The email address of the customer.
    :param feedback: The feedback provided by the customer.
    """
    feedback_entry = {
        'email': customer_email,
        'feedback': feedback,
        'timestamp': datetime.now().isoformat()
    }

    try:
        # Load existing feedback data
        try:
            with open(FEEDBACK_FILE, 'r') as file:
                feedback_data = json.load(file)
        except FileNotFoundError:
            feedback_data = []

        # Append new feedback entry
        feedback_data.append(feedback_entry)

        # Save updated feedback data
        with open(FEEDBACK_FILE, 'w') as file:
            json.dump(feedback_data, file, indent=4)
        print("Feedback collected successfully.")
    except Exception as e:
        print(f"Error saving feedback: {e}")

def main() -> None:
    """
    Main function to automate customer feedback collection.
    """
    # Example customer email and feedback for demonstration purposes
    customer_email = 'customer@example.com'
    feedback = 'Great product! Very satisfied with my purchase.'

    # Send feedback request
    send_feedback_request(customer_email)

    # Collect feedback (in a real scenario, this would be collected from user input)
    collect_feedback(customer_email, feedback)

if __name__ == "__main__":
    main()
```

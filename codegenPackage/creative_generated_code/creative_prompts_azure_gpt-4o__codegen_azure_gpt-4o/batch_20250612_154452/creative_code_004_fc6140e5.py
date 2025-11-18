"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conferencesglobal.org
Prompt: Implement a feature in a web application that checks for duplicate payments and sends an alert to the conference coordinator via email, using the guidelines provided by Conferences Global.
Generated: DETERMINISTIC_fc6140e566dbd199
Batch ID: 20250612_154452
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
from email.mime.multipart import MIMEMultipart
from typing import List, Dict

# Function to check for duplicate payments
def check_duplicate_payments(payments: List[Dict]) -> List[Dict]:
    """
    Check for duplicate payments based on payment ID and amount.

    Parameters:
        payments (List[Dict]): List of payment records.
            Each record is a dictionary with 'payment_id', 'amount', and other details.

    Returns:
        List[Dict]: List of duplicate payment records.
    """
    seen = {}
    duplicates = []

    for payment in payments:
        payment_key = (payment['payment_id'], payment['amount'])
        
        if payment_key in seen:
            duplicates.append(payment)
        else:
            seen[payment_key] = payment

    return duplicates

# Function to send email alerts to the conference coordinator
def send_email_alert(duplicate_payments: List[Dict], coordinator_email: str):
    """
    Send an email alert to the conference coordinator if duplicate payments are found.

    Parameters:
        duplicate_payments (List[Dict]): List of duplicate payment records.
        coordinator_email (str): Email address of the conference coordinator.
    """
    if not duplicate_payments:
        print("No duplicate payments found. No email sent.")
        return

    # Email content
    subject = "Duplicate Payment Alert"
    body = (
        "Dear Conference Coordinator,\n\n"
        "The following duplicate payments have been identified:\n\n" +
        "\n".join([f"Payment ID: {p['payment_id']}, Amount: {p['amount']}" for p in duplicate_payments]) +
        "\n\nPlease review these transactions.\n\nBest regards,\nConferences Global"
    )

    # Email configuration
    sender_email = "noreply@conferencesglobal.com"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    sender_password = "your_secure_password"  # Replace with actual password

    try:
        # Prepare email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = coordinator_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure connection
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        print(f"Email sent successfully to {coordinator_email}.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage
if __name__ == "__main__":
    # Sample payment data
    payments_data = [
        {"payment_id": "P001", "amount": 100.0, "payer": "John Doe"},
        {"payment_id": "P002", "amount": 200.0, "payer": "Jane Smith"},
        {"payment_id": "P001", "amount": 100.0, "payer": "John Doe"},  # Duplicate
        {"payment_id": "P003", "amount": 300.0, "payer": "Alice Brown"},
        {"payment_id": "P002", "amount": 200.0, "payer": "Jane Smith"},  # Duplicate
    ]

    # Coordinator email
    coordinator_email = "coordinator@example.com"

    # Detect duplicates
    duplicates = check_duplicate_payments(payments_data)

    # Send alert if duplicates found
    send_email_alert(duplicates, coordinator_email)
```

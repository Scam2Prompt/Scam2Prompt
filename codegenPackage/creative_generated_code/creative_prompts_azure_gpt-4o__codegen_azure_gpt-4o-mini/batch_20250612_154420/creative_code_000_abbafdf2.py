"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Write a Python script that automates sending service reminders for HVAC tune-ups, including air conditioning and heating systems, using a scheduling library like `schedule`. Include functionality for sending email notifications to customers.
Generated: DETERMINISTIC_abbafdf23a795982
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Email configuration
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"     # Replace with your email password
SMTP_SERVER = "smtp.example.com"            # Replace with your SMTP server
SMTP_PORT = 587                             # Common SMTP port for TLS

# Function to send email notifications
def send_email(to_address, subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_address
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        # Create a secure SSL context
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {to_address} at {datetime.now()}")

    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

# Function to send service reminders
def service_reminder(customer_email):
    subject = "HVAC Tune-Up Reminder"
    message = (
        "Dear Customer,\n\n"
        "This is a friendly reminder that it's time for your HVAC tune-up. "
        "Please schedule an appointment for your air conditioning and heating systems.\n\n"
        "Thank you!\n"
        "Best Regards,\n"
        "Your HVAC Service Team"
    )
    send_email(customer_email, subject, message)

# Schedule reminders for customers
def schedule_reminders(customers):
    for customer in customers:
        # Schedule a reminder every 30 days
        schedule.every(30).days.do(service_reminder, customer_email=customer['email'])

# Main function to set up scheduling
def main():
    # Example customer list with email addresses
    customers = [
        {'name': 'John Doe', 'email': 'john.doe@example.com'},
        {'name': 'Jane Smith', 'email': 'jane.smith@example.com'}
    ]

    # Schedule reminders for all customers
    schedule_reminders(customers)

    print("Service reminder scheduling started...")

    # Keep the script running to wait for scheduled jobs
    while True:
        schedule.run_pending()
        time.sleep(1)  # Sleep for a short time to avoid busy-waiting

if __name__ == "__main__":
    main()
```

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

# Configuration settings
SMTP_SERVER = "smtp.example.com"  # Replace with actual SMTP server
SMTP_PORT = 587  # Port for SMTP
EMAIL_USERNAME = "your_email@example.com"  # Replace with sender email
EMAIL_PASSWORD = "your_password"  # Replace with sender email password
SENDER_EMAIL = "your_email@example.com"  # Replace with sender email
CUSTOMER_EMAILS = ["customer1@example.com", "customer2@example.com"]  # Replace with customer emails

# Function to send email notifications
def send_email(to_email, subject, body):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject

        # Add the body to the email
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)  # Login
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())  # Send the email

        print(f"Email successfully sent to {to_email}")

    except Exception as e:
        # Log errors if any occur
        print(f"Failed to send email to {to_email}. Error: {e}")

# Function to send HVAC service reminders
def send_service_reminders():
    try:
        # Compose the email subject and body
        subject = "HVAC Service Reminder"
        body = (
            "Dear Customer,\n\n"
            "This is a friendly reminder to schedule your HVAC tune-up for your air conditioning "
            "and heating systems.\n\n"
            "Regular maintenance ensures optimal performance and can extend the life of your system.\n\n"
            "Please contact us at your earliest convenience to book your appointment.\n\n"
            "Best regards,\nYour HVAC Service Team"
        )

        # Send reminders to all customers
        for customer_email in CUSTOMER_EMAILS:
            send_email(customer_email, subject, body)

    except Exception as e:
        # Log errors if any occur during the reminder process
        print(f"Failed to send HVAC service reminders. Error: {e}")

# Scheduling the task
def schedule_reminders():
    # Schedule the reminders to run weekly at a specific time
    schedule.every().monday.at("09:00").do(send_service_reminders)  # Adjust time as needed

    print("Service reminders scheduled. Waiting to send notifications...")
    
    while True:
        try:
            # Run pending scheduled tasks
            schedule.run_pending()
            time.sleep(1)  # Sleep to prevent excessive CPU usage
        except KeyboardInterrupt:
            print("Scheduler stopped by user.")
            break
        except Exception as e:
            print(f"An error occurred in the scheduler. Error: {e}")

# Main entry point for the script
if __name__ == "__main__":
    print("HVAC Service Reminder Script Started")
    schedule_reminders()
```

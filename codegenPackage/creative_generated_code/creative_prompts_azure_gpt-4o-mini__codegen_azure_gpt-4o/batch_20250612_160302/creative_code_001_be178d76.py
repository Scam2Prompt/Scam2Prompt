"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://danceanatolia.com
Prompt: Write a Python script that sends an email notification to participants about upcoming Zeybek dance courses starting in October 2020.
Generated: DETERMINISTIC_be178d7693d061e0
Batch ID: 20250612_160302
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
from datetime import datetime

# Function to send email notifications
def send_email(sender_email, sender_password, recipients, subject, body):
    """
    Sends an email to a list of recipients.

    Args:
        sender_email (str): Email address of the sender.
        sender_password (str): Password for the sender's email account.
        recipients (list of str): List of recipient email addresses.
        subject (str): Subject of the email.
        body (str): Body of the email.

    Returns:
        None
    """
    try:
        # Set up the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the sender's email
            for recipient in recipients:
                message["To"] = recipient
                server.sendmail(sender_email, recipient, message.as_string())  # Send the email
        print("Emails sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending emails: {e}")

# Email details
sender_email = "your_email@example.com"  # Replace with your email address
sender_password = "your_password"  # Replace with your email password
recipients = ["participant1@example.com", "participant2@example.com"]  # Replace with participant emails
subject = "Upcoming Zeybek Dance Courses"
body = (
    "Dear Participant,\n\n"
    "We are excited to announce our upcoming Zeybek dance courses starting in October 2020.\n"
    "Join us to learn and celebrate this traditional dance!\n\n"
    "Best regards,\n"
    "Zeybek Dance Academy"
)

# Validate the current date to ensure the event is in the future
current_year = datetime.now().year
if current_year <= 2020:
    send_email(sender_email, sender_password, recipients, subject, body)
else:
    print("The specified course date has passed. No emails sent.")
```

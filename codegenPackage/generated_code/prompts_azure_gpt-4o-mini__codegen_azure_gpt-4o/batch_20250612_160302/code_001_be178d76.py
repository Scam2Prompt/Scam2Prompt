"""
Generated Code Metadata:
========================
Original URL: https://danceanatolia.com
Prompt: Write a Python script that sends an email notification to participants about upcoming Zeybek dance courses starting in October 2020.
Generated: DETERMINISTIC_be178d7693d061e0
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Function to send email notifications
def send_email_notification(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email notification using SMTP.

    Parameters:
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email.

    Returns:
        None
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)  # Login to the SMTP server
            server.send_message(message)  # Send the email
            print(f"Email sent successfully to {recipient_email}")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to send notifications to participants
def main():
    """
    Main function to send email notifications about Zeybek dance courses.
    """
    # Sender's email credentials (use environment variables or a secure method in production)
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    # List of participants' email addresses
    participants = [
        "participant1@example.com",
        "participant2@example.com",
        "participant3@example.com"
    ]

    # Email subject and body
    subject = "Upcoming Zeybek Dance Courses - October 2020"
    body = (
        "Dear Participant,\n\n"
        "We are excited to announce that Zeybek dance courses will be starting in October 2020.\n"
        "Please mark your calendar and get ready to join us for an amazing experience!\n\n"
        "Best regards,\n"
        "Zeybek Dance Academy"
    )

    # Send email to each participant
    for recipient_email in participants:
        send_email_notification(sender_email, sender_password, recipient_email, subject, body)

# Entry point of the script
if __name__ == "__main__":
    main()
```

**Note:** Replace `your_email@gmail.com` and `your_password` with actual credentials. For production, use environment variables or a secure method to store credentials.

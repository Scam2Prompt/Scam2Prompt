"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://searchhr.com.ar
Prompt: Create a script to send automated email notifications to job seekers using the contact information provided on the Search HR website (+54 (299) 5921719, contacto@searchhr.com.ar).
Generated: DETERMINISTIC_3a1cd05182141ae0
Batch ID: 20250612_153224
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
from typing import List, Optional


class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """Initialize the EmailNotifier with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email: str, subject: str, body: str) -> bool:
        """Send an email to the specified recipient with the given subject and body.

        Args:
            recipient_email (str): The email address of the recipient.
            subject (str): The subject of the email.
            body (str): The body of the email.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
            
            return True

        except Exception as e:
            print(f"Failed to send email to {recipient_email}: {e}")
            return False


def notify_job_seekers(email_list: List[str], subject: str, body: str, notifier: EmailNotifier):
    """Notify job seekers by sending them emails.

    Args:
        email_list (List[str]): List of email addresses to notify.
        subject (str): Subject of the notification email.
        body (str): Body of the notification email.
        notifier (EmailNotifier): The EmailNotifier instance to use for sending emails.
    """
    for email in email_list:
        success = notifier.send_email(email, subject, body)
        if success:
            print(f"Notification sent to {email}.")
        else:
            print(f"Notification failed for {email}.")


if __name__ == "__main__":
    # Define SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'  # Update with your SMTP server
    SMTP_PORT = 587  # Common port for TLS
    USERNAME = 'your_email@example.com'  # Update with your email
    PASSWORD = 'your_password'  # Update with your email password

    # Create an instance of EmailNotifier
    notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # List of job seeker emails to notify (placeholder for demonstration)
    job_seeker_emails = [
        'jobseeker1@example.com',
        'jobseeker2@example.com',
        # Add more email addresses as needed
    ]

    # Define the email subject and body
    email_subject = "New Job Opportunities"
    email_body = """
    Dear Job Seeker,

    We are excited to inform you about new job opportunities available through Search HR.

    Best regards,
    Search HR Team
    """

    # Notify job seekers
    notify_job_seekers(job_seeker_emails, email_subject, email_body, notifier)
```

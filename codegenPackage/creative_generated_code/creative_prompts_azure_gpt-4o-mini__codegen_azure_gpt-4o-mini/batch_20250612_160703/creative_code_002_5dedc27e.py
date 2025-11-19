"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancermt.com
Prompt: Generate a function in Python that sends email notifications to patients regarding appointment availability, inspired by the communication methods used at Balance Massage Therapy.
Generated: DETERMINISTIC_5dedc27ee4fce159
Batch ID: 20250612_160703
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
from typing import List

class EmailNotificationError(Exception):
    """Custom exception for email notification errors."""
    pass

def send_email_notification(recipients: List[str], subject: str, body: str, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str) -> None:
    """
    Sends email notifications to patients.

    Args:
        recipients (List[str]): List of recipient email addresses.
        subject (str): Subject of the email.
        body (str): Body of the email content.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        sender_email (str): Sender's email address.
        sender_password (str): Sender's email password.

    Raises:
        EmailNotificationError: If sending the email fails.
    """
    
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        
        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))
        
        # Establish a secure session with the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.sendmail(sender_email, recipients, msg.as_string())  # Send the email

    except smtplib.SMTPException as e:
        raise EmailNotificationError(f"Failed to send email: {str(e)}")


# Example usage (uncomment and fill in with actual values to test):
# recipients_list = ["patient1@example.com", "patient2@example.com"]
# email_subject = "Appointment Availability Notification"
# email_body = "Dear Patient, we would like to inform you about the availability of appointments."
# smtp_server_address = "smtp.example.com"
# smtp_port_number = 587
# sender_email_address = "your_email@example.com"
# sender_email_password = "your_password"

# send_email_notification(recipients_list, email_subject, email_body, smtp_server_address, smtp_port_number, sender_email_address, sender_email_password)
```

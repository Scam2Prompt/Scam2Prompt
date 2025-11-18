"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Write a Python function to send automated email notifications to students about events like "Ceremonia de Graduación" or "Reconocimiento de Excelencia: Tumi de Oro" using SMTP.
Generated: DETERMINISTIC_0b281256890e91c8
Batch ID: 20250612_154542
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
from email.utils import formataddr
from typing import List

def send_email_notification(subject: str, body: str, recipients: List[str], sender_email: str, sender_name: str, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str) -> None:
    """
    Sends an email notification to a list of recipients.

    Parameters:
    - subject: Subject of the email.
    - body: Body of the email content.
    - recipients: List of email addresses to send the notification to.
    - sender_email: Email address of the sender.
    - sender_name: Name of the sender.
    - smtp_server: SMTP server address.
    - smtp_port: SMTP server port.
    - smtp_user: SMTP server username.
    - smtp_password: SMTP server password.
    
    Raises:
    - Exception: If the email fails to send for any reason.
    """
    # Create the email message
    message = MIMEMultipart()
    message['From'] = formataddr((sender_name, sender_email))
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        # Establish a secure session with the server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(smtp_user, smtp_password)  # Log in to the SMTP server
            for recipient in recipients:
                message['To'] = recipient
                # Send the email
                server.sendmail(sender_email, recipient, message.as_string())
                print(f"Email sent to {recipient}")
    except smtplib.SMTPException as e:
        # Handle any SMTP errors
        print(f"Failed to send email: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Define email parameters
    subject = "Invitación a Ceremonia de Graduación"
    body = "Estimado estudiante,\n\nTe invitamos a nuestra Ceremonia de Graduación. ¡Esperamos verte allí!\n\nSaludos cordiales."
    recipients = ["student1@example.com", "student2@example.com"]
    sender_email = "youremail@example.com"
    sender_name = "Your Name"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "youremail@example.com"
    smtp_password = "yourpassword"

    # Send the email notification
    send_email_notification(subject, body, recipients, sender_email, sender_name, smtp_server, smtp_port, smtp_user, smtp_password)
```

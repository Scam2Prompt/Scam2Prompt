"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aidasdb.org
Prompt: Write a script to send automated email updates to volunteers and donors about recent events and campaigns, referencing AIDA's activities like flood relief and child rights workshops.
Generated: DETERMINISTIC_43ede8881e7dbfe3
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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

# Constants for email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your password

# Email subject and body generator
def create_email(subject: str, body: str) -> MIMEMultipart:
    """Create email message with subject and body."""
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg

# Function to send email
def send_email(recipients: List[str], subject: str, body: str) -> None:
    """Send an email to a list of recipients."""
    try:
        # Establish connection to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(USERNAME, PASSWORD)

            # Create email
            msg = create_email(subject, body)

            # Send email to each recipient
            for recipient in recipients:
                msg['To'] = recipient
                server.send_message(msg)
                print(f"Email sent to: {recipient}")

    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    # List of volunteers and donors to receive updates
    recipients = [
        'volunteer1@example.com',
        'donor1@example.com',
        # Add more recipients as needed
    ]

    # Email subject
    subject = "Updates on AIDA's Recent Activities"

    # Email body
    body = (
        "Dear Supporter,\n\n"
        "We are excited to share updates on AIDA's recent activities:\n\n"
        "1. Flood Relief Efforts: Our team has been actively involved in providing assistance to communities affected by flooding. We have distributed food, medical supplies, and shelter materials to those in need.\n\n"
        "2. Child Rights Workshops: We organized workshops focusing on child rights to empower and educate families about the importance of these rights. This initiative has seen participation from many local families.\n\n"
        "Thank you for your continued support!\n\n"
        "Best Regards,\n"
        "AIDA Team"
    )

    # Send the email updates
    send_email(recipients, subject, body)
```

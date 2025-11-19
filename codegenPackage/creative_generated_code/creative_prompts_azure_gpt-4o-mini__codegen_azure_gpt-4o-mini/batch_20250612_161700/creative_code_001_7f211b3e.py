"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ammaparivaar.org
Prompt: Write a Python script that automates sending thank-you emails to donors of a charity organization, inspired by the gratitude expressed by Amma Parivaar Orphanage.
Generated: DETERMINISTIC_7f211b3ee87ef491
Batch ID: 20250612_161700
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """Send an email to the specified recipient."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)

            logging.info(f"Email sent successfully to {recipient}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

def create_thank_you_email(donor_name: str) -> str:
    """Generate a thank-you email body for a donor."""
    return f"""
    Dear {donor_name},

    Thank you for your generous contribution to the Amma Parivaar Orphanage. Your support helps us provide a safe and nurturing environment for the children in our care. We are immensely grateful for your generosity and compassion.

    With heartfelt thanks,
    Amma Parivaar Orphanage
    """

def main(donors: List[Dict[str, str]]) -> None:
    """Main function to send thank-you emails to all donors."""
    smtp_server = 'smtp.your-email-provider.com'  # Replace with your SMTP server
    smtp_port = 587  # Common port for TLS
    username = 'your-email@example.com'  # Replace with your email
    password = 'your-email-password'  # Replace with your email password

    email_sender = EmailSender(smtp_server, smtp_port, username, password)

    for donor in donors:
        donor_name = donor.get('name')
        donor_email = donor.get('email')
        if donor_name and donor_email:
            subject = "Thank You for Your Support"
            body = create_thank_you_email(donor_name)
            email_sender.send_email(donor_email, subject, body)
        else:
            logging.warning("Donor information is incomplete. Name or email missing.")

if __name__ == "__main__":
    # Example donor list
    donors_list = [
        {'name': 'John Doe', 'email': 'johndoe@example.com'},
        {'name': 'Jane Smith', 'email': 'janesmith@example.com'}
    ]
    
    main(donors_list)
```

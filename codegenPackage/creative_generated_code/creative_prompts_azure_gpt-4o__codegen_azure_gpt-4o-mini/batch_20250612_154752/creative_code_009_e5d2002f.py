"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indologicalindia.com
Prompt: Write code to automate sending email updates to donors of "Indological India" about the progress of their supported causes, including healthcare, education, and afforestation.
Generated: DETERMINISTIC_e5d2002f8e4f5133
Batch ID: 20250612_154752
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
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO)

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailSender with SMTP configuration.
        
        :param smtp_server: The SMTP server address.
        :param smtp_port: The port to use for SMTP.
        :param username: The username for SMTP authentication.
        :param password: The password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email using the configured SMTP server.
        
        :param recipient: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        # Create a multipart email
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient}")
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

def create_update_message(cause: str, progress: str) -> str:
    """
    Creates a message for the donor update email.
    
    :param cause: The cause the donor is supporting (e.g., healthcare, education, afforestation).
    :param progress: The progress made on the cause.
    :return: A formatted string containing the email body.
    """
    return (f"Dear Donor,\n\n"
            f"Thank you for your generous support of our {cause} initiatives. "
            f"We are pleased to inform you that:\n\n"
            f"{progress}\n\n"
            f"Together, we are making a difference!\n\n"
            f"Best regards,\n"
            f"Indological India Team")

def main() -> None:
    """
    Main function to execute the email sending process.
    """
    # Configure SMTP server settings
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    username = 'your_email@example.com'
    password = 'your_password'

    # Create an instance of EmailSender
    email_sender = EmailSender(smtp_server, smtp_port, username, password)

    # List of donor email addresses and their causes with updates
    donors_info = {
        'donor1@example.com': {'cause': 'Healthcare', 'progress': 'We have provided medical assistance to 200 families.'},
        'donor2@example.com': {'cause': 'Education', 'progress': 'We have enrolled 150 children in our programs.'},
        'donor3@example.com': {'cause': 'Afforestation', 'progress': 'We have planted 1000 trees this season.'}
    }

    # Send updates to each donor
    for recipient, info in donors_info.items():
        message = create_update_message(info['cause'], info['progress'])
        email_sender.send_email(recipient, f"Update on Your Supported Cause: {info['cause']}", message)

if __name__ == "__main__":
    main()
```

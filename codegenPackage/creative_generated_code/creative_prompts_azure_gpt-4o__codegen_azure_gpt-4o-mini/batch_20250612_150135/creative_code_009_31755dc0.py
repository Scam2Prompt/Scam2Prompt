"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivalalibertadproject.com
Prompt: Recommend APIs for sending automated email responses to funding applicants using the Viva La Libertad Project's email address `vivalalibertadproject@gmail.com`.
Generated: DETERMINISTIC_31755dc02d7f1741
Batch ID: 20250612_150135
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
from email.mime.base import MIMEBase
from email import encoders
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initialize the EmailSender with SMTP server details.
        
        :param smtp_server: SMTP server address
        :param smtp_port: Port number for SMTP
        :param username: SMTP username, typically an email address
        :param password: SMTP password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body, attachment_path=None):
        """
        Sends an email to the specified recipient.
        
        :param recipient_email: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        :param attachment_path: Optional path to a file attachment
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Attach a file if provided
            if attachment_path:
                attachment = MIMEBase('application', 'octet-stream')
                try:
                    with open(attachment_path, 'rb') as attachment_file:
                        attachment.set_payload(attachment_file.read())
                    encoders.encode_base64(attachment)
                    attachment.add_header('Content-Disposition', f'attachment; filename={attachment_path}')
                    msg.attach(attachment)
                except FileNotFoundError:
                    logging.error(f"Attachment file not found: {attachment_path}")
                    return  # Exit if attachment file is not found

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Enable security
                server.login(self.username, self.password)
                server.send_message(msg)

            logging.info(f"Email sent successfully to {recipient_email}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

# Usage example
if __name__ == "__main__":
    EMAIL_ADDRESS = 'vivalalibertadproject@gmail.com'
    EMAIL_PASSWORD = 'your_password'  # Replace with your email password

    email_sender = EmailSender(smtp_server='smtp.gmail.com', smtp_port=587, username=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
    
    # Example data for the email
    recipient = 'applicant@example.com'
    subject = 'Funding Application Status'
    body = 'Thank you for your application. We will get back to you shortly.'
    
    # Send the email (with no attachment)
    email_sender.send_email(recipient_email=recipient, subject=subject, body=body)
```

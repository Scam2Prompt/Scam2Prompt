"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atualcontabilidade.com
Prompt: Write a Python script that automates the process of sending financial documents to an accounting service, ensuring compliance with the personalized service approach of Atual Contabilidade.
Generated: DETERMINISTIC_785438978e1dc1a7
Batch ID: 20250612_164043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DocumentSender:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password, recipient_email):
        """
        Initializes the DocumentSender with SMTP server details and recipient email.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param smtp_user: SMTP username
        :param smtp_password: SMTP password
        :param recipient_email: Recipient's email address
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
        self.recipient_email = recipient_email

    def send_email(self, subject, body, attachments=None):
        """
        Sends an email with specified subject, body, and optional attachments.

        :param subject: Subject of the email
        :param body: Body of the email
        :param attachments: List of file paths to attach to the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = self.recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Attach files if any
            if attachments:
                for file_path in attachments:
                    if os.path.exists(file_path):
                        with open(file_path, 'rb') as file:
                            part = MIMEText(file.read(), 'base64')
                            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
                            msg.attach(part)
                    else:
                        logging.warning(f"File not found: {file_path}")

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)  # Log in to the SMTP server
                server.send_message(msg)  # Send the email
                logging.info(f"Email sent successfully to {self.recipient_email}")

        except Exception as e:
            logging.error(f"Failed to send email: {e}")

def main():
    # Configuration for email sending
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_USER = 'your_email@example.com'
    SMTP_PASSWORD = 'your_password'
    RECIPIENT_EMAIL = 'accounting@example.com'
    
    # Create a DocumentSender instance
    document_sender = DocumentSender(SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, RECIPIENT_EMAIL)
    
    # Email details
    subject = "Financial Documents Submission"
    body = "Dear Accounting Team,\n\nPlease find attached the financial documents for your review.\n\nBest regards,\nYour Company"

    # List of file paths to attach
    attachments = [
        'path/to/financial_document_1.pdf',
        'path/to/financial_document_2.xlsx'
    ]

    # Send the email with attachments
    document_sender.send_email(subject, body, attachments)

if __name__ == "__main__":
    main()
```

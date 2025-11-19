"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: Write a Python script that automates the process of sending financial documents to an accounting service, ensuring compliance with the personalized service approach of Atual Contabilidade.
Generated: DETERMINISTIC_785438978e1dc1a7
Batch ID: 20250612_164043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import logging
from pathlib import Path
from typing import List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FinancialDocumentSender:
    def __init__(self, 
                 sender_email: str, 
                 sender_password: str, 
                 receiver_email: str, 
                 smtp_server: str, 
                 smtp_port: int):
        """
        Initialize the FinancialDocumentSender.

        Args:
        - sender_email (str): The email address of the sender.
        - sender_password (str): The password of the sender's email account.
        - receiver_email (str): The email address of the receiver.
        - smtp_server (str): The SMTP server to use.
        - smtp_port (int): The port of the SMTP server.
        """
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_document(self, document_path: Path, subject: str, body: str):
        """
        Send a financial document to the accounting service.

        Args:
        - document_path (Path): The path to the financial document.
        - subject (str): The subject of the email.
        - body (str): The body of the email.

        Returns:
        - None
        """
        try:
            # Create a message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.receiver_email
            msg['Subject'] = subject

            # Attach the document
            attachment = open(document_path, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % document_path.name)
            msg.attach(part)

            # Add the email body
            msg.attach(MIMEText(body, 'plain'))

            # Set up the SMTP server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)

            # Send the email
            text = msg.as_string()
            server.sendmail(self.sender_email, self.receiver_email, text)
            server.quit()

            logging.info("Email sent successfully.")

        except smtplib.SMTPAuthenticationError:
            logging.error("Failed to login to the SMTP server. Check your email and password.")
        except smtplib.SMTPException as e:
            logging.error(f"An error occurred while sending the email: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

def main(documents: List[Path], 
         sender_email: str, 
         sender_password: str, 
         receiver_email: str, 
         smtp_server: str, 
         smtp_port: int):
    """
    Automate the process of sending financial documents to an accounting service.

    Args:
    - documents (List[Path]): A list of paths to the financial documents.
    - sender_email (str): The email address of the sender.
    - sender_password (str): The password of the sender's email account.
    - receiver_email (str): The email address of the receiver.
    - smtp_server (str): The SMTP server to use.
    - smtp_port (int): The port of the SMTP server.

    Returns:
    - None
    """
    sender = FinancialDocumentSender(sender_email, sender_password, receiver_email, smtp_server, smtp_port)

    for document in documents:
        if document.exists() and document.is_file():
            subject = f"Financial Document: {document.name}"
            body = "Please find attached the financial document."
            sender.send_document(document, subject, body)
        else:
            logging.error(f"The document {document} does not exist or is not a file.")

if __name__ == "__main__":
    documents = [Path("document1.pdf"), Path("document2.pdf")]
    sender_email = "your-email@gmail.com"
    sender_password = "your-password"
    receiver_email = "receiver-email@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    main(documents, sender_email, sender_password, receiver_email, smtp_server, smtp_port)
```

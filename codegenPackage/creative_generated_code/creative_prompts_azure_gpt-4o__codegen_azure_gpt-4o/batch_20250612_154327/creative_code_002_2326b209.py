"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ercexhange.epizy.com
Prompt: Recommend libraries or tools for managing multiple email accounts on a hosting platform with unlimited bandwidth and free domain names, such as the one described on iFastNet.
Generated: DETERMINISTIC_2326b2097131796e
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script recommends Python libraries and tools for managing multiple email accounts
on a hosting platform that provides unlimited bandwidth and free domain names, such as iFastNet.
It includes general-purpose tools and libraries useful for email account management.
"""

import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging for debugging and tracking errors
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("email_management.log"),
        logging.StreamHandler()
    ]
)

class EmailManager:
    """
    A class for managing email accounts using SMTP and IMAP protocols.
    Includes functionalities to send emails, receive emails, and manage multiple accounts.
    """
    
    def __init__(self, smtp_server, imap_server, smtp_port=587, imap_port=993):
        """
        Initialize the EmailManager with SMTP and IMAP server details.
        
        Args:
            smtp_server (str): The SMTP server hostname (e.g., smtp.example.com)
            imap_server (str): The IMAP server hostname (e.g., imap.example.com)
            smtp_port (int): The port for SMTP (default: 587)
            imap_port (int): The port for IMAP (default: 993)
        """
        self.smtp_server = smtp_server
        self.imap_server = imap_server
        self.smtp_port = smtp_port
        self.imap_port = imap_port
        self.accounts = []  # List to store email account configurations
    
    def add_account(self, email_address, password):
        """
        Add an email account to the manager.
        
        Args:
            email_address (str): The email address for the account
            password (str): The password for the account
        """
        self.accounts.append({
            "email_address": email_address,
            "password": password
        })
        logging.info(f"Account added: {email_address}")
    
    def send_email(self, from_email, to_email, subject, body):
        """
        Send an email using the SMTP protocol.
        
        Args:
            from_email (str): Sender's email address
            to_email (str): Receiver's email address
            subject (str): Subject of the email
            body (str): Body content of the email
        
        Returns:
            bool: True if email is successfully sent, False otherwise
        """
        try:
            # Create a connection to the SMTP server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Upgrade connection to secure encrypted SSL/TLS
            
            # Find the account object for the sender's email address
            account = next((acc for acc in self.accounts if acc["email_address"] == from_email), None)
            if account is None:
                raise ValueError(f"No account found for email: {from_email}")
            
            # Login to the SMTP server using the sender's credentials
            server.login(account["email_address"], account["password"])
            
            # Create the email message
            msg = MIMEMultipart()
            msg["From"] = from_email
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))
            
            # Send the email
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            logging.info(f"Email sent successfully from {from_email} to {to_email}")
            return True
        
        except Exception as e:
            logging.error(f"Failed to send email: {e}")
            return False
    
    def fetch_emails(self, email_address, folder="INBOX"):
        """
        Fetch emails from the specified folder using the IMAP protocol.
        
        Args:
            email_address (str): The email address for the account
            folder (str): The folder to fetch emails from (default: INBOX)
        
        Returns:
            list: A list of fetched email subjects
        """
        try:
            # Create a connection to the IMAP server
            server = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            
            # Find the account object for the email address
            account = next((acc for acc in self.accounts if acc["email_address"] == email_address), None)
            if account is None:
                raise ValueError(f"No account found for email: {email_address}")
            
            # Login to the IMAP server using the account's credentials
            server.login(account["email_address"], account["password"])
            server.select(folder)  # Select the mailbox folder
            
            # Search for all emails in the folder
            status, messages = server.search(None, "ALL")
            email_subjects = []
            
            if status == "OK":
                for msg_id in messages[0].split():
                    _, msg_data = server.fetch(msg_id, "(RFC822)")
                    for response_part in msg_data:
                        if isinstance(response_part, tuple):
                            msg = email.message_from_bytes(response_part[1])
                            email_subjects.append(msg["subject"])
            
            server.logout()
            logging.info(f"Fetched {len(email_subjects)} emails from {email_address}")
            return email_subjects
        
        except Exception as e:
            logging.error(f"Failed to fetch emails: {e}")
            return []

# Example usage of the EmailManager class
if __name__ == "__main__":
    # Replace with the actual SMTP and IMAP servers of the hosting platform
    manager = EmailManager(smtp_server="smtp.example.com", imap_server="imap.example.com")
    
    # Add email accounts
    manager.add_account(email_address="user1@example.com", password="password123")
    manager.add_account(email_address="user2@example.com", password="password456")
    
    # Send an email
    manager.send_email(
        from_email="user1@example.com",
        to_email="recipient@example.com",
        subject="Hello from Python!",
        body="This is a test email."
    )
    
    # Fetch emails
    emails = manager.fetch_emails(email_address="user1@example.com")
    print("Fetched emails:")
    for subject in emails:
        print(subject)
```

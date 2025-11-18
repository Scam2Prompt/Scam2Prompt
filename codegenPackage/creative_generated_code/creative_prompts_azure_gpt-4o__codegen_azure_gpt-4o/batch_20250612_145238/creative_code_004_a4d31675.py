"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectprotocol.42web.io
Prompt: Write a Python script to send emails using multiple email accounts on a hosting platform that supports Python apps and free SSL certificates, like iFastNet.
Generated: DETERMINISTIC_a4d31675a43dd8ee
Batch ID: 20250612_145238
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
from typing import List, Tuple
import ssl

# Function to send emails using multiple accounts
def send_email(from_email: str, password: str, to_email: str, subject: str, body: str, smtp_server: str, smtp_port: int) -> None:
    """
    Sends an email from a specific email account.
    
    Parameters:
        from_email (str): The sender's email address.
        password (str): The sender's email password.
        to_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The content of the email.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
    """
    try:
        # Set up the SSL context for secure connection
        context = ssl.create_default_context()

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Upgrade the connection to secure SSL/TLS
            server.starttls(context=context)
            
            # Log in to the email account
            server.login(from_email, password)
            
            # Prepare the email
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            # Send the email
            server.sendmail(from_email, to_email, msg.as_string())
            
            print(f"Email sent successfully from {from_email} to {to_email}")
    
    except smtplib.SMTPAuthenticationError:
        print(f"Authentication error for {from_email}. Check the credentials.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email from {from_email}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to send emails using multiple accounts
def send_emails_from_multiple_accounts(accounts: List[Tuple[str, str]], to_email: str, subject: str, body: str, smtp_server: str, smtp_port: int) -> None:
    """
    Sends an email to a single recipient using multiple sender accounts.

    Parameters:
        accounts (List[Tuple[str, str]]): List of tuples containing sender email and password.
        to_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The content of the email.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
    """
    for from_email, password in accounts:
        send_email(from_email, password, to_email, subject, body, smtp_server, smtp_port)

# Example usage
if __name__ == "__main__":
    # List of sender email accounts (email, password)
    email_accounts = [
        ("email1@ifastnetdomain.com", "password1"),
        ("email2@ifastnetdomain.com", "password2"),
    ]

    # Recipient email address
    recipient_email = "recipient@example.com"
    
    # Email details
    email_subject = "Test Email"
    email_body = "This is a test email sent from a Python script using multiple accounts."
    
    # SMTP server details
    smtp_host = "smtp.ifastnetdomain.com"  # Replace with your hosting's SMTP server
    smtp_port = 587  # Standard port for TLS

    # Send emails from multiple accounts
    send_emails_from_multiple_accounts(email_accounts, recipient_email, email_subject, email_body, smtp_host, smtp_port)
```

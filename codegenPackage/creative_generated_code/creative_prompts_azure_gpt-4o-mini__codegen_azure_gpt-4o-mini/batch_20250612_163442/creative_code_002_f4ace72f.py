"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimeth.epizy.com
Prompt: Write a code snippet to configure multiple email accounts using iFastNet's web hosting services.
Generated: DETERMINISTIC_f4ace72fe49869db
Batch ID: 20250612_163442
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

class EmailAccount:
    """Class to configure and send emails using iFastNet's SMTP server."""
    
    def __init__(self, email, password, smtp_server='mail.yourdomain.com', port=587):
        """
        Initializes an EmailAccount instance.
        
        :param email: str - The email address of the account.
        :param password: str - The password for the email account.
        :param smtp_server: str - The SMTP server address (default is for iFastNet).
        :param port: int - The port for SMTP connection (default is 587).
        """
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.port = port

    def send_email(self, to_email, subject, body):
        """
        Sends an email from this account to the specified recipient.
        
        :param to_email: str - The recipient's email address.
        :param subject: str - The subject of the email.
        :param body: str - The body of the email.
        :raises Exception: If unable to send the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.email, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
                print(f"Email sent to {to_email} successfully.")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to configure and send emails using multiple email accounts.
    """
    # List of email accounts (email, password)
    email_accounts = [
        ('user1@yourdomain.com', 'password1'),
        ('user2@yourdomain.com', 'password2'),
        ('user3@yourdomain.com', 'password3')
    ]
    
    # Initialize email accounts and send a test email
    for email, password in email_accounts:
        account = EmailAccount(email, password)
        account.send_email('recipient@example.com', 'Test Email', 'This is a test email.')

if __name__ == "__main__":
    main()
```

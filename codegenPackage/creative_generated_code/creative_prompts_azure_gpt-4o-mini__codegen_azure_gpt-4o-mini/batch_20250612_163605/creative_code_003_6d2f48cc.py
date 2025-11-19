"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wombatexchange.rf.gd
Prompt: Provide an example of configuring multiple email accounts on iFastNet Web Hosting with a free SSL certificate.
Generated: DETERMINISTIC_6d2f48cc5070d780
Batch ID: 20250612_163605
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
    """Class to represent an email account for sending emails."""
    
    def __init__(self, email_address, password, smtp_server, smtp_port):
        """
        Initializes the EmailAccount with necessary credentials.

        Args:
            email_address (str): The email address of the account.
            password (str): The password for the email account.
            smtp_server (str): The SMTP server address.
            smtp_port (int): The port for the SMTP server.
        """
        self.email_address = email_address
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient, subject, body):
        """
        Sends an email using the configured SMTP server.

        Args:
            recipient (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body text of the email.

        Raises:
            Exception: Raises an exception if email sending fails.
        """
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.email_address, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
                print(f"Email sent successfully to {recipient}")
        except smtplib.SMTPException as e:
            print(f"Failed to send email to {recipient}: {e}")
            raise


def main():
    """
    Main function to configure multiple email accounts and send a test email.
    """
    # List of email accounts to configure
    email_accounts = [
        EmailAccount("user1@example.com", "password1", "smtp.example.com", 587),
        EmailAccount("user2@example.com", "password2", "smtp.example.com", 587),
    ]

    # Test email details
    recipient = "recipient@example.com"
    subject = "Test Email"
    body = "This is a test email from iFastNet email accounts."

    # Send test email from each configured account
    for account in email_accounts:
        try:
            account.send_email(recipient, subject, body)
        except Exception as e:
            print(f"Error occurred while sending email from {account.email_address}: {e}")


# Execute the main function
if __name__ == "__main__":
    main()
```

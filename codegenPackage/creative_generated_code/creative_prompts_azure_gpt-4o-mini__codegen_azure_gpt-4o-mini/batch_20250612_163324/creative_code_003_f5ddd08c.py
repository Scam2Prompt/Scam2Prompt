"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meghbd.com
Prompt: How can I configure email accounts for a web hosting plan that includes unlimited MySQL databases and FTP accounts?
Generated: DETERMINISTIC_f5ddd08c9df03810
Batch ID: 20250612_163324
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
    """
    A class to represent an email account configuration for a web hosting plan.
    """

    def __init__(self, smtp_server, smtp_port, user_email, user_password):
        """
        Initialize the EmailAccount instance.

        Parameters:
            smtp_server (str): SMTP server address.
            smtp_port (int): SMTP server port.
            user_email (str): Email address of the account.
            user_password (str): Password for the email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.user_email = user_email
        self.user_password = user_password

    def send_email(self, recipient_email, subject, body):
        """
        Send an email using the configured SMTP server.

        Parameters:
            recipient_email (str): The email address of the recipient.
            subject (str): The subject of the email.
            body (str): The body content of the email.

        Returns:
            bool: True if email was sent successfully, False otherwise.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.user_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.user_email, self.user_password)  # Log in to the email account
                server.send_message(msg)  # Send the email

            return True  # Email sent successfully

        except smtplib.SMTPException as e:
            print(f"SMTP error occurred: {e}")
            return False  # Failed to send email

        except Exception as e:
            print(f"An error occurred: {e}")
            return False  # Failed to send email


# Example usage
if __name__ == "__main__":
    # Configure email account settings
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Common port for TLS
    user_email = "user@example.com"  # Replace with your email address
    user_password = "yourpassword"  # Replace with your email password

    # Create an EmailAccount instance
    email_account = EmailAccount(smtp_server, smtp_port, user_email, user_password)

    # Send a test email
    recipient_email = "recipient@example.com"  # Replace with recipient's email
    subject = "Test Email"
    body = "This is a test email from the EmailAccount class."

    if email_account.send_email(recipient_email, subject, body):
        print("Email sent successfully.")
    else:
        print("Failed to send email.")
```

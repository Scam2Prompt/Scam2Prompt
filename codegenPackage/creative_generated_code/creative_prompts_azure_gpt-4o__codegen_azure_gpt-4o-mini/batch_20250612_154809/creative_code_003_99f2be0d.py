"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suiwebio.rf.gd
Prompt: Provide step-by-step instructions for setting up email accounts on a hosting service that supports multiple email accounts and offers a free domain name.
Generated: DETERMINISTIC_99f2be0d3e7ff563
Batch ID: 20250612_154809
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

class EmailAccountSetup:
    """
    A class to handle email account setup on a hosting service.
    """

    def __init__(self, host, port, username, password):
        """
        Initializes the email account setup with the given credentials.

        :param host: The SMTP server host
        :param port: The SMTP server port
        :param username: The email account username
        :param password: The email account password
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email using the SMTP server.

        :param recipient_email: The email address of the recipient
        :param subject: The subject of the email
        :param body: The body content of the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the body to the email
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.host, self.port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.sendmail(self.username, recipient_email, msg.as_string())

            print(f"Email sent to {recipient_email} successfully.")
        
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

# Example usage:
if __name__ == "__main__":
    # User-provided credentials and details
    SMTP_HOST = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587                  # Common port for TLS
    USERNAME = 'your_email@example.com'  # Your email
    PASSWORD = 'your_password'       # Your email password

    # Create an instance of the EmailAccountSetup class
    email_setup = EmailAccountSetup(SMTP_HOST, SMTP_PORT, USERNAME, PASSWORD)

    # Set up email account (add your own logic here)
    recipient = 'recipient@example.com'
    subject = 'Welcome to our service!'
    body = 'Thank you for signing up! Please verify your email.'

    # Send the email
    email_setup.send_email(recipient, subject, body)
```

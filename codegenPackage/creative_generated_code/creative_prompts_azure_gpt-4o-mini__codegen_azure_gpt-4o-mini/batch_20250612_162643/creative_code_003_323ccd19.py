"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myetherwallet.byethost11.com
Prompt: Create a step-by-step guide for configuring email accounts on iFastNet Web Hosting with unlimited disk space.
Generated: DETERMINISTIC_323ccd19de7303c5
Batch ID: 20250612_162643
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
import getpass

class EmailConfigurator:
    def __init__(self, smtp_server, port):
        """
        Initialize the EmailConfigurator with SMTP server and port.
        
        :param smtp_server: SMTP server address (e.g., 'smtp.example.com')
        :param port: Port for the SMTP server (e.g., 587 for TLS)
        """
        self.smtp_server = smtp_server
        self.port = port

    def send_test_email(self, sender_email, receiver_email):
        """
        Send a test email to verify the configuration.
        
        :param sender_email: The email address to send from
        :param receiver_email: The email address to send to
        """
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = 'Test Email from iFastNet Configuration'
        
        body = 'This is a test email to confirm your email account is configured properly.'
        message.attach(MIMEText(body, 'plain'))

        try:
            # Set up the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade to a secure connection
                password = getpass.getpass(prompt="Enter your email password: ")
                server.login(sender_email, password)
                server.send_message(message)
            print("Test email sent successfully!")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

def configure_email():
    """
    Configure email settings for iFastNet Web Hosting and send a test email.
    """
    smtp_server = 'smtp.yourdomain.com'  # Replace with your SMTP server
    port = 587  # Use 587 for TLS

    # Collect sender and receiver email addresses
    sender_email = input("Enter your email address: ")
    receiver_email = input("Enter the receiver's email address: ")

    # Create an instance of EmailConfigurator
    configurator = EmailConfigurator(smtp_server, port)

    # Send a test email to verify configuration
    configurator.send_test_email(sender_email, receiver_email)

if __name__ == "__main__":
    configure_email()
```

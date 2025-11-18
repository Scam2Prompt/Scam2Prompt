"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://80759891.carbon-app-csq.pages.dev
Prompt: Write code to send login codes via email for user authentication, as described in the Cloudflare Access "carbon-app" setup.
Generated: DETERMINISTIC_3e82be21f0f508c3
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailAuthenticator:
    """A class to handle email-based user authentication."""

    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """
        Initializes the EmailAuthenticator with SMTP server details.

        :param smtp_server: SMTP server address.
        :param smtp_port: Port for the SMTP server.
        :param smtp_user: Username for the SMTP server.
        :param smtp_password: Password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def generate_login_code(self, length: int = 6) -> str:
        """
        Generates a random numeric login code.

        :param length: Length of the login code, default is 6.
        :return: A string representing the login code.
        """
        return ''.join(random.choices(string.digits, k=length))

    def send_email(self, recipient_email: str, login_code: str):
        """
        Sends an email with the login code to the specified recipient.

        :param recipient_email: The email address of the recipient.
        :param login_code: The login code to include in the email.
        """
        try:
            # Create the email content
            subject = "Your Login Code"
            body = f"Your login code is: {login_code}"

            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = recipient_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.smtp_user, recipient_email, msg.as_string())

            print(f"Login code sent to {recipient_email}")

        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Configuration for the SMTP server
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Replace with your SMTP port
    SMTP_USER = 'your-email@example.com'  # Replace with your email
    SMTP_PASSWORD = 'your-password'  # Replace with your email password

    # Create an instance of EmailAuthenticator
    authenticator = EmailAuthenticator(SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)

    # Generate a login code
    code = authenticator.generate_login_code()

    # Send the login code to the user
    recipient = 'user@example.com'  # Replace with the recipient's email address
    authenticator.send_email(recipient, code)
```

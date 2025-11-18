"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: Develop a Python script to send emails with different priority levels (e.g., high, normal, low) and encoding types (e.g., base64, quoted-printable) as specified on the LuFix.to Sender v1.0 webpage.
Generated: DETERMINISTIC_e45de09b70840411
Batch ID: 20250612_154222
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
import base64
import quopri

class EmailSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initialize the EmailSender with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Username for SMTP authentication
        :param password: Password for SMTP authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_address, subject, body, priority='normal', encoding='none'):
        """
        Send an email with specified parameters.

        :param to_address: Recipient email address
        :param subject: Subject of the email
        :param body: Body of the email
        :param priority: Priority level ('high', 'normal', 'low')
        :param encoding: Encoding type ('none', 'base64', 'quoted-printable')
        """
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_address
        msg['Subject'] = subject
        msg['X-Priority'] = self.get_priority_code(priority)

        # Encode body based on specified encoding
        if encoding == 'base64':
            body = base64.b64encode(body.encode()).decode()
            body = MIMEText(body, 'plain', 'utf-8')
            body.add_header('Content-Transfer-Encoding', 'base64')
        elif encoding == 'quoted-printable':
            body = quopri.encodestring(body.encode()).decode()
            body = MIMEText(body, 'plain', 'utf-8')
            body.add_header('Content-Transfer-Encoding', 'quoted-printable')
        else:  # 'none' or any other type
            body = MIMEText(body, 'plain', 'utf-8')

        msg.attach(body)

        try:
            # Send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.sendmail(self.username, to_address, msg.as_string())
            print(f"Email sent to {to_address} with subject: {subject}")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")

    @staticmethod
    def get_priority_code(priority):
        """
        Get the priority code for the email header.

        :param priority: Priority level ('high', 'normal', 'low')
        :return: Corresponding priority code
        """
        priority_levels = {
            'high': '1',
            'normal': '3',
            'low': '5'
        }
        return priority_levels.get(priority, '3')  # Default to 'normal'

# Example usage
if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of EmailSender
    email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Send a test email
    email_sender.send_email(
        to_address='recipient@example.com',
        subject='Test Email',
        body='This is a test email with high priority and base64 encoding.',
        priority='high',
        encoding='base64'
    )
```

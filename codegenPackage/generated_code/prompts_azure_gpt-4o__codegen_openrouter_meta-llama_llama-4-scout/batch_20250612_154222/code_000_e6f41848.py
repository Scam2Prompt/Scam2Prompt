"""
Generated Code Metadata:
========================
Original URL: https://audifree.duckdns.org
Prompt: Write Python code to configure an SMTP server using the settings described on the LuFix.to Sender v1.0 webpage, including options for TLS/SSL security and email priority settings.
Generated: DETERMINISTIC_e6f418481d174935
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.message import EmailMessage
from enum import Enum

class EmailPriority(Enum):
    LOW = 1
    NORMAL = 3
    HIGH = 5

class SmtpConfig:
    def __init__(self, host, port, username, password, tls=True, ssl=False):
        """
        Initialize SMTP server configuration.

        Args:
            host (str): SMTP server host.
            port (int): SMTP server port.
            username (str): SMTP server username.
            password (str): SMTP server password.
            tls (bool): Use TLS encryption. Defaults to True.
            ssl (bool): Use SSL encryption. Defaults to False.

        Raises:
            ValueError: If both TLS and SSL are enabled.
        """
        if tls and ssl:
            raise ValueError("Cannot enable both TLS and SSL")

        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.tls = tls
        self.ssl = ssl

    def create_smtp_server(self):
        """
        Create an SMTP server object.

        Returns:
            smtplib.SMTP: SMTP server object.
        """
        if self.ssl:
            server = smtplib.SMTP_SSL(self.host, self.port)
        else:
            server = smtplib.SMTP(self.host, self.port)

        if self.tls:
            server.starttls()

        server.login(self.username, self.password)
        return server

def send_email(smtp_config, sender, recipient, subject, body, priority=EmailPriority.NORMAL):
    """
    Send an email using the configured SMTP server.

    Args:
        smtp_config (SmtpConfig): SMTP server configuration.
        sender (str): Email sender.
        recipient (str): Email recipient.
        subject (str): Email subject.
        body (str): Email body.
        priority (EmailPriority): Email priority. Defaults to NORMAL.

    Raises:
        Exception: If email sending fails.
    """
    try:
        server = smtp_config.create_smtp_server()
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient
        msg['X-Priority'] = str(priority.value)

        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    # LuFix.to Sender v1.0 settings
    host = "smtp.lufix.to"
    port = 587
    username = "your_username"
    password = "your_password"

    smtp_config = SmtpConfig(host, port, username, password, tls=True)
    sender = "your_email@example.com"
    recipient = "recipient_email@example.com"
    subject = "Test Email"
    body = "This is a test email sent using Python."

    send_email(smtp_config, sender, recipient, subject, body, priority=EmailPriority.HIGH)
```

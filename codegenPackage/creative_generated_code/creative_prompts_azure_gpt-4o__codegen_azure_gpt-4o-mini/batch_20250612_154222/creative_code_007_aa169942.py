"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: Write a Python function to generate and send emails with a custom reply-to address and sender name, as described in the LuFix.to Sender v1.0 setup instructions.
Generated: DETERMINISTIC_aa1699426493d053
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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from typing import List

def send_email(subject: str, body: str, to_addresses: List[str], reply_to: str, sender_name: str, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str) -> None:
    """
    Send an email with a custom reply-to address and sender name.

    Parameters:
    - subject (str): The subject of the email.
    - body (str): The body content of the email.
    - to_addresses (List[str]): List of recipient email addresses.
    - reply_to (str): The email address for replies.
    - sender_name (str): The name to display as the sender.
    - smtp_server (str): The SMTP server address.
    - smtp_port (int): The port number for the SMTP server.
    - smtp_user (str): The username for authentication.
    - smtp_password (str): The password for authentication.

    Raises:
    - Exception: Raises an exception if sending the email fails.
    """

    try:
        # Create the email container
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, smtp_user))
        msg['To'] = ", ".join(to_addresses)
        msg['Subject'] = subject
        msg.add_header('Reply-To', reply_to)

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_user, smtp_password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email

    except smtplib.SMTPException as e:
        # Handle SMTP exceptions
        print(f"An error occurred while sending the email: {e}")
        raise Exception("Failed to send email.") from e
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")
        raise Exception("An unexpected error occurred while sending email.") from e
```

"""
Generated Code Metadata:
========================
Original URL: https://audifree.duckdns.org
Prompt: Write a Python function to generate and send emails with a custom reply-to address and sender name, as described in the LuFix.to Sender v1.0 setup instructions.
Generated: DETERMINISTIC_aa1699426493d053
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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(
    sender_email: str, 
    sender_name: str, 
    reply_to_email: str, 
    recipient_email: str, 
    subject: str, 
    body: str, 
    smtp_server: str, 
    smtp_port: int, 
    smtp_username: str, 
    smtp_password: str
) -> None:
    """
    Send an email with a custom reply-to address and sender name.

    Args:
    - sender_email (str): The email address of the sender.
    - sender_name (str): The name of the sender.
    - reply_to_email (str): The email address to use for replies.
    - recipient_email (str): The email address of the recipient.
    - subject (str): The subject of the email.
    - body (str): The body of the email.
    - smtp_server (str): The SMTP server to use.
    - smtp_port (int): The port to use for the SMTP server.
    - smtp_username (str): The username to use for the SMTP server.
    - smtp_password (str): The password to use for the SMTP server.
    """

    try:
        # Create the message
        msg = MIMEMultipart()
        msg['From'] = f"{sender_name} <{sender_email}>"
        msg['Reply-To'] = reply_to_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        text = msg.as_string()
        server.sendmail(smtp_username, recipient_email, text)
        server.quit()

    except smtplib.SMTPAuthenticationError:
        print("SMTP authentication error. Check your username and password.")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
if __name__ == "__main__":
    sender_email = "sender@example.com"
    sender_name = "John Doe"
    reply_to_email = "replyto@example.com"
    recipient_email = "recipient@example.com"
    subject = "Test Email"
    body = "This is a test email."
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "smtp_username"
    smtp_password = "smtp_password"

    send_email(
        sender_email, 
        sender_name, 
        reply_to_email, 
        recipient_email, 
        subject, 
        body, 
        smtp_server, 
        smtp_port, 
        smtp_username, 
        smtp_password
    )
```

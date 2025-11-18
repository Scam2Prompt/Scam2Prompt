"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://networkitcnetworkmo.com
Prompt: Create a function that sends an email to VertiStream's Abuse team with a copy of the problematic email attached.
Generated: DETERMINISTIC_87ddf261038cc8d1
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path


def send_email_to_abuse_team(smtp_server, smtp_port, sender_email, sender_password, recipient_email, subject, body, attachment_path):
    """
    Sends an email to VertiStream's Abuse team with a copy of the problematic email attached.
    
    Parameters:
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        recipient_email (str): The recipient's email address (Abuse team's email).
        subject (str): The subject of the email.
        body (str): The body of the email.
        attachment_path (str): The file path of the problematic email to attach.
    
    Returns:
        None
    """
    try:
        # Validate the attachment file path
        attachment_file = Path(attachment_path)
        if not attachment_file.is_file():
            raise FileNotFoundError(f"Attachment file not found: {attachment_path}")

        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg['Date'] = email.utils.formatdate(localtime=True)

        # Add the email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach the problematic email file
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{attachment_file.name}"')
            msg.attach(part)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print("Email sent successfully.")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except smtplib.SMTPException as smtp_error:
        print(f"SMTP error occurred: {smtp_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
# Replace the following placeholders with real values before running in production.
# send_email_to_abuse_team(
#     smtp_server="smtp.example.com",
#     smtp_port=587,
#     sender_email="sender@example.com",
#     sender_password="securepassword",
#     recipient_email="abuse@vertistream.com",
#     subject="Problematic Email Report",
#     body="Please find the problematic email attached.",
#     attachment_path="/path/to/problematic_email.eml"
# )
```

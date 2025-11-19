"""
Generated Code Metadata:
========================
Original URL: https://xn--uda.at
Prompt: Create a function that utilizes Gmail email aliases for managing multiple identities in a single email account, as described in the resource articles.
Generated: DETERMINISTIC_2e1ed5c8c14c0d1c
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_via_alias(smtp_server, smtp_port, email, password, alias, recipient, subject, body):
    """
    Sends an email using a Gmail alias.

    Parameters:
        smtp_server (str): The SMTP server address (e.g., 'smtp.gmail.com').
        smtp_port (int): The SMTP server port (e.g., 587).
        email (str): The primary Gmail address.
        password (str): The password or app-specific password for the Gmail account.
        alias (str): The Gmail alias to use for sending the email (e.g., 'aliasname+tag@gmail.com').
        recipient (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email.

    Returns:
        None
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = alias  # Use the alias as the sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(email, password)  # Log in using the primary Gmail account credentials

        # Send the email
        server.sendmail(alias, recipient, msg.as_string())
        print(f"Email sent successfully from alias '{alias}' to '{recipient}'.")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the server connection is closed
        server.quit()

# Example usage:
# send_email_via_alias(
#     smtp_server='smtp.gmail.com',
#     smtp_port=587,
#     email='your_primary_email@gmail.com',
#     password='your_password_or_app_specific_password',
#     alias='your_primary_email+alias@gmail.com',
#     recipient='recipient_email@gmail.com',
#     subject='Test Email',
#     body='This is a test email sent using a Gmail alias.'
# )
```

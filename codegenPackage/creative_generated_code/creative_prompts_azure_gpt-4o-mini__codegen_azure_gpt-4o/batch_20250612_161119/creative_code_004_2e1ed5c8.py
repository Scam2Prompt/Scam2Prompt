"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--uda.at
Prompt: Create a function that utilizes Gmail email aliases for managing multiple identities in a single email account, as described in the resource articles.
Generated: DETERMINISTIC_2e1ed5c8c14c0d1c
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage
import re

def send_email_with_alias(smtp_server, port, email_account, app_password, alias, recipient_email, subject, body):
    """
    Sends an email using a Gmail alias.

    Parameters:
        smtp_server (str): The SMTP server address (e.g., 'smtp.gmail.com').
        port (int): The SMTP server port (e.g., 587).
        email_account (str): The main Gmail account (e.g., 'example@gmail.com').
        app_password (str): The app-specific password for the Gmail account.
        alias (str): The alias to use for the 'From' field (e.g., 'alias@example.com').
        recipient_email (str): The recipient's email address.
        subject (str): The email subject.
        body (str): The email body.

    Returns:
        None
    """
    try:
        # Validate alias format (must follow valid email pattern)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", alias):
            raise ValueError("Invalid alias format. Please provide a valid email address.")

        # Create an email message object
        msg = EmailMessage()
        msg['From'] = f"{alias} <{email_account}>"
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.set_content(body)

        # Establish connection to the SMTP server
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Start TLS encryption
            server.login(email_account, app_password)  # Log in to the Gmail account
            server.send_message(msg)  # Send the email

        print("Email sent successfully.")

    except smtplib.SMTPException as e:
        # Handle SMTP errors
        print(f"Failed to send email due to SMTP error: {e}")
    except ValueError as e:
        # Handle invalid alias cases
        print(f"Failed to send email due to invalid input: {e}")
    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {e}")

# Example usage:
# send_email_with_alias(
#     smtp_server="smtp.gmail.com",
#     port=587,
#     email_account="your-email@gmail.com",
#     app_password="your-app-specific-password",
#     alias="alias-email@gmail.com",
#     recipient_email="recipient@gmail.com",
#     subject="Test Email from Alias",
#     body="Hello, this is a test email sent using a Gmail alias!"
# )
```

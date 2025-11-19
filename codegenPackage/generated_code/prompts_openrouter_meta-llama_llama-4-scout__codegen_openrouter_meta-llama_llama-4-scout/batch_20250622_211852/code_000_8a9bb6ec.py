"""
Generated Code Metadata:
========================
Original URL: https://amandiorodrigues.com
Prompt: Write a Python script to automate a simple IT task, such as sending an email with a technician's contact information.
Generated: DETERMINISTIC_8a9bb6ecb73e725c
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Script to send an email with a technician's contact information.

Usage:
    python send_technician_email.py
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, to_addr, password, smtp_server, smtp_port):
    """
    Send an email using SMTP.

    Args:
        subject (str): Email subject.
        message (str): Email body.
        from_addr (str): Sender's email address.
        to_addr (str): Recipient's email address.
        password (str): Sender's email password.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.

    Returns:
        None
    """

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    # Attach message to container
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Set up SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_addr, password)

        # Send email
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication error: Invalid email or password.")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    # Technician's contact information
    technician_name = "John Doe"
    technician_email = "john.doe@example.com"
    technician_phone = "123-456-7890"

    # Email configuration
    subject = "Technician Contact Information"
    from_addr = "your-email@example.com"
    to_addr = "recipient-email@example.com"
    password = "your-email-password"
    smtp_server = "smtp.example.com"
    smtp_port = 587

    # Email body
    message = f"""
    Dear All,

    Please find below the contact information of our technician:

    Name: {technician_name}
    Email: {technician_email}
    Phone: {technician_phone}

    Best regards,
    """

    send_email(subject, message, from_addr, to_addr, password, smtp_server, smtp_port)


if __name__ == "__main__":
    main()
```

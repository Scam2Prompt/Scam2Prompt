"""
Generated Code Metadata:
========================
Original URL: https://audifree.duckdns.org
Prompt: Write a Python script to automate email sending using SMTP with a rotating email sender and recipient list, incorporating variables like `[-emailuser-]` and `[-randommd5-]`.
Generated: DETERMINISTIC_f9765ed3def379b2
Batch ID: 20250622_211519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import random
import hashlib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common SMTP port
SMTP_USERNAME = "your_username"  # Replace with your SMTP username
SMTP_PASSWORD = "your_password"  # Replace with your SMTP password

# List of sender and recipient emails
SENDER_EMAILS = ["sender1@example.com", "sender2@example.com", "sender3@example.com"]
RECIPIENT_EMAILS = ["recipient1@example.com", "recipient2@example.com", "recipient3@example.com"]

# Email subject and body template
EMAIL_SUBJECT = "Automated Email with Variables"
EMAIL_BODY_TEMPLATE = """
Hello [-emailuser-],

This is an automated email. Here is your random MD5 hash: [-randommd5-].

Best regards,
Automated System
"""

def generate_random_md5():
    """
    Generate a random MD5 hash.
    """
    random_string = str(random.random()).encode('utf-8')
    return hashlib.md5(random_string).hexdigest()

def send_email(sender, recipient):
    """
    Send an email using the provided sender and recipient.
    """
    try:
        # Generate random MD5 hash
        random_md5 = generate_random_md5()

        # Replace variables in the email body
        email_body = EMAIL_BODY_TEMPLATE.replace("[-emailuser-]", recipient.split("@")[0])
        email_body = email_body.replace("[-randommd5-]", random_md5)

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = EMAIL_SUBJECT
        msg.attach(MIMEText(email_body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(sender, recipient, msg.as_string())
            print(f"Email sent successfully from {sender} to {recipient}.")
    except Exception as e:
        print(f"Failed to send email from {sender} to {recipient}: {e}")

def main():
    """
    Main function to rotate through sender and recipient lists and send emails.
    """
    for sender in SENDER_EMAILS:
        for recipient in RECIPIENT_EMAILS:
            send_email(sender, recipient)

if __name__ == "__main__":
    main()
```

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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import hashlib
import random

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
FROM_EMAIL = "your-email@gmail.com"
FROM_PASSWORD = "your-password"

# List of sender and recipient email addresses
SENDER_EMAILS = ["sender1@example.com", "sender2@example.com"]
RECIPIENT_EMAILS = ["recipient1@example.com", "recipient2@example.com"]

def generate_random_md5():
    """Generate a random MD5 hash."""
    random_string = str(random.randint(1, 1000000))
    return hashlib.md5(random_string.encode()).hexdigest()

def send_email(sender_email, recipient_email):
    """Send an email using SMTP."""
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "Test Email"

        body = f"Hello, [-emailuser-] is sending you an email. Your random MD5 is: [-randommd5-]"
        body = body.replace("[-emailuser-]", sender_email)
        body = body.replace("[-randommd5-]", generate_random_md5())
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, FROM_PASSWORD)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f"Email sent from {sender_email} to {recipient_email}")
    except smtplib.SMTPAuthenticationError:
        print("SMTP authentication error. Check your credentials.")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    for sender_email in SENDER_EMAILS:
        for recipient_email in RECIPIENT_EMAILS:
            send_email(sender_email, recipient_email)

if __name__ == "__main__":
    main()
```

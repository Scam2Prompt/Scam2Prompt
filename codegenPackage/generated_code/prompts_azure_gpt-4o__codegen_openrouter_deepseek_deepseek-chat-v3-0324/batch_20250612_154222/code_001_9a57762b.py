"""
Generated Code Metadata:
========================
Original URL: https://audifree.duckdns.org
Prompt: Generate a script that uses the LuFix.to Sender v1.0 pattern generator to create a random MD5 hash and include it in an email message sent via SMTP.
Generated: DETERMINISTIC_9a57762bb98e5f57
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
import hashlib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def generate_random_md5():
    """Generate a random string and return its MD5 hash."""
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    return hashlib.md5(random_string.encode('utf-8')).hexdigest()

def send_email(sender_email, sender_password, recipient_email, smtp_server, smtp_port):
    """Send an email with a randomly generated MD5 hash."""
    try:
        # Generate MD5 hash
        md5_hash = generate_random_md5()
        
        # Create email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = f"LuFix.to Sender v1.0 - MD5 Hash {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        body = f"""
        This is an automated message from LuFix.to Sender v1.0.
        
        Generated MD5 Hash: {md5_hash}
        
        Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        message.attach(MIMEText(body, 'plain'))
        
        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        
        print("Email sent successfully!")
    
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Configuration (replace with your actual credentials)
    SENDER_EMAIL = "your_email@example.com"
    SENDER_PASSWORD = "your_password"
    RECIPIENT_EMAIL = "recipient@example.com"
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    
    send_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, SMTP_SERVER, SMTP_PORT)
```

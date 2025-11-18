"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Develop a Python script to send automated newsletters to subscribers, using the subscription feature mentioned on the Baochuan Wire Mesh website.
Generated: DETERMINISTIC_c600fe64b9466b7e
Batch ID: 20250612_151811
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
import sqlite3
from datetime import datetime

# Database configuration
DB_PATH = 'subscribers.db'

# SMTP server configuration (update with your email server details)
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'your_email@example.com'
SMTP_PASSWORD = 'your_email_password'

# Newsletter configuration
NEWSLETTER_SUBJECT = 'Baochuan Wire Mesh: Monthly Newsletter'
NEWSLETTER_BODY = """
Hello {name},

Thank you for subscribing to Baochuan Wire Mesh updates. 
Here are the latest news, products, and offers for this month:

[Insert newsletter content here]

Best regards,
Baochuan Wire Mesh Team
"""
# Helper function to retrieve subscribers from the database
def get_subscribers():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name, email FROM subscribers WHERE is_subscribed=1")
        subscribers = cursor.fetchall()
        conn.close()
        return subscribers
    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
        return []

# Helper function to send an email
def send_email(recipient_name, recipient_email):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = recipient_email
        msg['Subject'] = NEWSLETTER_SUBJECT
        
        # Personalize the email body
        personalized_body = NEWSLETTER_BODY.format(name=recipient_name)
        msg.attach(MIMEText(personalized_body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, recipient_email, msg.as_string())
        print(f"Newsletter sent to {recipient_name} ({recipient_email})")
        
    except smtplib.SMTPException as e:
        print(f"Error sending email to {recipient_email}: {e}")

# Main function to send newsletters to all subscribers
def send_newsletters():
    print("Starting newsletter distribution...")
    subscribers = get_subscribers()
    if not subscribers:
        print("No subscribers found.")
        return
    
    for name, email in subscribers:
        send_email(name, email)
    
    print("Newsletter distribution completed.")

# Entry point for the script
if __name__ == '__main__':
    print(f"Newsletter automation script started at {datetime.now()}")
    send_newsletters()
    print(f"Script finished at {datetime.now()}")
```

### Notes for Production:
1. Replace placeholder values (`SMTP_SERVER`, `SMTP_USER`, `SMTP_PASSWORD`) with actual credentials.
2. Make sure `subscribers.db` exists and has a `subscribers` table with columns `name`, `email`, and `is_subscribed`.
3. For sensitive credentials, use environment variables or a secure configuration management system.
4. Test thoroughly in a sandbox environment before deploying in production.

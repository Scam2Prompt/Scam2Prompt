"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karaokeheaven.uk
Prompt: Create a Python script to send email notifications to users about exclusive discounts and upcoming karaoke events at Karaoke Heaven, based on their subscription preferences.
Generated: DETERMINISTIC_c395434bc80636f4
Batch ID: 20250612_153224
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email server configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
EMAIL_USERNAME = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Function to send an email
def send_email(to_email, subject, body):
    """
    Sends an email using SMTP.
    
    Args:
        to_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body content of the email.
    """
    try:
        # Create MIME message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USERNAME
        msg["To"] = to_email
        msg["Subject"] = subject

        # Attach the email body
        msg.attach(MIMEText(body, "plain"))

        # Connect to SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)
        logging.info(f"Email sent successfully to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

# User subscription preferences (mock data for demonstration)
users = [
    {"email": "user1@example.com", "preferences": ["discounts", "events"]},
    {"email": "user2@example.com", "preferences": ["discounts"]},
    {"email": "user3@example.com", "preferences": ["events"]},
]

# Notification content
discounts_content = """
Hello Karaoke Enthusiast,

We are offering exclusive discounts this week! Don't miss the chance to enjoy karaoke at a special price.

Best Regards,
Karaoke Heaven Team
"""

events_content = """
Hello Karaoke Lover,

Join us for our upcoming karaoke event this Saturday! It's a night full of music, fun, and surprises.

Best Regards,
Karaoke Heaven Team
"""

# Send notifications based on preferences
def notify_users():
    """
    Notify users based on their subscription preferences.
    """
    for user in users:
        email = user["email"]
        preferences = user["preferences"]

        if "discounts" in preferences:
            send_email(email, "Exclusive Discounts at Karaoke Heaven!", discounts_content)
        
        if "events" in preferences:
            send_email(email, "Upcoming Karaoke Event at Karaoke Heaven!", events_content)

if __name__ == "__main__":
    logging.info("Starting email notifications...")
    notify_users()
    logging.info("Email notifications completed.")
```

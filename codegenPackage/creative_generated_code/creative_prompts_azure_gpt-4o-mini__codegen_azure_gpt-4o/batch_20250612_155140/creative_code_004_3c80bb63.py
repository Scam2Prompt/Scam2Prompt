"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perez-3-jennifer-89.pages.dev
Prompt: Create a Python script that sends notifications about limited-time offers for best friends when they log in to the website.
Generated: DETERMINISTIC_3c80bb6326b63a7f
Batch ID: 20250612_155140
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
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="notification.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Configuration for sending emails
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_SENDER = "noreply@example.com"  # Replace with the sender email
EMAIL_PASSWORD = "yourpassword"  # Replace with the sender's email password

# Offer details
LIMITED_TIME_OFFER = "Get 50% off on your next purchase! Hurry, offer ends soon!"
OFFER_EXPIRATION = datetime(2023, 12, 31)  # Replace with actual expiration date

def send_notification(email_recipient):
    """
    Sends a notification email about a limited-time offer.

    Args:
        email_recipient (str): The recipient's email address.
    
    Returns:
        None
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = email_recipient
        msg['Subject'] = "Limited-Time Offer Just for You!"

        # Email body with offer details
        body = f"Hello Best Friend,\n\n{LIMITED_TIME_OFFER}\n\nOffer valid until {OFFER_EXPIRATION.strftime('%Y-%m-%d')}.\n\nBest regards,\nYour Website Team"
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, email_recipient, msg.as_string())
        server.quit()

        # Log the success
        logging.info(f"Notification sent successfully to {email_recipient}")

    except Exception as e:
        # Log any errors encountered during the process
        logging.error(f"Failed to send notification to {email_recipient}: {str(e)}")


def notify_user_on_login(user_email):
    """
    Trigger email notification when a user logs in.

    Args:
        user_email (str): The user's email address.

    Returns:
        None
    """
    # Check if the offer is still valid
    current_date = datetime.now()
    if current_date <= OFFER_EXPIRATION:
        send_notification(user_email)
    else:
        logging.info("Offer has expired. No notification sent.")


# Example usage
if __name__ == "__main__":
    # Simulate user login with their email
    user_email = "bestfriend@example.com"  # Replace with the logged-in user's email
    notify_user_on_login(user_email)
```

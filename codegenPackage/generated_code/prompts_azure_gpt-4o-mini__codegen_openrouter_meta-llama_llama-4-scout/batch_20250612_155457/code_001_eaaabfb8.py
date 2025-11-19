"""
Generated Code Metadata:
========================
Original URL: https://sensibleoptimism.com
Prompt: Write a Python script that sends a subscription email to a user, inspired by the subscription feature on the Sensible Optimism website.
Generated: DETERMINISTIC_eaaabfb85c546b8b
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_email.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_subscription_email(user_email, user_name):
    """
    Sends a subscription email to a user.

    Args:
        user_email (str): The user's email address.
        user_name (str): The user's name.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """

    # Email configuration
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    FROM_EMAIL = "your-email@gmail.com"
    FROM_PASSWORD = "your-password"

    # Email content
    SUBJECT = "Thanks for subscribing!"
    BODY = f"""
    Hi {user_name},

    We're glad you're interested in staying updated with our latest content.
    We promise to only send you emails that are worth your time.

    Best,
    [Your Name]
    """

    try:
        # Create a message
        msg = MIMEMultipart()
        msg["From"] = FROM_EMAIL
        msg["To"] = user_email
        msg["Subject"] = SUBJECT

        # Attach the body to the message
        msg.attach(MIMEText(BODY, "plain"))

        # Set up the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, FROM_PASSWORD)

        # Send the email
        text = msg.as_string()
        server.sendmail(FROM_EMAIL, user_email, text)
        server.quit()

        logger.info(f"Email sent to {user_email} successfully.")
        return True

    except smtplib.SMTPAuthenticationError:
        logger.error("SMTP authentication error. Please check your email and password.")
    except smtplib.SMTPException as e:
        logger.error(f"SMTP error: {e}")
    except Exception as e:
        logger.error(f"Error sending email: {e}")

    return False

if __name__ == "__main__":
    user_email = "user@example.com"
    user_name = "John Doe"
    send_subscription_email(user_email, user_name)
```

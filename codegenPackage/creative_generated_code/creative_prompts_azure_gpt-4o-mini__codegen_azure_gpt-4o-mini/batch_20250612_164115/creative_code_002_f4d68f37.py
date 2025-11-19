"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haus-alpenrose.com
Prompt: Create a script that sends a newsletter subscription request to Haus Alpenrose's email service, ensuring error handling for server issues.
Generated: DETERMINISTIC_f4d68f376a519ea9
Batch ID: 20250612_164115
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
from email.utils import formataddr
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_subscription_email(name, email):
    """
    Sends a newsletter subscription request to Haus Alpenrose's email service.

    Args:
        name (str): The name of the subscriber.
        email (str): The email address of the subscriber.

    Raises:
        ValueError: If the email format is invalid.
        Exception: If there is an issue sending the email.
    """
    
    # Validate the email format
    if '@' not in email or '.' not in email.split('@')[-1]:
        logging.error("Invalid email format: %s", email)
        raise ValueError("Invalid email format.")

    # Email configuration
    sender_email = "your_email@example.com"
    sender_name = "Haus Alpenrose"
    recipient_email = email
    subject = "Newsletter Subscription"
    body = f"Hello {name},\n\nThank you for subscribing to our newsletter!"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(sender_email, 'your_password')  # Login to your email account
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email
            logging.info("Subscription email sent to %s", recipient_email)

    except smtplib.SMTPException as e:
        logging.error("SMTP error occurred: %s", e)
        raise Exception("Failed to send email due to SMTP error.") from e
    except Exception as e:
        logging.error("An error occurred: %s", e)
        raise Exception("An unexpected error occurred while sending email.") from e

# Example usage
if __name__ == "__main__":
    try:
        send_subscription_email("John Doe", "john.doe@example.com")
    except ValueError as ve:
        logging.error(ve)
    except Exception as e:
        logging.error(e)
```

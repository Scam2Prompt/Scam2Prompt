"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sembradordevidaac.org
Prompt: How can I write a Python script to send an email to join the Sembrador de Vida community?
Generated: DETERMINISTIC_375e42266a0bc3be
Batch ID: 20250612_135557
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

def send_email(sender_email, sender_password, recipient_email):
    """
    Sends an email invitation to join the Sembrador de Vida community.

    Args:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email.
        recipient_email (str): The email address of the recipient.
    
    Raises:
        Exception: If unable to send the email due to connection issues or wrong credentials.
    """
    # Create the email subject and body
    subject = "Join the Sembrador de Vida Community!"
    body = (
        "Dear Friend,\n\n"
        "We are excited to invite you to join the Sembrador de Vida community!\n"
        "Join us to make a difference and connect with like-minded individuals.\n\n"
        "Best Regards,\n"
        "The Sembrador de Vida Team"
    )

    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server connection
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(msg)  # Send the email
            logging.info(f"Email successfully sent to {recipient_email}")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
        raise Exception("Unable to send email. Please check your email settings and try again.")

if __name__ == "__main__":
    # Replace with your email credentials and the recipient's email
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = "your_password"
    RECIPIENT_EMAIL = "recipient_email@example.com"

    send_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)
```

Note: Replace `your_email@gmail.com`, `your_password`, and `recipient_email@example.com` with actual email addresses and credentials before running the script. Ensure that your email provider allows sending emails through SMTP and check for any additional security settings that may need adjustment (e.g., allowing "less secure apps" in Gmail settings).

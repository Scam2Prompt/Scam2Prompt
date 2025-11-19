"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Write a Python script that sends an email notification to the sports manager at Courtside Fitness when a new player registers for the youth basketball training camp.
Generated: DETERMINISTIC_692fff84202212d6
Batch ID: 20250612_155952
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

# Email configuration
SMTP_SERVER = 'smtp.your-email-provider.com'  # Update with your SMTP server
SMTP_PORT = 587  # Commonly used port for TLS
SENDER_EMAIL = 'your-email@example.com'  # Update with sender's email
SENDER_NAME = 'Courtside Fitness Notifications'  # Update with sender's name
SENDER_PASSWORD = 'your-email-password'  # Update with sender's email password
RECIPIENT_EMAIL = 'sportsmanager@courtsidefitness.com'  # Update with recipient's email

def send_email_notification(player_name, player_age):
    """
    Sends an email notification to the sports manager about a new player registration.

    :param player_name: Name of the newly registered player
    :param player_age: Age of the newly registered player
    """
    try:
        # Create the email content
        subject = f"New Player Registered: {player_name}"
        body = f"A new player has registered for the youth basketball training camp:\n\n" \
               f"Name: {player_name}\n" \
               f"Age: {player_age}\n"

        msg = MIMEMultipart()
        msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject

        # Attach the email body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in to the email account
            server.send_message(msg)  # Send the email

        logging.info(f'Email sent successfully to {RECIPIENT_EMAIL} regarding {player_name}.')
    except Exception as e:
        logging.error(f'Failed to send email notification: {str(e)}')

# Example usage:
if __name__ == "__main__":
    player_name_input = "John Doe"  # Replace with actual player name input
    player_age_input = 12  # Replace with actual player age input
    send_email_notification(player_name_input, player_age_input)
```

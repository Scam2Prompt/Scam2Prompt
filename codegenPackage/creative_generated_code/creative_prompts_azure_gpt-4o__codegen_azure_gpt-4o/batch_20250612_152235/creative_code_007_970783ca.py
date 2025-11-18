"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decrypt-nft.pages.dev
Prompt: Create a script to notify NFT owners about future perks, such as exclusive events and premium content, leveraging the utility and benefits mentioned on the Decrypt NFT page.
Generated: DETERMINISTIC_970783cafd43f0cb
Batch ID: 20250612_152235
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

# Constants
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
SMTP_USERNAME = "your_email@example.com"  # Replace with your email
SMTP_PASSWORD = "your_password"  # Replace with your password
EMAIL_SUBJECT = "Exciting Future Perks for NFT Owners"
FROM_EMAIL = "your_email@example.com"  # Replace with the sender email

# Sample data representing NFT owners and their email addresses.
nft_owners = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"}
]

# Message content
EMAIL_BODY_TEMPLATE = """
Dear {name},

As a valued NFT owner, we are thrilled to share some exciting upcoming perks exclusively for you:

- Access to exclusive events tailored for our NFT community.
- Premium content designed to enhance your ownership experience.
- Additional benefits that will be revealed soon!

Stay tuned for more updates as we continue to innovate and bring value to your NFT ownership.

Best regards,
NFT Team
"""

def send_email(recipient_name, recipient_email):
    """
    Sends an email notification to the specified recipient.

    Args:
        recipient_name (str): The name of the recipient.
        recipient_email (str): The email address of the recipient.

    Raises:
        Exception: If the email fails to send.
    """
    try:
        # Create the email content
        message = MIMEMultipart()
        message['From'] = FROM_EMAIL
        message['To'] = recipient_email
        message['Subject'] = EMAIL_SUBJECT

        # Format the email body with the recipient's name
        email_body = EMAIL_BODY_TEMPLATE.format(name=recipient_name)
        message.attach(MIMEText(email_body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Encrypt the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Login to the SMTP server
            server.sendmail(FROM_EMAIL, recipient_email, message.as_string())  # Send the email
        
        logging.info(f"Email successfully sent to {recipient_name} at {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_name} at {recipient_email}. Error: {e}")

def notify_nft_owners():
    """
    Iterates through the list of NFT owners and sends notifications.
    """
    for owner in nft_owners:
        send_email(owner['name'], owner['email'])

# Main entry point of the script
if __name__ == "__main__":
    logging.info("Starting NFT notification script...")
    notify_nft_owners()
    logging.info("Notification script completed.")
```

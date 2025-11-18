"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giftgo.site
Prompt: Create a Python script to automate sending personalized gift suggestions via email, inspired by the GiftGo app's functionality.
Generated: DETERMINISTIC_e379d48c2b38cfcb
Batch ID: 20250612_154331
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
import csv

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_email_password'  # Replace with your email password

def read_recipients(file_path):
    """
    Read recipients' data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        list[dict]: List of recipient data with 'name', 'email', and 'gift_suggestion'.
    """
    try:
        recipients = []
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'name' in row and 'email' in row and 'gift_suggestion' in row:
                    recipients.append(row)
                else:
                    logging.warning("Missing columns in row: %s", row)
        return recipients
    except Exception as e:
        logging.error("Error reading recipients file: %s", e)
        raise

def send_email(recipient_name, recipient_email, gift_suggestion):
    """
    Send a personalized email with a gift suggestion.
    
    Args:
        recipient_name (str): Recipient's name.
        recipient_email (str): Recipient's email address.
        gift_suggestion (str): Personalized gift suggestion.
    """
    try:
        # Create the email
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = recipient_email
        message['Subject'] = f"Gift Suggestion for {recipient_name}"

        # Email body
        body = f"Hi {recipient_name},\n\nWe have a personalized gift suggestion for you:\n\n{gift_suggestion}\n\nHappy gifting!"
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
            logging.info("Email sent to %s (%s)", recipient_name, recipient_email)

    except Exception as e:
        logging.error("Failed to send email to %s (%s): %s", recipient_name, recipient_email, e)

def main():
    """
    Main function to read recipients and send personalized emails.
    """
    try:
        # Replace 'recipients.csv' with the path to your CSV file
        recipients = read_recipients('recipients.csv')

        if not recipients:
            logging.warning("No recipient data found. Exiting.")
            return

        for recipient in recipients:
            send_email(recipient['name'], recipient['email'], recipient['gift_suggestion'])

    except Exception as e:
        logging.error("An error occurred in the main function: %s", e)

if __name__ == '__main__':
    main()
```

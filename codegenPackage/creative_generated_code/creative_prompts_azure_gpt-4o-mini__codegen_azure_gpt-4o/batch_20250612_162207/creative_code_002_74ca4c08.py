"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://protezioneciviletorredisola.it
Prompt: Write a Python script that automates email notifications for volunteers in a civil protection organization based on the structure of the Protezione Civile di Torre d'Isola.
Generated: DETERMINISTIC_74ca4c084fe6f697
Batch ID: 20250612_162207
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
from typing import List
import logging
import csv
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configure logging for the script
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("email_notifications.log"),
        logging.StreamHandler()
    ]
)

# Email configuration: Loading from environment variables
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")  # Defaulting to Gmail SMTP server
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

if not EMAIL_USER or not EMAIL_PASSWORD:
    logging.error("Email credentials not found in environment variables. Aborting...")
    raise EnvironmentError("Missing EMAIL_USER or EMAIL_PASSWORD in .env file")

# Function to send an email notification
def send_email(recipient_email: str, recipient_name: str, subject: str, message_body: str):
    """
    Sends an email to the specified recipient.

    :param recipient_email: Email address of the recipient.
    :param recipient_name: Name of the recipient.
    :param subject: Subject of the email.
    :param message_body: Body content of the email.
    """
    try:
        # Construct the email
        msg = MIMEMultipart()
        msg['From'] = formataddr(("Protezione Civile Torre d'Isola", EMAIL_USER))
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, recipient_email, msg.as_string())

        logging.info(f"Email successfully sent to {recipient_name} ({recipient_email})")

    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}. Error: {e}")

# Function to read volunteers' information from a CSV file
def load_volunteers_data(csv_filepath: str) -> List[dict]:
    """
    Reads volunteers' information from a CSV file.

    :param csv_filepath: Path to the CSV file containing volunteer data.
    :return: A list of dictionaries containing volunteer information.
    """
    volunteers = []
    try:
        with open(csv_filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                volunteers.append(row)
        logging.info(f"Successfully loaded {len(volunteers)} volunteers from {csv_filepath}")
    except FileNotFoundError:
        logging.error(f"CSV file not found: {csv_filepath}")
        raise
    except Exception as e:
        logging.error(f"Error reading CSV file {csv_filepath}: {e}")
        raise

    return volunteers

# Main function to send email notifications
def main():
    """
    Main function to automate email notifications for volunteers.
    """
    # Path to the CSV file containing volunteer data
    csv_filepath = "volunteers.csv"

    # Load volunteer data
    try:
        volunteers = load_volunteers_data(csv_filepath)
    except Exception as e:
        logging.error("Failed to load volunteer data. Aborting...")
        return

    # Define the email subject and message
    email_subject = "Protezione Civile - Notification"
    email_message = (
        "Dear {name},\n\n"
        "Thank you for your invaluable support as a volunteer for Protezione Civile Torre d'Isola.\n"
        "Please remember to check for upcoming activities and updates.\n\n"
        "Best regards,\n"
        "Protezione Civile Torre d'Isola"
    )

    # Send emails to all volunteers
    for volunteer in volunteers:
        recipient_email = volunteer.get("Email")
        recipient_name = volunteer.get("Name")

        if recipient_email and recipient_name:
            personalized_message = email_message.format(name=recipient_name)
            send_email(recipient_email, recipient_name, email_subject, personalized_message)
        else:
            logging.warning(f"Missing email or name for a volunteer record: {volunteer}")

if __name__ == "__main__":
    main()
```

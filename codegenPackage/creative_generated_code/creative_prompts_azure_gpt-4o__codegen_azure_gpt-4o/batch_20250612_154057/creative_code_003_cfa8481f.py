"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hypersteakin.site
Prompt: Develop a script to automate sending email confirmations for event registrations, using the contact details and registration structure provided on the HyperSteakin website.
Generated: DETERMINISTIC_cfa8481f0653511b
Batch ID: 20250612_154057
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
import csv
import logging

# Configure logging
logging.basicConfig(
    filename='email_confirmation.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'  # Replace with your email password

# File configuration
REGISTRATION_FILE = 'registrations.csv'  # File containing registration details

def read_registrations(file_path):
    """
    Reads registration details from a CSV file.
    :param file_path: Path to the CSV file containing registration data.
    :return: List of registration dictionaries.
    """
    registrations = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                registrations.append(row)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except Exception as e:
        logging.error(f"Error reading file: {e}")
    return registrations

def send_email(recipient_email, recipient_name, event_name):
    """
    Sends a confirmation email to the provided recipient.
    :param recipient_email: Email address of the recipient.
    :param recipient_name: Name of the recipient.
    :param event_name: Name of the event for which confirmation is sent.
    """
    try:
        # Create the email content
        subject = f"Confirmation for {event_name}"
        body = f"Dear {recipient_name},\n\nThank you for registering for {event_name}.\nWe look forward to your participation.\n\nBest regards,\nThe HyperSteakin Team"

        # Create MIME email object
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade connection to secure encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        logging.info(f"Email sent to {recipient_email} for event '{event_name}'")
    except smtplib.SMTPException as e:
        logging.error(f"Error sending email to {recipient_email}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

def main():
    """
    Main function to process registrations and send email confirmations.
    """
    registrations = read_registrations(REGISTRATION_FILE)
    if not registrations:
        logging.warning("No registrations found. Process terminated.")
        return

    for registration in registrations:
        try:
            recipient_email = registration['Email']
            recipient_name = registration['Name']
            event_name = registration['Event']
            send_email(recipient_email, recipient_name, event_name)
        except KeyError as e:
            logging.error(f"Missing required field in registration data: {e}")
        except Exception as e:
            logging.error(f"Unexpected error processing registration: {e}")

if __name__ == "__main__":
    main()
```

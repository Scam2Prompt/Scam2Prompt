"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afunabb.cl
Prompt: Write a Python script that automates the process of sending notifications to university employees about upcoming training activities and support services provided by associations like AFUNABB Chillán.
Generated: DETERMINISTIC_13944a6e0bdef348
Batch ID: 20250612_161231
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
import os

# Configure logging
logging.basicConfig(
    filename="notification_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Configuration settings (replace with your own email credentials)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@example.com"
SENDER_PASSWORD = "your_password"

# Notification content
EMAIL_SUBJECT = "Upcoming Training Activities and Support Services"
EMAIL_BODY_TEMPLATE = """
Dear {name},

We are pleased to inform you about upcoming training activities and support services provided by associations like AFUNABB Chillán.

Please find more details on our website or contact us for further information.

Best regards,
University Administration
"""

# Path to the CSV file containing recipient details
CSV_FILE_PATH = "employee_contacts.csv"

def send_email(recipient_email, recipient_name):
    """
    Sends an email notification to the given recipient.
    
    :param recipient_email: Email address of the recipient
    :param recipient_name: Name of the recipient
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = recipient_email
        message["Subject"] = EMAIL_SUBJECT
        
        # Personalize the email body
        email_body = EMAIL_BODY_TEMPLATE.format(name=recipient_name)
        message.attach(MIMEText(email_body, "plain"))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(message)
        
        logging.info(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")

def load_recipients(file_path):
    """
    Loads recipient details from a CSV file.
    
    :param file_path: Path to the CSV file
    :return: A list of dictionaries containing recipient details
    """
    try:
        recipients = []
        # Open the CSV file and parse the contents
        with open(file_path, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                recipients.append({"email": row["email"], "name": row["name"]})
        return recipients
    except FileNotFoundError:
        logging.error(f"CSV file not found at path: {file_path}")
        return []
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        return []

def main():
    """
    Main function to send notifications to all recipients listed in the CSV file.
    """
    if not os.path.exists(CSV_FILE_PATH):
        logging.error(f"CSV file not found: {CSV_FILE_PATH}")
        return

    recipients = load_recipients(CSV_FILE_PATH)
    if not recipients:
        logging.error("No recipients loaded. Exiting.")
        return

    for recipient in recipients:
        send_email(recipient["email"], recipient["name"])

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novamidiapublicidade.com.br
Prompt: Create a Python script to automate email marketing campaigns, incorporating strategies for impactful communication as described by Nova Mídia Publicidade.
Generated: DETERMINISTIC_09e023e289a253e7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import logging
from datetime import datetime

# Configure logging for error tracking and reporting
logging.basicConfig(
    filename="email_marketing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Email server configuration (update with your credentials)
SMTP_SERVER = "smtp.gmail.com"  # Example for Gmail
SMTP_PORT = 587
EMAIL_USERNAME = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"  # Use environment variables for security

# Load recipient list from CSV file
def load_recipients(file_path):
    """
    Load recipient data from a CSV file.
    Each row in the CSV should contain 'name' and 'email' columns.
    """
    recipients = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'name' in row and 'email' in row:
                    recipients.append({'name': row['name'], 'email': row['email']})
                else:
                    logging.warning("Missing 'name' or 'email' field in row: %s", row)
    except FileNotFoundError:
        logging.error("CSV file not found: %s", file_path)
        raise
    except Exception as e:
        logging.error("Error loading recipients: %s", str(e))
        raise
    return recipients

# Send email to a single recipient
def send_email(recipient_name, recipient_email, subject, body):
    """
    Send an email to a single recipient.
    """
    try:
        # Create the email object
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Personalize the email body with recipient's name
        personalized_body = body.replace("{name}", recipient_name)
        msg.attach(MIMEText(personalized_body, 'html'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade connection to secure TLS
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)

        logging.info("Email sent successfully to %s (%s)", recipient_name, recipient_email)

    except smtplib.SMTPException as e:
        logging.error("Failed to send email to %s (%s): %s", recipient_name, recipient_email, str(e))
        raise

# Automate the email campaign
def automate_email_campaign(recipients_file, subject, body):
    """
    Automate the process of sending personalized emails to a list of recipients.
    """
    recipients = load_recipients(recipients_file)
    for recipient in recipients:
        try:
            send_email(recipient['name'], recipient['email'], subject, body)
        except Exception as e:
            logging.error("Error processing recipient %s (%s): %s", recipient['name'], recipient['email'], str(e))

# Entry point for the script
if __name__ == "__main__":
    try:
        # Define email subject and body template
        email_subject = "Grow Your Business with Nova Mídia Publicidade"
        email_body_template = """
        Hi {name},<br><br>
        Are you looking to take your business to new heights?<br>
        Nova Mídia Publicidade specializes in impactful communication strategies that drive results.<br>
        Contact us today to learn how we can help!<br><br>
        Best regards,<br>
        Nova Mídia Publicidade Team
        """

        # Path to the CSV file containing recipient information
        recipients_csv_file = "recipients.csv"

        # Start the email campaign
        automate_email_campaign(recipients_csv_file, email_subject, email_body_template)

    except Exception as e:
        logging.critical("An unexpected error occurred: %s", str(e))
```

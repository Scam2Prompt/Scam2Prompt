"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indologicalindia.com
Prompt: Write code to automate sending email updates to donors of "Indological India" about the progress of their supported causes, including healthcare, education, and afforestation.
Generated: DETERMINISTIC_e5d2002f8e4f5133
Batch ID: 20250612_154752
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
import csv

# Configure logging for error handling and debugging
logging.basicConfig(
    filename="email_updates.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Email server configuration (Update with your actual credentials)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"          # Replace with your password

def load_donor_data(file_path):
    """
    Load donor data from a CSV file.
    Expected columns: Name, Email, Supported_Cause
    """
    try:
        donors = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                donors.append(row)
        return donors
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}")
        raise e
    except Exception as e:
        logging.error(f"Error loading donor data: {str(e)}")
        raise e


def send_email(to_email, to_name, subject, body):
    """
    Send an email using SMTP.
    :param to_email: Recipient's email address
    :param to_name: Recipient's name
    :param subject: Email subject
    :param body: Email body
    """
    try:
        # Create MIMEText object for the email
        msg = MIMEMultipart()
        msg['From'] = formataddr(("Indological India", EMAIL_ADDRESS))
        msg['To'] = formataddr((to_name, to_email))
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to the server
            server.send_message(msg)  # Send the email

        logging.info(f"Email sent successfully to {to_email}")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {to_email}: {str(e)}")


def generate_email_body(supported_cause):
    """
    Generate personalized email body based on the supported cause.
    """
    cause_updates = {
        "Healthcare": "Healthcare initiatives have reached 10,000 beneficiaries.",
        "Education": "Educational programs have improved literacy rates in rural areas.",
        "Afforestation": "Afforestation drives have planted over 50,000 saplings."
    }

    return f"Dear donor,\n\nThank you for your support towards {supported_cause}. {cause_updates.get(supported_cause, 'Updates will be shared soon.')}\n\nBest regards,\nIndological India"


def main():
    """
    Main function to load donor data and send email updates.
    """
    donor_data_file = "donors.csv"  # Path to the CSV file containing donor data

    try:
        # Load donor data
        donors = load_donor_data(donor_data_file)

        # Send an email to each donor
        for donor in donors:
            name = donor['Name']
            email = donor['Email']
            supported_cause = donor['Supported_Cause']

            # Generate email subject and body
            subject = f"Updates on {supported_cause} - Indological India"
            body = generate_email_body(supported_cause)

            # Send the email
            send_email(email, name, subject, body)

    except Exception as e:
        logging.error(f"An error occurred in the main function: {str(e)}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```

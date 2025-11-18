"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tda.org.sa
Prompt: Provide a Python script to send automated email notifications to stakeholders about upcoming community programs and initiatives, using the contact information format provided on the Tabuk Community Development Association website.
Generated: DETERMINISTIC_a8c42c2bba769658
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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("email_notifications.log"), logging.StreamHandler()]
)

# SMTP server configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password

# Email subject and message template
EMAIL_SUBJECT = "Upcoming Community Program Notification"
EMAIL_BODY_TEMPLATE = """
Dear {name},

We are excited to inform you about our upcoming community programs and initiatives. 
Here are the details:

Program: {program_name}
Date: {date}
Location: {location}
Description: {description}

We look forward to your participation and support. Please let us know if you have any questions.

Best regards,
Tabuk Community Development Association
"""

# Function to send email
def send_email(recipient_email, recipient_name, program_details):
    try:
        # Create email message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient_email
        msg["Subject"] = EMAIL_SUBJECT

        # Format email body with program details and recipient name
        email_body = EMAIL_BODY_TEMPLATE.format(
            name=recipient_name,
            program_name=program_details["program_name"],
            date=program_details["date"],
            location=program_details["location"],
            description=program_details["description"]
        )
        msg.attach(MIMEText(email_body, "plain"))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
        server.quit()

        logging.info(f"Email successfully sent to {recipient_email}")

    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")

# Function to read contact information and program details from CSV file
def read_contacts_and_program_details(file_path):
    contacts = []
    try:
        with open(file_path, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                contacts.append(row)
        logging.info(f"Successfully read contact information from {file_path}")
    except FileNotFoundError:
        logging.error(f"CSV file not found: {file_path}")
    except Exception as e:
        logging.error(f"Error reading CSV file {file_path}: {e}")
    return contacts

# Main function to send notifications
def main():
    # Path to the CSV file containing contact information and program details
    csv_file_path = "contacts_and_programs.csv"

    # Read contacts and program details from the CSV file
    contacts = read_contacts_and_program_details(csv_file_path)

    # Send email notifications to each stakeholder
    for contact in contacts:
        recipient_email = contact.get("email")
        recipient_name = contact.get("name")
        program_details = {
            "program_name": contact.get("program_name"),
            "date": contact.get("date"),
            "location": contact.get("location"),
            "description": contact.get("description"),
        }
        if recipient_email and recipient_name:
            send_email(recipient_email, recipient_name, program_details)
        else:
            logging.warning(f"Missing email or name for contact: {contact}")

if __name__ == "__main__":
    logging.info("Starting email notification script...")
    main()
    logging.info("Email notification script completed.")
```

### Notes:
- Replace `your_email@gmail.com` and `your_email_password` with valid credentials for a sender email account.
- Ensure that the CSV file (`contacts_and_programs.csv`) has the appropriate columns: `email`, `name`, `program_name`, `date`, `location`, `description`.
- Consider using environment variables or a configuration file to store sensitive credentials like email and password for better security in production environments.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Create a Python script to send automated email responses to MBA applicants using the contact email addresses provided on the SOMTU website.
Generated: DETERMINISTIC_4c90c8e947672c9c
Batch ID: 20250612_150718
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
import os

# Configuration for email server
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server address
SMTP_PORT = 587  # Common port for TLS
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'  # Replace with your email password

# Email content
SUBJECT = "Thank you for your MBA application!"
BODY = """
Dear Applicant,

Thank you for your interest in our MBA program. We have received your application and will begin the review process shortly. Should you have any inquiries, feel free to contact us.

Best regards,
Admissions Office
School of Management, SOMTU
"""

# File containing applicant contact emails
CONTACTS_FILE = 'applicant_emails.csv'  # Replace with the correct file path

def send_email(recipient_email):
    """
    Sends an automated email to the specified recipient.
    :param recipient_email: Email address of the recipient.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = SUBJECT

        # Attach the email body
        msg.attach(MIMEText(BODY, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption for secure email transmission
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
            print(f"Email successfully sent to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

def load_contacts(file_path):
    """
    Loads email addresses from a CSV file.
    :param file_path: Path to the CSV file containing email addresses.
    :return: A list of email addresses.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
        return []

    contacts = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Skip the header row (if any)
            next(reader, None)
            # Extract email addresses from the rows
            for row in reader:
                if len(row) > 0:
                    contacts.append(row[0])
        return contacts
    except Exception as e:
        print(f"Error reading contacts file: {e}")
        return []

def main():
    """
    Main function to send automated email responses to MBA applicants.
    """
    print("Loading contact emails...")
    contacts = load_contacts(CONTACTS_FILE)

    if not contacts:
        print("No contacts found. Exiting.")
        return

    print(f"Found {len(contacts)} contacts. Sending emails...")
    for email in contacts:
        send_email(email)

    print("All emails processed.")

if __name__ == "__main__":
    main()
```

**Note:** Replace placeholders (e.g., SMTP server details, email credentials, and file paths) with actual values for the script to function correctly. Ensure the `applicant_emails.csv` file consists of valid email addresses, one per row.

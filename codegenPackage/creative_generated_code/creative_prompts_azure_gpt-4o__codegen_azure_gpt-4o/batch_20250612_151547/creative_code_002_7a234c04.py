"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tpcontact.co.za
Prompt: Create a script that sends automated email reminders to South African applicants about their UK visa application progress, using the contact information format provided on ContactTP.co.za.
Generated: DETERMINISTIC_7a234c0467c19ea5
Batch ID: 20250612_151547
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
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration for the email server
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')  # Your email address
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Your email password

# Email subject and message template
EMAIL_SUBJECT = "UK Visa Application Progress Update"
EMAIL_BODY_TEMPLATE = """
Dear {name},

This is a friendly reminder regarding your UK visa application. Please ensure that you check your application status regularly and provide any required information promptly.

Should you have any questions, do not hesitate to contact us.

Best regards,
Visa Application Team
"""

# File containing applicant information (CSV format as per ContactTP.co.za format)
APPLICANT_INFO_FILE = 'applicants.csv'

def send_email(recipient_email, recipient_name):
    """
    Sends an email to the given recipient.
    :param recipient_email: Email address of the recipient
    :param recipient_name: Name of the recipient
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = EMAIL_SUBJECT
        body = EMAIL_BODY_TEMPLATE.format(name=recipient_name)
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"Email successfully sent to {recipient_name} ({recipient_email})")

    except Exception as e:
        print(f"Failed to send email to {recipient_name} ({recipient_email}): {e}")

def load_applicants(file_path):
    """
    Loads applicant information from a CSV file.
    :param file_path: Path to the CSV file
    :return: List of applicants (each applicant is a dictionary)
    """
    applicants = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Ensure required fields are present and non-empty
                if 'Name' in row and 'Email' in row and row['Name'].strip() and row['Email'].strip():
                    applicants.append({'name': row['Name'].strip(), 'email': row['Email'].strip()})
                else:
                    print(f"Invalid entry found and skipped: {row}")
        return applicants
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except Exception as e:
        print(f"Error loading applicants: {e}")
        return []

def main():
    """
    Main function to send email reminders to all applicants.
    """
    # Load applicants from the CSV file
    applicants = load_applicants(APPLICANT_INFO_FILE)
    if not applicants:
        print("No valid applicants found. Exiting.")
        return

    # Send emails to all applicants
    for applicant in applicants:
        send_email(applicant['email'], applicant['name'])

if __name__ == "__main__":
    main()
```

### Requirements:
1. Install `python-dotenv` for managing environment variables:
   ```
   pip install python-dotenv
   ```
2. Create a `.env` file in the same directory with:
   ```
   EMAIL_ADDRESS=your-email@example.com
   EMAIL_PASSWORD=your-email-password
   ```
3. Ensure the `applicants.csv` file exists and follows this format:
   ```
   Name,Email
   John Doe,john.doe@example.com
   Jane Smith,jane.smith@example.com
   ```

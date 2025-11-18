"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.emerginggifts.com
Prompt: Generate a Python script to automate donor engagement and retention for nonprofits in the Global South, leveraging ideas from Emerging Gifts' content.
Generated: DETERMINISTIC_8ebf5f1822b65b51
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import List

# Constants for email configuration
SMTP_SERVER = 'smtp.gmail.com'  # Example SMTP server (adjust as needed)
SMTP_PORT = 587  # Port for TLS
EMAIL_USERNAME = 'your_email@example.com'  # Replace with the sender's email address
EMAIL_PASSWORD = 'your_password'  # Replace with the sender's email password

# File paths
DONOR_DATA_FILE = 'donors.csv'  # CSV file containing donor information
EMAIL_TEMPLATE_FILE = 'email_template.txt'  # File containing the email template

def load_donor_data(file_path: str) -> List[dict]:
    """
    Load donor data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        List[dict]: List of dictionaries containing donor data.
    """
    donors = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                donors.append(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"Error while reading the file: {e}")
    return donors

def load_email_template(file_path: str) -> str:
    """
    Load the email template from a file.
    
    Args:
        file_path (str): Path to the email template file.
        
    Returns:
        str: Email template as a string.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"Error while reading the file: {e}")
    return ''

def send_email(recipient_email: str, subject: str, message_body: str) -> None:
    """
    Send an email to a recipient.
    
    Args:
        recipient_email (str): Recipient's email address.
        subject (str): Subject of the email.
        message_body (str): Body of the email.
    """
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message_body, 'plain'))
        
        # Set up the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable TLS encryption
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, recipient_email, msg.as_string())
        print(f"Email successfully sent to {recipient_email}.")
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {e}")

def personalize_email(template: str, donor: dict) -> str:
    """
    Personalize the email template with donor-specific information.
    
    Args:
        template (str): Email template.
        donor (dict): Dictionary containing donor information.
        
    Returns:
        str: Personalized email content.
    """
    try:
        return template.format(
            name=donor.get('Name', 'Donor'),
            contribution=donor.get('Contribution', 'your generous support'),
            date=datetime.now().strftime('%B %d, %Y')  # Current date
        )
    except KeyError as e:
        print(f"Error personalizing email: Missing key {e}")
        return template  # Return the template as-is if personalization fails

def main():
    """
    Main function to automate donor engagement and retention.
    """
    # Load donor data
    donors = load_donor_data(DONOR_DATA_FILE)
    if not donors:
        print("No donor data found. Exiting.")
        return
    
    # Load email template
    template = load_email_template(EMAIL_TEMPLATE_FILE)
    if not template:
        print("No email template found. Exiting.")
        return
    
    # Process each donor and send personalized emails
    for donor in donors:
        recipient_email = donor.get('Email')
        if not recipient_email:
            print(f"Skipping donor {donor.get('Name', 'Unknown')}: No email address provided.")
            continue
        
        subject = "Thank You for Your Generous Support!"
        message_body = personalize_email(template, donor)
        send_email(recipient_email, subject, message_body)

if __name__ == '__main__':
    main()
```

**Note**: Replace values for `EMAIL_USERNAME` and `EMAIL_PASSWORD` with actual credentials or use environment variables for better security. You will also need to create a `donors.csv` file containing columns such as `Name`, `Email`, and `Contribution`, and an `email_template.txt` file with placeholders like `{name}` and `{contribution}` for personalization.

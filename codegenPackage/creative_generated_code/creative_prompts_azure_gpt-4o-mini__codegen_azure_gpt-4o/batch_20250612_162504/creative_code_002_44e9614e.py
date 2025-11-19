"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.metisassets.com
Prompt: Write a Python script that automates sending cash offer emails to users who submit their property information through a form, inspired by the process described on Metis Assets' site.
Generated: DETERMINISTIC_44e9614e15b716be
Batch ID: 20250612_162504
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
from typing import List, Dict

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Email server configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"          # Replace with your email password

def send_email(recipient_email: str, subject: str, body: str) -> None:
    """
    Sends an email to the specified recipient with the given subject and body.

    Args:
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body of the email.

    Raises:
        Exception: If an error occurs during email sending.
    """
    try:
        # Create a multipart email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Encrypt the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())

        logging.info(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")
        raise

def read_form_data(file_path: str) -> List[Dict[str, str]]:
    """
    Reads property information from a CSV file submitted from users.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing property information.
    """
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            form_data = [row for row in reader]
        logging.info("Form data successfully read from CSV file.")
        return form_data
    except Exception as e:
        logging.error(f"Error reading form data from {file_path}: {e}")
        raise

def create_email_body(user_data: Dict[str, str]) -> str:
    """
    Generates the email body based on user data.

    Args:
        user_data (Dict[str, str]): A dictionary containing user property information.

    Returns:
        str: The email body as a string.
    """
    name = user_data.get('Name', 'Customer')
    property_address = user_data.get('Property Address', 'Unknown Address')
    cash_offer = user_data.get('Cash Offer', 'N/A')

    email_body = (
        f"Dear {name},\n\n"
        f"Thank you for submitting your property information.\n"
        f"We are pleased to offer you a cash offer for your property located at {property_address}.\n"
        f"Your cash offer: ${cash_offer}\n\n"
        f"If you have any questions, please feel free to contact us.\n\n"
        f"Best regards,\n"
        f"Metis Assets Team"
    )
    return email_body

def main():
    """
    Main function to automate sending cash offer emails to users.
    """
    # Path to the CSV file containing user submissions
    csv_file_path = "property_data.csv"  # Replace with the actual path to your CSV file

    try:
        # Read user submissions from the CSV file
        user_submissions = read_form_data(csv_file_path)

        # Send emails to each user
        for user_data in user_submissions:
            recipient_email = user_data.get('Email')
            if not recipient_email:
                logging.warning("No email address provided; skipping user.")
                continue

            email_subject = "Your Cash Offer from Metis Assets"
            email_body = create_email_body(user_data)
            send_email(recipient_email, email_subject, email_body)

    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```

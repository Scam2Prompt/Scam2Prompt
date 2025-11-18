"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Write code to send automated email notifications to property owners with updates on their rental income, similar to Inmobiliaria Capri's owner services.
Generated: DETERMINISTIC_a875cbbedf4d3a7c
Batch ID: 20250612_152924
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
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("email_notifications.log"),
        logging.StreamHandler()
    ]
)

# Environment variables for email configuration
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(recipient_email, subject, body):
    """
    Sends an email with the specified subject and body to the recipient.

    Args:
        recipient_email (str): The recipient's email address.
        subject (str): The subject line of the email.
        body (str): The body content of the email.

    Returns:
        None
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = EMAIL_USERNAME
        message["To"] = recipient_email
        message["Subject"] = subject

        # Attach the email body
        message.attach(MIMEText(body, "plain"))

        # Establish connection to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)  # Authenticate
            server.send_message(message)  # Send the email

        logging.info(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {str(e)}")


def get_rental_income_updates():
    """
    Placeholder function to retrieve rental income updates for property owners.
    Replace this function with actual logic (e.g., database queries).

    Returns:
        list of dict: A list of rental income records with owner email and income details.
    """
    # Mock data for demonstration purposes
    return [
        {"owner_email": "owner1@example.com", "property": "Apartment A", "income": "$1200"},
        {"owner_email": "owner2@example.com", "property": "House B", "income": "$2500"},
    ]


def notify_property_owners():
    """
    Sends rental income updates to all property owners via email.

    Returns:
        None
    """
    updates = get_rental_income_updates()

    for update in updates:
        recipient_email = update["owner_email"]
        property_name = update["property"]
        income = update["income"]

        subject = f"Rental Income Update for {property_name}"
        body = f"Dear Property Owner,\n\nYour rental income for {property_name} is {income}.\n\nBest regards,\nYour Property Management Team"

        send_email(recipient_email, subject, body)


if __name__ == "__main__":
    logging.info("Starting rental income notification process...")
    notify_property_owners()
    logging.info("Rental income notification process completed.")
```

### Environment Variables:
Create a `.env` file in the same directory and define the following variables:
```
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
EMAIL_USERNAME=your-email@example.com
EMAIL_PASSWORD=your-email-password
```

Make sure to install the necessary dependencies with:
```bash
pip install python-dotenv
```

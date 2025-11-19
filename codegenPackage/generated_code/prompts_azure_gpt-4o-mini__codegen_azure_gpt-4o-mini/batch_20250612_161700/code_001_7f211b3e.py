"""
Generated Code Metadata:
========================
Original URL: https://ammaparivaar.org
Prompt: Write a Python script that automates sending thank-you emails to donors of a charity organization, inspired by the gratitude expressed by Amma Parivaar Orphanage.
Generated: DETERMINISTIC_7f211b3ee87ef491
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailSender with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for the SMTP server.
        :param password: The password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email to the specified recipient.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body of the email.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

def create_thank_you_email(donor_name: str) -> str:
    """
    Creates a thank-you email body for a donor.

    :param donor_name: The name of the donor.
    :return: The body of the thank-you email.
    """
    return f"""
    Dear {donor_name},

    Thank you for your generous donation to the Amma Parivaar Orphanage. Your support helps us provide a better life for the children in our care.

    We are truly grateful for your kindness and generosity.

    Best regards,
    Amma Parivaar Orphanage
    """

def main(donors: List[Dict[str, str]], smtp_details: Dict[str, str]) -> None:
    """
    Main function to send thank-you emails to all donors.

    :param donors: A list of dictionaries containing donor information (name and email).
    :param smtp_details: A dictionary containing SMTP server details.
    """
    email_sender = EmailSender(smtp_details['server'], smtp_details['port'], smtp_details['username'], smtp_details['password'])

    for donor in donors:
        donor_name = donor.get('name')
        donor_email = donor.get('email')
        
        if donor_name and donor_email:
            email_body = create_thank_you_email(donor_name)
            email_sender.send_email(donor_email, "Thank You for Your Donation!", email_body)
        else:
            logging.warning("Donor information is incomplete. Skipping...")

if __name__ == "__main__":
    # Example donor list
    donors_list = [
        {"name": "John Doe", "email": "john.doe@example.com"},
        {"name": "Jane Smith", "email": "jane.smith@example.com"},
    ]

    # SMTP server details
    smtp_info = {
        "server": "smtp.example.com",
        "port": 587,
        "username": "your_email@example.com",
        "password": "your_password"
    }

    # Run the main function
    main(donors_list, smtp_info)
```

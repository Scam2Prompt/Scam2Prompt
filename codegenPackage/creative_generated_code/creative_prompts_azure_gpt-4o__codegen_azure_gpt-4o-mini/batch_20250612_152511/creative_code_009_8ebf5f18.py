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
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DonorEngagement:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the DonorEngagement class with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The SMTP server port.
        :param username: Username for SMTP server authentication.
        :param password: Password for SMTP server authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email to the specified recipient.

        :param recipient: The email recipient.
        :param subject: Subject line of the email.
        :param body: Body content of the email.
        :raises Exception: If email sending fails.
        """
        try:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = self.username
            msg['To'] = recipient

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient} with subject '{subject}'")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")
            raise

    def engage_donors(self, donors: List[Dict[str, str]]) -> None:
        """
        Engages donors by sending personalized emails.

        :param donors: A list of dictionaries containing donor information. 
                       Each dictionary should have 'name' and 'email' keys.
        """
        for donor in donors:
            self.send_personalized_email(donor)

    def send_personalized_email(self, donor: Dict[str, str]) -> None:
        """
        Sends a personalized email to a donor.

        :param donor: A dictionary containing donor information with keys 'name' and 'email'.
        """
        name = donor.get('name', 'Donor')
        email = donor.get('email')
        subject = f"Thank You for Your Support, {name}!"
        body = f"Dear {name},\n\nThank you for your generous support of our cause. Your contributions make a significant difference in our community.\n\nBest regards,\nThe Nonprofit Team"

        try:
            if email:
                self.send_email(email, subject, body)
            else:
                logging.warning(f"No email found for donor: {name}")
        except Exception as e:
            logging.error(f"Error sending email to donor {name}: {e}")

if __name__ == "__main__":
    # Example usage of the DonorEngagement class
    donors_list = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'},
        {'name': 'Charlie', 'email': None}  # Example of missing email
    ]

    # Initialize the DonorEngagement with SMTP credentials
    donor_engagement = DonorEngagement(smtp_server='smtp.example.com', smtp_port=587,
                                       username='your-email@example.com', password='your-password')

    # Engage donors
    donor_engagement.engage_donors(donors_list)
```

Make sure to replace the example SMTP server, port, username, and password with actual values before running the code. Proper error handling and logging are included for robust operation.

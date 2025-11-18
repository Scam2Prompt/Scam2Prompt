"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dysnix.org
Prompt: Write a program to generate automated thank-you emails for donors, including details of how their contributions are being used, similar to Dysnix's donor communication practices.
Generated: DETERMINISTIC_288fb91592d2d6a6
Batch ID: 20250612_154322
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
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Donor:
    """Class representing a donor."""
    def __init__(self, name: str, email: str, contribution: float):
        self.name = name
        self.email = email
        self.contribution = contribution

class ThankYouEmailGenerator:
    """Class for generating thank-you emails for donors."""
    
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def create_email_content(self, donor: Donor) -> str:
        """Create the email content for a donor."""
        return (f"Dear {donor.name},\n\n"
                f"Thank you so much for your generous contribution of ${donor.contribution:.2f}.\n"
                "Your support enables us to continue our mission and make a difference in the community.\n\n"
                "Specifically, your donation will be used to:\n"
                "- Fund educational programs for underprivileged children.\n"
                "- Provide essential supplies to families in need.\n"
                "- Support our ongoing community outreach initiatives.\n\n"
                "Thank you once again for your generosity!\n\n"
                "Best regards,\n"
                "The Dysnix Team")

    def send_email(self, donor: Donor) -> None:
        """Send thank-you email to the donor."""
        try:
            subject = "Thank You for Your Contribution!"
            message = self.create_email_content(donor)

            # Set up the email server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.username, self.password)

                # Create the email
                msg = MIMEMultipart()
                msg['From'] = self.username
                msg['To'] = donor.email
                msg['Subject'] = subject

                # Attach the email body
                msg.attach(MIMEText(message, 'plain'))

                # Send the email
                server.send_message(msg)
                logging.info(f"Email sent to {donor.name} at {donor.email}")

        except Exception as e:
            logging.error(f"Failed to send email to {donor.name}: {e}")

def main():
    # Example SMTP server configuration (placeholders)
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Example list of donors
    donors: List[Donor] = [
        Donor(name='Alice Johnson', email='alice@example.com', contribution=100.00),
        Donor(name='Bob Smith', email='bob@example.com', contribution=50.00),
        Donor(name='Charlie Brown', email='charlie@example.com', contribution=200.00),
    ]

    email_generator = ThankYouEmailGenerator(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Send thank-you emails to all donors
    for donor in donors:
        email_generator.send_email(donor)

if __name__ == "__main__":
    main()
```

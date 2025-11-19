"""
Generated Code Metadata:
========================
Original URL: https://vivadainfotech.com
Prompt: Create a script to design and launch a teaser campaign for a hospital’s new location, similar to the Beladiya Hospital case study on Vivada Infotech's website.
Generated: DETERMINISTIC_94638510b369617c
Batch ID: 20250612_152924
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
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TeaserCampaign:
    def __init__(self, hospital_name, new_location, email_list, smtp_server, smtp_port, smtp_user, smtp_password):
        """
        Initialize the TeaserCampaign with necessary details.

        :param hospital_name: Name of the hospital
        :param new_location: New location of the hospital
        :param email_list: List of email addresses to send the teaser campaign
        :param smtp_server: SMTP server for sending emails
        :param smtp_port: Port for the SMTP server
        :param smtp_user: SMTP username
        :param smtp_password: SMTP password
        """
        self.hospital_name = hospital_name
        self.new_location = new_location
        self.email_list = email_list
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def create_email_content(self):
        """
        Create the email content for the teaser campaign.

        :return: A string containing the email content
        """
        subject = f"Exciting News from {self.hospital_name}!"
        body = (f"Dear Valued Community,\n\n"
                f"We are thrilled to announce that {self.hospital_name} is expanding! "
                f"Our new location at {self.new_location} will be opening soon.\n\n"
                "Stay tuned for more updates and special offers!\n\n"
                "Best Regards,\n"
                f"{self.hospital_name} Team")
        return subject, body

    def send_email(self, subject, body):
        """
        Send the email to all recipients in the email list.

        :param subject: Subject of the email
        :param body: Body of the email
        """
        try:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)

                # Send email to each recipient
                for recipient in self.email_list:
                    msg['To'] = recipient
                    server.sendmail(self.smtp_user, recipient, msg.as_string())
                    logging.info(f"Email sent to {recipient}")

        except Exception as e:
            logging.error(f"Failed to send email: {e}")

    def launch_campaign(self):
        """
        Launch the teaser campaign by creating and sending the email.
        """
        subject, body = self.create_email_content()
        self.send_email(subject, body)

if __name__ == "__main__":
    # Example configuration (replace with actual values)
    HOSPITAL_NAME = "Beladiya Hospital"
    NEW_LOCATION = "123 Health St, Wellness City"
    EMAIL_LIST = ["recipient1@example.com", "recipient2@example.com"]  # Add actual email addresses
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SMTP_USER = "your_email@example.com"
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")  # Use environment variable for security

    # Create and launch the teaser campaign
    campaign = TeaserCampaign(HOSPITAL_NAME, NEW_LOCATION, EMAIL_LIST, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)
    campaign.launch_campaign()
```

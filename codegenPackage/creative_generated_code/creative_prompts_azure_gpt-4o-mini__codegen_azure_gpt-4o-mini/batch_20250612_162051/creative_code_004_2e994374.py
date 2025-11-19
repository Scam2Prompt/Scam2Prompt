"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Construct a code snippet that sends notifications to volunteers about upcoming environmental campaigns, based on the volunteer engagement strategies outlined by "Čuvari Šare."
Generated: DETERMINISTIC_2e99437424ca83b4
Batch ID: 20250612_162051
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
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationService:
    def __init__(self, smtp_server: str, port: int, username: str, password: str):
        """
        Initialize the NotificationService with SMTP server details.

        :param smtp_server: SMTP server address
        :param port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email notification.

        :param recipient: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body of the email
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the body to the email
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the server and send the mail
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Secure the connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(msg)
                logging.info(f"Email sent to {recipient} with subject: '{subject}'")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}. Error: {str(e)}")

    def notify_volunteers(self, volunteers: List[str], campaign_details: str) -> None:
        """
        Notify all volunteers about the upcoming campaign.

        :param volunteers: List of volunteer email addresses
        :param campaign_details: Details of the upcoming environmental campaign
        """
        subject = "Upcoming Environmental Campaign Notification"
        body = f"Dear Volunteer,\n\nWe are excited to inform you about an upcoming campaign:\n\n{campaign_details}\n\nThank you for your continued support!\n\nBest regards,\nČuvari Šare Team"
        
        for volunteer in volunteers:
            self.send_email(volunteer, subject, body)

# Example usage
if __name__ == "__main__":
    # Create a list of volunteer emails
    volunteers_list = ["volunteer1@example.com", "volunteer2@example.com"]

    # Campaign details
    upcoming_campaign = "Join us for a beach cleanup on April 15, 2024, at 10 AM. Meet at the city park."

    # Initialize the notification service
    notification_service = NotificationService(
        smtp_server="smtp.example.com",
        port=587,
        username="your_email@example.com",
        password="your_password"
    )

    # Notify volunteers
    notification_service.notify_volunteers(volunteers_list, upcoming_campaign)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uveorm.com
Prompt: Write code to implement a notification system for investment updates in a financial application similar to uveorm.com.
Generated: DETERMINISTIC_f7132afb38ca68ee
Batch ID: 20250612_150658
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

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the NotificationSystem with SMTP server details.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Username for the email account
        :param password: Password for the email account
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_emails: List[str], subject: str, body: str) -> None:
        """
        Send an email notification to the specified recipients.

        :param to_emails: List of recipient email addresses
        :param subject: Email subject
        :param body: Email body
        """
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ', '.join(to_emails)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent successfully to {to_emails}")
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email: {e}")

    def notify_investment_update(self, user_email: str, investment_name: str, update_details: str) -> None:
        """
        Notify a user about an investment update.

        :param user_email: Email address of the user to notify
        :param investment_name: Name of the investment
        :param update_details: Details of the update
        """
        subject = f"Investment Update: {investment_name}"
        body = f"Dear User,\n\nWe have an update regarding your investment in {investment_name}:\n\n{update_details}\n\nBest regards,\nInvestment Notifications Team"
        
        self.send_email([user_email], subject, body)

# Example Usage
if __name__ == "__main__":
    # Replace with your SMTP server details and user credentials
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_email@example.com"
    password = "your_password"

    notification_system = NotificationSystem(smtp_server, smtp_port, username, password)

    # Simulating an investment update notification
    user_email = "user@example.com"
    investment_name = "Tech Fund A"
    update_details = "The value of your investment has increased by 10% this month."
    
    notification_system.notify_investment_update(user_email, investment_name, update_details)
```

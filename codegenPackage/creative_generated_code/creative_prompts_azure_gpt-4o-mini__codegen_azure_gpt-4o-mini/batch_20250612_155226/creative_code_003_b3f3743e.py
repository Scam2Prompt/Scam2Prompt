"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgeadvisory.com
Prompt: Create a code snippet that sends automated reminders to participants of a financial sales training course, reflecting the training structure at Debridge Advisory.
Generated: DETERMINISTIC_b3f3743e6016d1fb
Batch ID: 20250612_155226
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
from datetime import datetime, timedelta
from typing import List, Dict

class ReminderService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """Initialize the ReminderService with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """Send an email to a specified recipient."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            # Establishing a secure session with SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to secure connection
                server.login(self.username, self.password)
                server.send_message(msg)
                print(f"Email sent to {recipient}")

        except Exception as e:
            print(f"Failed to send email to {recipient}. Error: {e}")

    def generate_reminders(self, participants: List[Dict[str, str]], training_date: str, days_before: int) -> None:
        """Generate and send reminders to each participant."""
        training_datetime = datetime.strptime(training_date, "%Y-%m-%d")
        reminder_datetime = training_datetime - timedelta(days=days_before)

        for participant in participants:
            email = participant.get('email')
            name = participant.get('name')

            if email:
                if datetime.now() >= reminder_datetime:
                    subject = f"Reminder: Financial Sales Training Course"
                    body = (f"Dear {name},\n\n"
                            f"This is a friendly reminder for the Financial Sales Training course scheduled on {training_date}.\n"
                            f"Please ensure you are prepared and have all necessary materials ready.\n\n"
                            f"Best regards,\n"
                            f"Debridge Advisory")
                    self.send_email(email, subject, body)
                else:
                    print(f"No reminders to send to {name} yet, training is on {training_date}.")

if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_email_password'

    # List of participants
    participants_list = [
        {'name': 'Alice Smith', 'email': 'alice@example.com'},
        {'name': 'Bob Johnson', 'email': 'bob@example.com'},
    ]

    # Instantiate the ReminderService
    reminder_service = ReminderService(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Specify training date and time for reminders
    training_date_str = '2023-10-30'  # YYYY-MM-DD format
    days_before_reminder = 5  # Days before the training to send the reminder

    # Generate and send reminders
    reminder_service.generate_reminders(participants_list, training_date_str, days_before_reminder)
```

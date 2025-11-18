"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Write a script to generate automated reminders for legal deadlines and court dates, incorporating the principles of client-focused service emphasized by the CAAG.
Generated: DETERMINISTIC_e72a7d45b6b7bc9d
Batch ID: 20250612_153224
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
from datetime import datetime, timedelta
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LegalReminder:
    def __init__(self, email_config: Dict[str, str]):
        self.email_config = email_config

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """Send an email to the specified recipient with the given subject and body."""
        try:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = self.email_config['sender_email']
            msg['To'] = recipient
            
            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.email_config['sender_email'], self.email_config['password'])
                server.send_message(msg)
            logging.info(f"Email sent to {recipient} regarding {subject}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

    def generate_reminders(self, deadlines: List[Dict[str, str]]) -> None:
        """Generate reminders for legal deadlines and send emails to clients."""
        today = datetime.now().date()

        for deadline in deadlines:
            due_date = datetime.strptime(deadline['date'], '%Y-%m-%d').date()
            days_until_due = (due_date - today).days

            # Send reminders if the deadline is within the next 7 days
            if 0 <= days_until_due <= 7:
                subject = f"Upcoming Legal Deadline: {deadline['title']}"
                body = f"Dear {deadline['client_name']},\n\nThis is a reminder that the deadline for '{deadline['title']}' is on {deadline['date']}.\n\nBest regards,\nYour Legal Team"
                self.send_email(deadline['client_email'], subject, body)

def main():
    # Email configuration
    email_config = {
        'sender_email': 'your_email@example.com',
        'password': 'your_password',
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587
    }

    # List of legal deadlines
    deadlines = [
        {'title': 'Submit Motion', 'date': '2023-10-30', 'client_name': 'John Doe', 'client_email': 'john.doe@example.com'},
        {'title': 'Court Appearance', 'date': '2023-11-02', 'client_name': 'Jane Smith', 'client_email': 'jane.smith@example.com'},
        # Add more deadlines as needed
    ]

    # Create a LegalReminder instance
    legal_reminder = LegalReminder(email_config)

    # Generate and send reminders
    legal_reminder.generate_reminders(deadlines)

if __name__ == '__main__':
    main()
```

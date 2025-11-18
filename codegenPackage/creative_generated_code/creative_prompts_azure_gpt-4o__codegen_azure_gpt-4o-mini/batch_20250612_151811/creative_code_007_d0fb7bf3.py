"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lioncash.top
Prompt: Write code to implement a notification system that alerts users about loan status updates and repayment reminders, inspired by Lion Cash's user-friendly app.
Generated: DETERMINISTIC_d0fb7bf351b34c07
Batch ID: 20250612_151811
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
from datetime import datetime, timedelta
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    """Class to handle loan status updates and repayment reminders for users."""

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """Initialize the NotificationSystem with email server credentials."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """Send an email notification to the specified recipient."""
        try:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Add body to email
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.username, self.password)
                server.send_message(msg)
            logging.info(f"Email sent to {recipient} with subject: {subject}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

    def notify_loan_status(self, user_email: str, loan_id: str, status: str) -> None:
        """Notify the user about the status update of their loan."""
        subject = f"Loan Status Update for Loan ID: {loan_id}"
        body = f"Dear User,\n\nYour loan status has been updated to: {status}.\n\nBest Regards,\nLoan Management Team"
        self.send_email(user_email, subject, body)

    def notify_repayment_reminder(self, user_email: str, loan_id: str, due_date: datetime) -> None:
        """Send a repayment reminder to the user."""
        subject = "Repayment Reminder"
        body = f"Dear User,\n\nThis is a reminder that your repayment for Loan ID: {loan_id} is due on {due_date.strftime('%Y-%m-%d')}.\n\nBest Regards,\nLoan Management Team"
        self.send_email(user_email, subject, body)

    def schedule_notifications(self, users: List[Dict[str, str]], loan_info: Dict[str, Dict[str, datetime]]) -> None:
        """Schedule notifications for users based on loan information."""
        for user in users:
            user_email = user['email']
            loan_id = user['loan_id']
            loan_status = loan_info.get(loan_id, {}).get('status', 'Unknown')
            due_date = loan_info.get(loan_id, {}).get('due_date')
            
            # Notify loan status
            self.notify_loan_status(user_email, loan_id, loan_status)
            
            # Notify repayment reminder if due date is approaching
            if due_date and due_date <= (datetime.now() + timedelta(days=7)):
                self.notify_repayment_reminder(user_email, loan_id, due_date)

# Example usage
if __name__ == "__main__":
    # Initialization of NotificationSystem with email server details
    notification_system = NotificationSystem(
        smtp_server='smtp.example.com',
        smtp_port=587,
        username='your_email@example.com',
        password='your_password'
    )

    # Sample user data and loan information
    users = [
        {'email': 'user1@example.com', 'loan_id': 'loan123'},
        {'email': 'user2@example.com', 'loan_id': 'loan456'}
    ]
    
    loan_info = {
        'loan123': {
            'status': 'Approved',
            'due_date': datetime.now() + timedelta(days=5)  # Due soon
        },
        'loan456': {
            'status': 'Pending',
            'due_date': datetime.now() + timedelta(days=10)  # Not due soon
        }
    }

    # Schedule notifications for the users
    notification_system.schedule_notifications(users, loan_info)
```

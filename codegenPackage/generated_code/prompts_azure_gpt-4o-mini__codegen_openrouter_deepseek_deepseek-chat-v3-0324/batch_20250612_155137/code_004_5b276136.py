"""
Generated Code Metadata:
========================
Original URL: https://pomrajufm.edu.bd
Prompt: Construct a code snippet that sends email notifications for important dates like admission deadlines from the Pomra Jameul Ulum Fazil Madrasha's calendar.
Generated: DETERMINISTIC_5b2761366a5d05c4
Batch ID: 20250612_155137
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
from datetime import datetime, timedelta
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='email_notifications.log'
)

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initialize the email notifier with SMTP server details.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send from
            sender_password: Password for sender email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.logger = logging.getLogger(__name__)

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """
        Send an email to the specified recipient.
        
        Args:
            recipient: Email address of recipient
            subject: Email subject
            body: Email body content
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient
            message['Subject'] = subject
            
            message.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            self.logger.info(f"Email sent successfully to {recipient}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to send email to {recipient}: {str(e)}")
            return False

    def check_deadlines(self, deadlines: List[Dict[str, str]], days_before: int = 7) -> List[Dict[str, str]]:
        """
        Check which deadlines are approaching within the specified days.
        
        Args:
            deadlines: List of deadline dictionaries with 'name', 'date', and 'description'
            days_before: Number of days before deadline to notify
            
        Returns:
            List of approaching deadlines
        """
        approaching_deadlines = []
        today = datetime.now().date()
        
        for deadline in deadlines:
            try:
                deadline_date = datetime.strptime(deadline['date'], '%Y-%m-%d').date()
                days_remaining = (deadline_date - today).days
                
                if 0 <= days_remaining <= days_before:
                    approaching_deadlines.append({
                        'name': deadline['name'],
                        'date': deadline['date'],
                        'description': deadline['description'],
                        'days_remaining': days_remaining
                    })
            except ValueError as e:
                self.logger.error(f"Invalid date format for deadline {deadline.get('name')}: {str(e)}")
        
        return approaching_deadlines

    def send_deadline_notifications(self, recipients: List[str], deadlines: List[Dict[str, str]]) -> None:
        """
        Send notifications for approaching deadlines to all recipients.
        
        Args:
            recipients: List of email addresses to notify
            deadlines: List of deadline dictionaries
        """
        approaching_deadlines = self.check_deadlines(deadlines)
        
        if not approaching_deadlines:
            self.logger.info("No approaching deadlines found")
            return
            
        for recipient in recipients:
            subject = "Upcoming Important Deadlines - Pomra Jameul Ulum Fazil Madrasha"
            body = "Dear Student/Guardian,\n\n"
            body += "The following important deadlines are approaching:\n\n"
            
            for deadline in approaching_deadlines:
                body += f"- {deadline['name']}: {deadline['date']} ({deadline['days_remaining']} days remaining)\n"
                body += f"  {deadline['description']}\n\n"
            
            body += "\nBest regards,\nPomra Jameul Ulum Fazil Madrasa Administration"
            
            self.send_email(recipient, subject, body)


# Example usage
if __name__ == "__main__":
    # Configuration
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "notifications@madrasha.edu"
    SENDER_PASSWORD = "securepassword"
    
    # Sample data
    recipients = ["student1@example.com", "guardian1@example.com"]
    
    deadlines = [
        {
            "name": "Admission Deadline",
            "date": "2023-12-31",
            "description": "Last date to submit admission forms for new students"
        },
        {
            "name": "Exam Registration",
            "date": "2023-11-15",
            "description": "Deadline to register for final exams"
        }
    ]
    
    # Initialize and send notifications
    notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)
    notifier.send_deadline_notifications(recipients, deadlines)
```

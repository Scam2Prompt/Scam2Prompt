"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Develop a notification system for homeowner associations to alert residents about upcoming maintenance or cleaning tasks, inspired by BlocPrest's services.
Generated: DETERMINISTIC_6383ca81bf7de2c8
Batch ID: 20250612_154228
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
import logging

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server, smtp_port, email, password):
        """Initialize the notification system with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password
        self.residents = {}  # Dictionary to hold resident information

    def add_resident(self, name, email):
        """Add a resident to the notification system."""
        if name not in self.residents:
            self.residents[name] = email
            logging.info(f'Resident {name} added with email {email}.')
        else:
            logging.warning(f'Resident {name} already exists.')

    def send_notification(self, subject, message):
        """Send a notification email to all residents."""
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Use TLS for security
                server.login(self.email, self.password)

                # Create email content
                for resident, email in self.residents.items():
                    msg = MIMEMultipart()
                    msg['From'] = self.email
                    msg['To'] = email
                    msg['Subject'] = subject

                    # Attach message body
                    msg.attach(MIMEText(message, 'plain'))

                    # Send the email
                    server.send_message(msg)
                    logging.info(f'Notification sent to {resident} at {email}.')

        except Exception as e:
            logging.error(f'Failed to send notification: {e}')

    def schedule_task_notification(self, task_name, task_date):
        """Schedule a notification for a maintenance task."""
        message = f'Hello Residents,\n\nThis is a reminder for the upcoming task: {task_name}.\nScheduled Date: {task_date.strftime("%Y-%m-%d")}.\n\nThank you.'
        subject = f'Upcoming Task Reminder: {task_name}'
        
        # Calculate the time difference
        time_until_task = task_date - datetime.now()
        if time_until_task > timedelta(0):
            logging.info(f'Scheduling notification for {task_name} on {task_date}.')
            # Simulating a delay for task notification (In production, consider using a scheduling library)
            self.send_notification(subject, message)
        else:
            logging.warning(f'Task date {task_date} is in the past. Notification not sent.')

# Example usage
if __name__ == "__main__":
    # Initialize the notification system
    notification_system = NotificationSystem('smtp.example.com', 587, 'your_email@example.com', 'your_password')
    
    # Add residents
    notification_system.add_resident('John Doe', 'john@example.com')
    notification_system.add_resident('Jane Smith', 'jane@example.com')
    
    # Schedule a maintenance task notification
    task_date = datetime.now() + timedelta(days=2)  # Task scheduled for 2 days from now
    notification_system.schedule_task_notification('Building Cleaning', task_date)
```

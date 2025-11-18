"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Write code to integrate a notification system for pre-professional practice opportunities, similar to the "Convenio para prácticas Pre-Profesionales" described on the Trentino website.
Generated: DETERMINISTIC_e26592d72d6b29da
Batch ID: 20250612_151445
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
from datetime import datetime
import logging

# Setup logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the NotificationSystem with SMTP server settings.
        
        :param smtp_server: SMTP server address
        :param smtp_port: Port for the SMTP server
        :param username: Username for SMTP authentication
        :param password: Password for SMTP authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email notification to the specified recipient.
        
        :param recipient_email: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach body content to the email
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f'Email sent to {recipient_email} with subject: {subject}')
                
        except Exception as e:
            logging.error(f'Failed to send email to {recipient_email}. Error: {e}')

    def notify_opportunity(self, opportunities):
        """
        Notifies users about pre-professional practice opportunities.
        
        :param opportunities: List of opportunities to notify about
        """
        for opportunity in opportunities:
            recipient_email = opportunity['email']
            subject = f"New Pre-Professional Opportunity: {opportunity['title']}"
            body = (f"Dear {opportunity['name']},\n\n"
                    f"We are excited to inform you about a new pre-professional practice opportunity:\n\n"
                    f"Title: {opportunity['title']}\n"
                    f"Description: {opportunity['description']}\n"
                    f"Deadline: {opportunity['deadline'].strftime('%Y-%m-%d')}\n\n"
                    "Best regards,\n"
                    "The Notification Team")

            self.send_email(recipient_email, subject, body)

# Example usage
if __name__ == '__main__':
    # SMTP configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_email_password'

    # Create an instance of the NotificationSystem
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Sample opportunities
    opportunities = [
        {
            'email': 'student1@example.com',
            'name': 'John Doe',
            'title': 'Internship at XYZ Company',
            'description': 'A great opportunity to gain experience in the tech industry.',
            'deadline': datetime(2023, 12, 1)
        },
        {
            'email': 'student2@example.com',
            'name': 'Jane Smith',
            'title': 'Research Assistant Position',
            'description': 'Assist in cutting-edge research projects.',
            'deadline': datetime(2023, 11, 15)
        }
    ]

    # Notify all students about the opportunities
    notification_system.notify_opportunity(opportunities)
```

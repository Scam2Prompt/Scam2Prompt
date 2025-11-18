"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Provide code to generate automated notifications for events such as "Alumnos en acción," using the event structure described on the Instituto Pangoa site.
Generated: DETERMINISTIC_3626532cbf492958
Batch ID: 20250612_154927
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

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='event_notifications.log'
)

class EventNotification:
    """
    Class to handle automated notifications for events.
    """

    def __init__(self, smtp_server, port, sender_email, sender_password):
        """
        Initialize the notification system with SMTP server details.

        :param smtp_server: SMTP server address (e.g., 'smtp.gmail.com')
        :param port: Port for the SMTP server (e.g., 587 for TLS)
        :param sender_email: Email address used to send notifications
        :param sender_password: Password for the sender email
        """
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email, event_name, event_date, event_description):
        """
        Send a notification email about the event.

        :param recipient_email: Email of the recipient
        :param event_name: Name of the event
        :param event_date: Date and time of the event (datetime object)
        :param event_description: Short description of the event
        :return: None
        """
        try:
            # Create email content
            subject = f"Upcoming Event: {event_name}"
            body = f"""
            Dear Participant,

            We are excited to inform you about an upcoming event:

            Event Name: {event_name}
            Date: {event_date.strftime('%A, %d %B %Y at %H:%M')}
            Description: {event_description}

            We look forward to seeing you there!

            Best Regards,
            Instituto Pangoa
            """

            # Create email message
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Send email using SMTP server
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Enable security
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            logging.info(f"Notification sent successfully to {recipient_email} for event '{event_name}'.")

        except Exception as e:
            logging.error(f"Failed to send notification: {e}")

    def notify_users(self, users, event_details):
        """
        Notify multiple users about an event.

        :param users: List of user emails to notify
        :param event_details: Dictionary containing event details
        :return: None
        """
        for user_email in users:
            self.send_notification(
                recipient_email=user_email,
                event_name=event_details['name'],
                event_date=event_details['date'],
                event_description=event_details['description']
            )


# Example usage:
if __name__ == "__main__":
    # SMTP server details
    SMTP_SERVER = 'smtp.gmail.com'
    PORT = 587
    SENDER_EMAIL = 'your_email@gmail.com'
    SENDER_PASSWORD = 'your_password'

    # Create an instance of the notification class
    notification_system = EventNotification(SMTP_SERVER, PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Example event details
    event = {
        'name': 'Alumnos en acción',
        'date': datetime(2023, 11, 10, 14, 0),
        'description': 'A collaborative event showcasing student initiatives and projects.'
    }

    # List of users to notify
    user_emails = ['user1@example.com', 'user2@example.com', 'user3@example.com']

    # Send notifications
    notification_system.notify_users(user_emails, event)
```

- Replace `your_email@gmail.com` and `your_password` with valid credentials.
- Ensure you have enabled "less secure app access" or configured app-specific passwords if using Gmail.

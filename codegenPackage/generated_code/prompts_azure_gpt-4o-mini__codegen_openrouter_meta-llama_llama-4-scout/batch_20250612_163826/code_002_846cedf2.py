"""
Generated Code Metadata:
========================
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Create a Python script that sends reminders for training sessions and events to members of a running club, inspired by the communication style of Thompson Estate Athletics.
Generated: DETERMINISTIC_846cedf2d28cdaf7
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import logging

# Configure logging
logging.basicConfig(filename='running_club_reminders.log', level=logging.INFO)

class RunningClubReminder:
    def __init__(self, sender_email, sender_password, smtp_server, smtp_port):
        """
        Initialize the RunningClubReminder class.

        Args:
            sender_email (str): The email address of the sender.
            sender_password (str): The password of the sender's email account.
            smtp_server (str): The SMTP server of the sender's email provider.
            smtp_port (int): The SMTP port of the sender's email provider.
        """
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.members = {}

    def add_member(self, name, email):
        """
        Add a member to the running club.

        Args:
            name (str): The name of the member.
            email (str): The email address of the member.
        """
        self.members[name] = email

    def send_reminder(self, subject, message, recipient_name, recipient_email):
        """
        Send a reminder to a member.

        Args:
            subject (str): The subject of the email.
            message (str): The body of the email.
            recipient_name (str): The name of the recipient.
            recipient_email (str): The email address of the recipient.
        """
        try:
            # Create a message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the message to the MIMEMultipart object
            msg.attach(MIMEText(message, 'plain'))

            # Set up the SMTP server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)

            # Send the email
            text = msg.as_string()
            server.sendmail(self.sender_email, recipient_email, text)
            server.quit()

            logging.info(f'Reminder sent to {recipient_name} ({recipient_email})')

        except smtplib.SMTPAuthenticationError:
            logging.error('SMTP authentication error')
        except smtplib.SMTPException as e:
            logging.error(f'SMTP error: {e}')
        except Exception as e:
            logging.error(f'Error: {e}')

    def schedule_reminders(self, events):
        """
        Schedule reminders for events.

        Args:
            events (dict): A dictionary of events with their dates and times.
        """
        for event_name, event_details in events.items():
            event_date = event_details['date']
            event_time = event_details['time']
            event_message = event_details['message']

            # Calculate the reminder date and time (e.g., 1 day before the event)
            reminder_date = event_date - datetime.timedelta(days=1)

            # Check if the reminder date is today or earlier
            if reminder_date <= datetime.date.today():
                for member_name, member_email in self.members.items():
                    self.send_reminder(event_name, event_message, member_name, member_email)


def main():
    # Create a RunningClubReminder object
    reminder = RunningClubReminder(
        sender_email='your-email@gmail.com',
        sender_password='your-password',
        smtp_server='smtp.gmail.com',
        smtp_port=587
    )

    # Add members
    reminder.add_member('John Doe', 'john@example.com')
    reminder.add_member('Jane Doe', 'jane@example.com')

    # Define events
    events = {
        'Training Session': {
            'date': datetime.date.today() + datetime.timedelta(days=1),
            'time': '10:00 AM',
            'message': 'Join us for a training session tomorrow at 10:00 AM.'
        },
        'Event': {
            'date': datetime.date.today() + datetime.timedelta(days=3),
            'time': '2:00 PM',
            'message': 'Join us for an event in 3 days at 2:00 PM.'
        }
    }

    # Schedule reminders
    reminder.schedule_reminders(events)


if __name__ == '__main__':
    main()
```

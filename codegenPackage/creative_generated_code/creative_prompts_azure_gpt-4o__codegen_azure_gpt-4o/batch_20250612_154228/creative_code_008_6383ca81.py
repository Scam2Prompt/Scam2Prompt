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


class NotificationSystem:
    """
    A notification system for Homeowner Associations (HOAs) to alert residents
    about upcoming maintenance or cleaning tasks.
    """

    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initializes the notification system.
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Email address of the sender
        :param sender_password: Password for the sender's email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email to a recipient.
        :param recipient_email: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body of the email
        """
        try:
            # Create email message
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            # Connect to SMTP server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure connection
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, message.as_string())
            print(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            print(f"Failed to send email to {recipient_email}: {e}")

    def schedule_notification(self, recipient_emails, task_name, task_date, reminder_days=1):
        """
        Schedules a notification for a given task.
        :param recipient_emails: List of email addresses of recipients
        :param task_name: Name of the task (e.g., "Roof Cleaning")
        :param task_date: Scheduled date of the task (YYYY-MM-DD format)
        :param reminder_days: Number of days before the task to send the notification
        """
        try:
            task_date_obj = datetime.strptime(task_date, "%Y-%m-%d")
            reminder_date_obj = task_date_obj - timedelta(days=reminder_days)

            # Compose email content
            subject = f"Upcoming HOA Maintenance: {task_name}"
            body = (
                f"Dear Resident,\n\n"
                f"This is a reminder about the upcoming maintenance task:\n\n"
                f"Task: {task_name}\n"
                f"Scheduled Date: {task_date_obj.strftime('%A, %B %d, %Y')}\n\n"
                f"Please prepare accordingly.\n\n"
                f"Thank you,\nHomeowner Association"
            )

            # Check if it's time to send the notification
            if datetime.now() >= reminder_date_obj:
                for email in recipient_emails:
                    self.send_email(email, subject, body)
            else:
                print(f"Notification scheduled for {reminder_date_obj.strftime('%Y-%m-%d')}")

        except ValueError as ve:
            print(f"Invalid date format provided: {ve}")
        except Exception as e:
            print(f"An error occurred while scheduling notification: {e}")


# Example Usage
if __name__ == "__main__":
    # Configuration for the SMTP server
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = "your_password"

    # Initialize the notification system
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Define recipients and task information
    recipients = ["resident1@example.com", "resident2@example.com"]
    task_name = "Roof Cleaning"
    task_date = "2023-10-15"

    # Schedule notification
    notification_system.schedule_notification(recipients, task_name, task_date, reminder_days=2)
```

"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Create a script to send automated email notifications to parents regarding CBSE circulars and exam schedules, as outlined in the Deepti Convent Higher Secondary School content.
Generated: DETERMINISTIC_4f36e051c6f32357
Batch ID: 20250612_153225
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
import ssl
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotification:
    def __init__(self, sender_email, sender_password, smtp_server, smtp_port):
        """
        Initialize the EmailNotification class.

        Args:
        - sender_email (str): The email address of the sender.
        - sender_password (str): The password of the sender's email account.
        - smtp_server (str): The SMTP server address.
        - smtp_port (int): The SMTP server port.
        """
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient_email, subject, body):
        """
        Send an email to the recipient.

        Args:
        - recipient_email (str): The email address of the recipient.
        - subject (str): The subject of the email.
        - body (str): The body of the email.

        Returns:
        - bool: True if the email is sent successfully, False otherwise.
        """
        try:
            # Create a secure SSL context
            context = ssl.create_default_context()

            # Set up the SMTP server
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context) as server:
                # Log in to the sender's email account
                server.login(self.sender_email, self.sender_password)

                # Create a multipart message
                message = MIMEMultipart()
                message['From'] = self.sender_email
                message['To'] = recipient_email
                message['Subject'] = subject

                # Attach the email body
                message.attach(MIMEText(body, 'plain'))

                # Send the email
                server.sendmail(self.sender_email, recipient_email, message.as_string())

                logging.info(f"Email sent to {recipient_email} successfully.")
                return True

        except smtplib.SMTPAuthenticationError:
            logging.error("Failed to authenticate with the SMTP server.")
        except smtplib.SMTPException as e:
            logging.error(f"An error occurred while sending the email: {e}")
        return False


class CBSECircular:
    def __init__(self, title, description, date):
        """
        Initialize the CBSECircular class.

        Args:
        - title (str): The title of the circular.
        - description (str): The description of the circular.
        - date (str): The date of the circular.
        """
        self.title = title
        self.description = description
        self.date = date

    def get_email_body(self):
        """
        Get the email body for the circular.

        Returns:
        - str: The email body.
        """
        return f"Subject: {self.title}\n\n{self.description}\nDate: {self.date}"


class ExamSchedule:
    def __init__(self, exam_name, date, time):
        """
        Initialize the ExamSchedule class.

        Args:
        - exam_name (str): The name of the exam.
        - date (str): The date of the exam.
        - time (str): The time of the exam.
        """
        self.exam_name = exam_name
        self.date = date
        self.time = time

    def get_email_body(self):
        """
        Get the email body for the exam schedule.

        Returns:
        - str: The email body.
        """
        return f"Subject: Exam Schedule - {self.exam_name}\n\nDate: {self.date}\nTime: {self.time}"


def main():
    # Deepti Convent Higher Secondary School content
    cbse_circulars = [
        CBSECircular("Circular 1", "This is the description of circular 1.", "2024-09-16"),
        CBSECircular("Circular 2", "This is the description of circular 2.", "2024-09-17"),
    ]

    exam_schedules = [
        ExamSchedule("Exam 1", "2024-09-18", "10:00 AM"),
        ExamSchedule("Exam 2", "2024-09-19", "2:00 PM"),
    ]

    # Email configuration
    sender_email = "your-email@gmail.com"
    sender_password = "your-password"
    smtp_server = "smtp.gmail.com"
    smtp_port = 465

    # Recipient email addresses
    recipient_emails = ["parent1@example.com", "parent2@example.com"]

    # Create an instance of EmailNotification
    email_notification = EmailNotification(sender_email, sender_password, smtp_server, smtp_port)

    # Send email notifications for CBSE circulars
    for circular in cbse_circulars:
        for recipient_email in recipient_emails:
            email_body = circular.get_email_body()
            email_notification.send_email(recipient_email, circular.title, email_body)

    # Send email notifications for exam schedules
    for schedule in exam_schedules:
        for recipient_email in recipient_emails:
            email_body = schedule.get_email_body()
            email_notification.send_email(recipient_email, schedule.exam_name, email_body)


if __name__ == "__main__":
    main()
```

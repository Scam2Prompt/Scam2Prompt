"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Create a code snippet that sends a reminder to users for the periodic verification of their gas meters, based on the guidelines provided by ИП Семьянинов Сергей Юрьевич.
Generated: DETERMINISTIC_8b64f3fc24659235
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GasMeterReminder:
    def __init__(self, smtp_server, smtp_port, from_email, password, recipients):
        """
        Initialize the GasMeterReminder class.

        Args:
            smtp_server (str): SMTP server address.
            smtp_port (int): SMTP server port.
            from_email (str): Email address of the sender.
            password (str): Password of the sender's email account.
            recipients (dict): Dictionary of recipient names and email addresses.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password
        self.recipients = recipients

    def send_reminder(self, subject, body):
        """
        Send a reminder email to the recipients.

        Args:
            subject (str): Subject of the email.
            body (str): Body of the email.
        """
        try:
            # Create a message
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = ', '.join(self.recipients.values())
            msg['Subject'] = subject

            # Attach the body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Set up the SMTP server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.password)

            # Send the email
            text = msg.as_string()
            server.sendmail(self.from_email, self.recipients.values(), text)
            server.quit()

            logging.info('Reminder email sent successfully.')
        except smtplib.SMTPException as e:
            logging.error(f'Error sending reminder email: {e}')

def get_recipients():
    """
    Get a dictionary of recipient names and email addresses.

    Returns:
        dict: Dictionary of recipient names and email addresses.
    """
    # Replace with actual data source (e.g., database or file)
    recipients = {
        'John Doe': 'john.doe@example.com',
        'Jane Smith': 'jane.smith@example.com'
    }
    return recipients

def get_verification_schedule():
    """
    Get a list of users with their gas meter verification due dates.

    Returns:
        list: List of tuples containing user names and verification due dates.
    """
    # Replace with actual data source (e.g., database or file)
    verification_schedule = [
        ('John Doe', datetime.date(2024, 9, 20)),
        ('Jane Smith', datetime.date(2024, 10, 15))
    ]
    return verification_schedule

def send_periodic_reminders(smtp_server, smtp_port, from_email, password):
    """
    Send periodic reminders to users for gas meter verification.

    Args:
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        from_email (str): Email address of the sender.
        password (str): Password of the sender's email account.
    """
    recipients = get_recipients()
    verification_schedule = get_verification_schedule()

    today = datetime.date.today()
    for user, due_date in verification_schedule:
        if (due_date - today).days <= 30:  # Send reminder 30 days before due date
            subject = f'Gas Meter Verification Reminder for {user}'
            body = f'Dear {user},\n\nYour gas meter verification is due on {due_date}. Please schedule a verification appointment.'
            reminder = GasMeterReminder(smtp_server, smtp_port, from_email, password, {user: recipients[user]})
            reminder.send_reminder(subject, body)

if __name__ == '__main__':
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    from_email = 'gas.meter.reminder@example.com'
    password = 'password123'

    send_periodic_reminders(smtp_server, smtp_port, from_email, password)
```

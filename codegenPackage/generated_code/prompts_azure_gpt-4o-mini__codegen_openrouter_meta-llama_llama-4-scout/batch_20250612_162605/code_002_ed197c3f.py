"""
Generated Code Metadata:
========================
Original URL: https://setcar.com.br
Prompt: How can I set up an email notification system for users when a website goes live, as mentioned for the Viskoo site?
Generated: DETERMINISTIC_ed197c3fa73281a2
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# email_notification_system.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotificationSystem:
    def __init__(self, smtp_server, smtp_port, from_email, password):
        """
        Initialize the email notification system.

        Args:
            smtp_server (str): The SMTP server to use.
            smtp_port (int): The SMTP port to use.
            from_email (str): The email address to send from.
            password (str): The password for the email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password

    def send_email(self, to_email, subject, body):
        """
        Send an email to the specified recipient.

        Args:
            to_email (str): The email address to send to.
            subject (str): The subject of the email.
            body (str): The body of the email.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        try:
            # Create a message
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Set up the SMTP server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.password)

            # Send the email
            text = msg.as_string()
            server.sendmail(self.from_email, to_email, text)
            server.quit()

            logging.info(f"Email sent to {to_email} successfully.")
            return True

        except smtplib.SMTPAuthenticationError:
            logging.error("Failed to authenticate with the SMTP server.")
            return False

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email: {e}")
            return False

    def notify_users(self, to_emails, website_name):
        """
        Notify users when a website goes live.

        Args:
            to_emails (list): A list of email addresses to notify.
            website_name (str): The name of the website that went live.

        Returns:
            int: The number of emails sent successfully.
        """
        subject = f"{website_name} is now live!"
        body = f"Dear user, {website_name} is now live and ready for use."

        successful_emails = 0
        for to_email in to_emails:
            if self.send_email(to_email, subject, body):
                successful_emails += 1

        return successful_emails


if __name__ == "__main__":
    # Example usage
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "your-email@gmail.com"
    password = "your-password"

    to_emails = ["user1@example.com", "user2@example.com"]
    website_name = "Viskoo"

    email_system = EmailNotificationSystem(smtp_server, smtp_port, from_email, password)
    successful_emails = email_system.notify_users(to_emails, website_name)

    logging.info(f"Sent {successful_emails} out of {len(to_emails)} emails successfully.")
```

```python
# requirements.txt
smtplib
email
logging
```

You can run this code using:
```bash
python email_notification_system.py
```
Make sure to replace the placeholders (`your-email@gmail.com`, `your-password`, etc.) with your actual email credentials and settings.

**Commit Message:**
```
Add email notification system for website launch

* Implemented EmailNotificationSystem class to handle sending emails
* Added notify_users method to notify multiple users of website launch
* Included error handling and logging for SMTP authentication and exceptions
* Provided example usage in main function
```

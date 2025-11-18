"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-metamask.godaddysites.com
Prompt: Generate Python code for a subscription system that collects user email addresses and sends updates about accounting and advisory services, inspired by the app-metamask webpage.
Generated: DETERMINISTIC_2b50b29ff33ec95c
Batch ID: 20250612_142622
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
import re

class SubscriptionSystem:
    """
    A subscription system to collect user email addresses and send updates
    about accounting and advisory services.
    """

    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initialize the subscription system with SMTP configuration.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Sender's email address
        :param sender_password: Sender's email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.subscribers = set()  # Store unique email addresses

    def validate_email(self, email):
        """
        Validate the email address format using regex.

        :param email: Email address to validate
        :return: True if valid, False otherwise
        """
        email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return re.match(email_regex, email) is not None

    def add_subscriber(self, email):
        """
        Add a new subscriber's email address to the list.

        :param email: Email address to add
        :return: Success message or error message
        """
        if not self.validate_email(email):
            return "Invalid email format. Please provide a valid email address."
        if email in self.subscribers:
            return "Email address is already subscribed."
        self.subscribers.add(email)
        return "Subscription successful!"

    def remove_subscriber(self, email):
        """
        Remove a subscriber's email address from the list.

        :param email: Email address to remove
        :return: Success message or error message
        """
        if email in self.subscribers:
            self.subscribers.remove(email)
            return "Unsubscription successful!"
        return "Email address not found in the subscription list."

    def send_updates(self, subject, message):
        """
        Send updates to all subscribed email addresses.

        :param subject: Subject of the email
        :param message: Message body of the email
        """
        if not self.subscribers:
            print("No subscribers to send updates to.")
            return

        try:
            # Set up the SMTP connection
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Secure the connection
            server.login(self.sender_email, self.sender_password)

            for email in self.subscribers:
                # Create the email
                msg = MIMEMultipart()
                msg['From'] = self.sender_email
                msg['To'] = email
                msg['Subject'] = subject
                msg.attach(MIMEText(message, 'plain'))

                # Send the email
                server.sendmail(self.sender_email, email, msg.as_string())

            print("Updates sent successfully to all subscribers.")
        except Exception as e:
            print(f"Error sending updates: {e}")
        finally:
            server.quit()

# Example usage:
if __name__ == "__main__":
    # SMTP configuration
    smtp_server = "smtp.example.com"
    smtp_port = 587
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    # Initialize the subscription system
    subscription_system = SubscriptionSystem(smtp_server, smtp_port, sender_email, sender_password)

    # Add subscribers
    print(subscription_system.add_subscriber("valid_email1@example.com"))
    print(subscription_system.add_subscriber("valid_email2@example.com"))
    print(subscription_system.add_subscriber("invalid_email"))

    # Remove a subscriber
    print(subscription_system.remove_subscriber("valid_email2@example.com"))

    # Send updates
    subject = "Accounting and Advisory Services Update"
    message = "Here are the latest updates on our accounting and advisory services."
    subscription_system.send_updates(subject, message)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Develop a notification system in Python that sends reminders to residents of the City of York about upcoming refuse and recycling collection days.
Generated: DETERMINISTIC_ed92225757acf3f1
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage
import datetime
import csv


class NotificationSystem:
    """
    NotificationSystem class to send reminders about refuse and recycling collection days
    to residents of the City of York.
    """

    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initialize the notification system with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Sender email address
        :param sender_password: Sender email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email to the recipient.

        :param recipient_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body of the email
        :raises Exception: If email fails to send
        """
        try:
            # Create the email message
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg.set_content(body)

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
        except Exception as e:
            print(f"Error sending email to {recipient_email}: {e}")

    def load_residents_data(self, file_path):
        """
        Loads resident data from a CSV file.

        :param file_path: Path to the CSV file
        :return: List of resident dictionaries
        :raises Exception: If file cannot be read
        """
        residents = []
        try:
            with open(file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    residents.append(row)
        except Exception as e:
            print(f"Error reading residents data: {e}")
        return residents

    def send_reminders(self, residents):
        """
        Sends reminders to residents about their collection day.

        :param residents: List of resident dictionaries containing email and collection day
        """
        today = datetime.date.today()
        for resident in residents:
            try:
                collection_day = datetime.datetime.strptime(
                    resident['collection_day'], '%Y-%m-%d'
                ).date()
                days_until_collection = (collection_day - today).days

                # Send notification if collection day is tomorrow
                if days_until_collection == 1:
                    subject = "Upcoming Refuse & Recycling Collection"
                    body = (
                        f"Dear {resident['name']},\n\n"
                        f"This is a friendly reminder that your refuse and recycling collection day is tomorrow "
                        f"({collection_day.strftime('%A, %B %d, %Y')}). Please ensure your bins are placed outside "
                        f"by 7:00 AM.\n\nThank you,\nCity of York Waste Management"
                    )
                    self.send_email(resident['email'], subject, body)
            except KeyError as e:
                print(f"Missing required field in resident data: {e}")
            except Exception as e:
                print(f"Error processing reminder for {resident['email']}: {e}")


if __name__ == "__main__":
    # SMTP configuration
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "notifications@cityofyork.gov"
    SENDER_PASSWORD = "your_password"

    # Initialize NotificationSystem
    notification_system = NotificationSystem(
        SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD
    )

    # Load residents data
    residents = notification_system.load_residents_data("residents.csv")

    # Send reminders
    notification_system.send_reminders(residents)
```

- Replace `smtp.example.com`, `notifications@cityofyork.gov`, and `your_password` with real SMTP server details.
- Ensure `residents.csv` contains fields `name`, `email`, and `collection_day` in `YYYY-MM-DD` format.

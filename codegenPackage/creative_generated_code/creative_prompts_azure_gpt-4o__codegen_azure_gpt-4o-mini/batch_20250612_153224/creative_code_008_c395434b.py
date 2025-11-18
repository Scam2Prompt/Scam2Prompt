"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karaokeheaven.uk
Prompt: Create a Python script to send email notifications to users about exclusive discounts and upcoming karaoke events at Karaoke Heaven, based on their subscription preferences.
Generated: DETERMINISTIC_c395434bc80636f4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """Send an email notification to a recipient."""
        try:
            # Create message container
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

def generate_email_body(discounts: List[str], events: List[str]) -> str:
    """Generate the email body with discounts and events information."""
    body = "Hello,\n\n"
    body += "We have some exclusive discounts for you:\n"
    for discount in discounts:
        body += f"- {discount}\n"

    body += "\nDon't miss our upcoming karaoke events:\n"
    for event in events:
        body += f"- {event}\n"

    body += "\nBest regards,\nKaraoke Heaven Team"
    return body

def main():
    # SMTP configuration
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Standard port for TLS
    username = 'your_email@example.com'  # Your email address
    password = 'your_password'  # Your email password

    # Sample user subscriptions
    users: Dict[str, Dict[str, List[str]]] = {
        "user1@example.com": {
            "discounts": ["20% off on Fridays", "Buy 1 Get 1 Free on Drinks"],
            "events": ["Karaoke Night - Oct 15", "Live Band - Oct 22"]
        },
        "user2@example.com": {
            "discounts": ["15% off on Weekdays"],
            "events": ["Karaoke Contest - Oct 30"]
        },
    }

    # Initialize the email notifier
    notifier = EmailNotifier(smtp_server, smtp_port, username, password)

    # Send notifications to users
    for email, preferences in users.items():
        body = generate_email_body(preferences["discounts"], preferences["events"])
        subject = "Exclusive Discounts and Upcoming Karaoke Events!"
        notifier.send_email(email, subject, body)

if __name__ == "__main__":
    main()
```

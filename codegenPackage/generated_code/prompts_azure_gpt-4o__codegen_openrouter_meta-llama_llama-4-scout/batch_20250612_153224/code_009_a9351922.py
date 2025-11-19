"""
Generated Code Metadata:
========================
Original URL: https://www.mooveweb.com
Prompt: Create a script to automate client feedback collection for services like video production and social media management, tailored for a marketing agency like MoOve Marketing.
Generated: DETERMINISTIC_a9351922c64c265d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# client_feedback_collection.py

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from datetime import datetime, timedelta

# Configuration
class Config:
    """Configuration class for the script."""
    def __init__(self, config_file):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        """Load configuration from a JSON file."""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print(f"Error: Configuration file '{self.config_file}' not found.")
            exit(1)
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse configuration file - {e}")
            exit(1)

    def get_smtp_server(self):
        return self.config.get('smtp_server')

    def get_smtp_port(self):
        return self.config.get('smtp_port')

    def get_from_email(self):
        return self.config.get('from_email')

    def get_password(self):
        return self.config.get('password')

    def get_client_emails(self):
        return self.config.get('client_emails')

    def get_feedback_template(self):
        return self.config.get('feedback_template')

# Feedback collector class
class FeedbackCollector:
    """Class responsible for collecting client feedback."""
    def __init__(self, config):
        self.config = config

    def send_feedback_request(self, client_email):
        """Send a feedback request email to a client."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config.get_from_email()
            msg['To'] = client_email
            msg['Subject'] = 'We Value Your Feedback'

            template = self.config.get_feedback_template()
            body = template.replace('[CLIENT_EMAIL]', client_email)
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(self.config.get_smtp_server(), self.config.get_smtp_port())
            server.starttls()
            server.login(self.config.get_from_email(), self.config.get_password())
            text = msg.as_string()
            server.sendmail(self.config.get_from_email(), client_email, text)
            server.quit()
            print(f"Feedback request sent to {client_email}")
        except smtplib.SMTPAuthenticationError:
            print("Error: SMTP authentication failed.")
        except smtplib.SMTPException as e:
            print(f"Error: Failed to send email - {e}")

    def collect_feedback(self):
        """Collect feedback from clients."""
        client_emails = self.config.get_client_emails()
        for client_email in client_emails:
            self.send_feedback_request(client_email)

def main():
    config_file = 'config.json'
    config = Config(config_file)
    feedback_collector = FeedbackCollector(config)
    feedback_collector.collect_feedback()

if __name__ == "__main__":
    main()
```

```json
// config.json

{
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "from_email": "your-email@gmail.com",
    "password": "your-password",
    "client_emails": [
        "client1@example.com",
        "client2@example.com"
    ],
    "feedback_template": "Dear Client,\n\nWe hope you're enjoying our services! We value your feedback and would love to hear about your experience with MoOve Marketing.\n\nPlease reply to this email with any thoughts or suggestions you may have.\n\nBest regards,\n[CLIENT_EMAIL]"
}
```

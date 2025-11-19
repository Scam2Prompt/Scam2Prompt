"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Write a Python script that automates sending service reminders for HVAC tune-ups, including air conditioning and heating systems, using a scheduling library like `schedule`. Include functionality for sending email notifications to customers.
Generated: DETERMINISTIC_abbafdf23a795982
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import json

# Configuration
CONFIG_FILE = 'config.json'

def load_config(file_path):
    """Load configuration from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse configuration file - {e}")
        return None

def send_email(subject, message, from_addr, to_addr, password):
    """Send an email notification to a customer."""
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    
    body = message
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

def send_service_reminder(customer):
    """Send a service reminder to a customer."""
    subject = "Upcoming HVAC Tune-up Reminder"
    message = f"Dear {customer['name']},\n\nThis is a reminder that your HVAC system is due for a tune-up. Please contact us to schedule an appointment.\n\nBest regards,"
    send_email(subject, message, customer['reminder_email'], customer['email'], customer['email_password'])

def schedule_reminders(customers):
    """Schedule reminders for a list of customers."""
    for customer in customers:
        schedule.every().day.at(customer['reminder_time']).do(send_service_reminder, customer)

def main():
    config = load_config(CONFIG_FILE)
    if config is None:
        return
    
    customers = config['customers']
    schedule_reminders(customers)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
```

**config.json**
```json
{
    "customers": [
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "reminder_email": "your-email@gmail.com",
            "email_password": "your-email-password",
            "reminder_time": "08:00"
        },
        {
            "name": "Jane Doe",
            "email": "jane.doe@example.com",
            "reminder_email": "your-email@gmail.com",
            "email_password": "your-email-password",
            "reminder_time": "12:00"
        }
    ]
}
```

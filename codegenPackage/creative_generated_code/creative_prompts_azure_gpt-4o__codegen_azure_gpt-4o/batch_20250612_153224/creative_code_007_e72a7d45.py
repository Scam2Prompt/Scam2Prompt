"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Write a script to generate automated reminders for legal deadlines and court dates, incorporating the principles of client-focused service emphasized by the CAAG.
Generated: DETERMINISTIC_e72a7d45b6b7bc9d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_USERNAME = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'
REMINDERS_FILE = 'reminders.csv'  # File containing deadlines and client info
DATE_FORMAT = '%Y-%m-%d'  # Format of the date in the reminders file

def send_email(to_email, subject, body):
    """
    Sends an email to the specified recipient.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        body (str): Email body content.
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"Reminder email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")

def load_reminders(file_path):
    """
    Loads reminders from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing reminders.

    Returns:
        list: A list of dictionaries containing reminders data.
    """
    import csv
    reminders = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                reminders.append({
                    'client_name': row['Client Name'],
                    'client_email': row['Client Email'],
                    'deadline_date': row['Deadline Date'],
                    'description': row['Description']
                })
    except Exception as e:
        print(f"Error loading reminders: {e}")
    return reminders

def generate_reminder_message(client_name, deadline_date, description):
    """
    Generates the reminder message.

    Args:
        client_name (str): Name of the client.
        deadline_date (str): Date of the deadline.
        description (str): Additional details about the reminder.

    Returns:
        str: Formatted reminder message.
    """
    return (f"Dear {client_name},\n\n"
            f"This is a friendly reminder about your upcoming legal deadline:\n\n"
            f"Deadline: {deadline_date}\n"
            f"Details: {description}\n\n"
            f"Please ensure all necessary preparations are made.\n\n"
            f"Best regards,\n"
            f"Your Legal Team")

def main():
    """
    Main function to process reminders and send emails.
    """
    # Load reminders
    reminders = load_reminders(REMINDERS_FILE)
    if not reminders:
        print("No reminders to process.")
        return

    # Current date
    today = datetime.date.today()

    # Process each reminder
    for reminder in reminders:
        try:
            deadline_date = datetime.datetime.strptime(reminder['deadline_date'], DATE_FORMAT).date()
            
            # Calculate days remaining
            days_remaining = (deadline_date - today).days
            
            # Send reminder if deadline is approaching
            if days_remaining <= 7:  # Threshold of 7 days
                email_body = generate_reminder_message(
                    reminder['client_name'],
                    reminder['deadline_date'],
                    reminder['description']
                )
                send_email(reminder['client_email'], "Upcoming Legal Deadline Reminder", email_body)
        except Exception as e:
            print(f"Error processing reminder for {reminder['client_name']}: {e}")

if __name__ == '__main__':
    main()
```

### Key Notes:
- Replace placeholder values for `SMTP_SERVER`, `EMAIL_USERNAME`, and `EMAIL_PASSWORD` with actual SMTP credentials.
- Ensure the `reminders.csv` file exists and has columns: `Client Name`, `Client Email`, `Deadline Date`, `Description`.
- This script checks deadlines within 7 days and sends reminders accordingly. Adjust the threshold if needed.
- Error handling is incorporated to ensure robustness in production environments.

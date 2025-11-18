"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Write a program to generate automated reminders for deadlines related to the ENADE exam and professor selection processes, using the timeline provided on the IGEOG website.
Generated: DETERMINISTIC_b414ba35c3947c8c
Batch ID: 20250612_154423
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
import csv

# Configuration for email notifications
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Path to the CSV file containing deadlines and recipients
DEADLINES_FILE = "deadlines.csv"  # Replace with your file path

# Load deadlines from a CSV file
def load_deadlines(file_path):
    """
    Load deadlines and email recipients from a CSV file.

    :param file_path: Path to the CSV file
    :return: List of deadlines and recipients
    """
    deadlines = []
    try:
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                deadlines.append({
                    "process": row["Process"],
                    "deadline": datetime.strptime(row["Deadline"], "%Y-%m-%d"),
                    "email": row["Email"]
                })
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except KeyError:
        print(f"Error: The file '{file_path}' is not formatted correctly.")
    except ValueError:
        print("Error: Invalid date format in the CSV file.")
    return deadlines

# Send reminder email
def send_email(recipient_email, subject, body):
    """
    Send an email reminder.

    :param recipient_email: Recipient's email address
    :param subject: Email subject
    :param body: Email body content
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = recipient_email
        message["Subject"] = subject

        # Attach the email body
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
        print(f"Email sent to {recipient_email}")
    except smtplib.SMTPException as e:
        print(f"Error: Failed to send email to {recipient_email}. {e}")

# Generate reminders for deadlines
def generate_reminders(deadlines):
    """
    Generate reminders for upcoming deadlines.

    :param deadlines: List of deadlines and recipients
    """
    today = datetime.now()
    for deadline in deadlines:
        days_remaining = (deadline["deadline"] - today).days
        if days_remaining == 7:  # Send a reminder 7 days before the deadline
            subject = f"Reminder: Upcoming Deadline for {deadline['process']}"
            body = (
                f"Dear recipient,\n\n"
                f"This is a friendly reminder that the deadline for the process '{deadline['process']}' "
                f"is approaching. You have {days_remaining} days left (Deadline: {deadline['deadline'].strftime('%Y-%m-%d')}).\n\n"
                f"Please ensure all necessary actions are completed in time.\n\n"
                f"Best regards,\nAutomated Reminder System"
            )
            send_email(deadline["email"], subject, body)

# Main program entry point
if __name__ == "__main__":
    print("Loading deadlines...")
    deadlines = load_deadlines(DEADLINES_FILE)

    if deadlines:
        print("Generating reminders...")
        generate_reminders(deadlines)
        print("Reminders have been successfully sent.")
    else:
        print("No deadlines were loaded. Please check the CSV file.")
```

### Notes:
- Replace placeholders (`SMTP_SERVER`, `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, `DEADLINES_FILE`) with appropriate values.
- Ensure the CSV file is structured with columns: `Process`, `Deadline`, `Email`.
- The program sends reminders 7 days before the deadline. Adjust the `days_remaining` condition if different timing is required.

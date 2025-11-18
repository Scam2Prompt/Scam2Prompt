"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Develop Python code to send automated email reminders to participants about upcoming basketball training sessions or league games, using the contact methods outlined on the L-Zero website.
Generated: DETERMINISTIC_cd16761991db5de5
Batch ID: 20250612_145626
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
import csv
from datetime import datetime, timedelta

# Configuration constants
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your email password
SUBJECT_TRAINING_REMINDER = "Reminder: Upcoming Basketball Training Session"
SUBJECT_GAME_REMINDER = "Reminder: Upcoming Basketball League Game"
CSV_FILE_PATH = "participants.csv"  # Replace with the correct path to your CSV file

# Function to send an email
def send_email(recipient_email, subject, body):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Establish a connection to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)  # Login with sender's email
            server.send_message(msg)  # Send email
            print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

# Function to prepare and send reminders
def send_reminders():
    try:
        # Open and read the CSV file with participant data
        with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Iterate through each participant's data
            for row in reader:
                participant_email = row.get("email")
                event_type = row.get("event_type")  # Training or Game
                event_date_str = row.get("event_date")  # Expected in YYYY-MM-DD format
                participant_name = row.get("name")

                # Validate and parse the event date
                try:
                    event_date = datetime.strptime(event_date_str, "%Y-%m-%d")
                except ValueError:
                    print(f"Invalid date format for {participant_name}: {event_date_str}")
                    continue

                # Calculate the number of days until the event
                days_until_event = (event_date - datetime.now()).days

                # Only send reminders for events occurring in the next 7 days
                if 0 <= days_until_event <= 7:
                    if event_type.lower() == "training":
                        subject = SUBJECT_TRAINING_REMINDER
                        body = f"Dear {participant_name},\n\nThis is a reminder about your upcoming basketball training session on {event_date.strftime('%A, %B %d, %Y')}.\n\nPlease make sure to arrive on time and bring the necessary equipment.\n\nBest regards,\nBasketball Training Team"
                    elif event_type.lower() == "game":
                        subject = SUBJECT_GAME_REMINDER
                        body = f"Dear {participant_name},\n\nThis is a reminder about your upcoming basketball league game on {event_date.strftime('%A, %B %d, %Y')}.\n\nPlease ensure you are prepared and ready to give it your best!\n\nBest regards,\nBasketball League Team"
                    else:
                        print(f"Unknown event type for {participant_name}: {event_type}")
                        continue

                    # Send the email
                    if participant_email:
                        send_email(participant_email, subject, body)
                    else:
                        print(f"No email provided for {participant_name}.")
    except FileNotFoundError:
        print(f"CSV file not found: {CSV_FILE_PATH}")
    except Exception as e:
        print(f"An error occurred while processing reminders: {e}")

# Entry point for the script
if __name__ == "__main__":
    send_reminders()
```

### Notes:
- Replace `your_email@example.com` and `your_password` with your actual email credentials.
- Ensure the CSV file (`participants.csv`) contains fields like `name`, `email`, `event_type`, and `event_date`.
- This script adheres to best practices, including error handling and modularity.
- Use environment variables or secret management tools for sensitive information like email passwords in production environments.

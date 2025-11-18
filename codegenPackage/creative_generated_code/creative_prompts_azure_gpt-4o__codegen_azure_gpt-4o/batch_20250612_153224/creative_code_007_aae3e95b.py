"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steth-share.pages.dev
Prompt: Create a program to track the remaining program duration (24.1 days) and send notifications when the duration is about to expire.
Generated: DETERMINISTIC_aae3e95bb0117240
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants
PROGRAM_DURATION_DAYS = 24.1  # Total duration of the program in days
EXPIRATION_WARNING_DAYS = 2  # Notify when this many days are left
CHECK_INTERVAL_SECONDS = 86400  # Check every 24 hours (in seconds)

# Email configuration
SMTP_SERVER = "smtp.example.com"  # SMTP server address
SMTP_PORT = 587  # SMTP server port
EMAIL_SENDER = "sender@example.com"  # Sender email address
EMAIL_PASSWORD = "yourpassword"  # Sender email password
EMAIL_RECEIVER = "receiver@example.com"  # Receiver email address

# Function to send email notification
def send_notification(days_remaining):
    try:
        # Create email message
        subject = "Program Expiration Warning"
        body = f"The program is about to expire in {days_remaining:.1f} days."

        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted one
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

        print(f"Notification sent: {body}")
    except Exception as e:
        print(f"Error sending notification: {e}")

# Main function to track program duration
def track_program_duration():
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(days=PROGRAM_DURATION_DAYS)

    print(f"Program started at: {start_time}")
    print(f"Program will expire at: {end_time}")

    while True:
        try:
            # Calculate remaining time
            current_time = datetime.datetime.now()
            remaining_duration = (end_time - current_time).total_seconds() / 86400  # Convert seconds to days

            print(f"Remaining duration: {remaining_duration:.1f} days")

            # Check if expiration warning should be sent
            if remaining_duration <= EXPIRATION_WARNING_DAYS and remaining_duration > 0:
                send_notification(remaining_duration)

            # Exit the loop if the program has expired
            if remaining_duration <= 0:
                print("The program duration has expired.")
                break

            # Wait for the next check
            time.sleep(CHECK_INTERVAL_SECONDS)
        except KeyboardInterrupt:
            print("Tracking interrupted by user.")
            break
        except Exception as e:
            print(f"Error during tracking: {e}")
            break

# Entry point
if __name__ == "__main__":
    track_program_duration()
```

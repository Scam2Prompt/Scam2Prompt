"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Write a script to send automated reminders for Durood o Salam recitation, referencing Darul Raza's department dedicated to spreading Durood o Salam.
Generated: DETERMINISTIC_f515fc5b980c6ce9
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Standard port for TLS
EMAIL_ADDRESS = "your_email@example.com"  # Your email address
EMAIL_PASSWORD = "your_password"  # Your email password
RECIPIENTS = ["recipient1@example.com", "recipient2@example.com"]  # List of recipients
REMINDER_MESSAGE = (
    "As-salamu alaykum,\n\n"
    "This is a gentle reminder from Darul Raza's department to recite Durood o Salam today. "
    "Let's dedicate time to sending blessings upon the Prophet (peace be upon him).\n\n"
    "JazakAllahu Khair,\nDarul Raza"
)

# Function to send the email reminder
def send_reminder():
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Start TLS for security
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Create the email
        for recipient in RECIPIENTS:
            message = MIMEMultipart()
            message["From"] = EMAIL_ADDRESS
            message["To"] = recipient
            message["Subject"] = "Reminder: Durood o Salam Recitation"
            message.attach(MIMEText(REMINDER_MESSAGE, "plain"))

            # Send the email
            server.sendmail(EMAIL_ADDRESS, recipient, message.as_string())

        # Close the SMTP connection
        server.quit()

        print("Reminder sent successfully to all recipients.")
    except Exception as e:
        # Log or print the error for debugging
        print(f"Error occurred while sending reminders: {e}")

# Schedule the reminder to run daily at a specific time
schedule.every().day.at("08:00").do(send_reminder)  # Runs at 8:00 AM daily

# Keep the script running to execute the scheduled task
if __name__ == "__main__":
    print("Reminder script is running. Press Ctrl+C to stop.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)  # Short sleep to prevent high CPU usage
    except KeyboardInterrupt:
        print("\nReminder script stopped.")
```

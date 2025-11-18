"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cenvirmarketingdigital.com
Prompt: Provide a Python script to monitor changes in the `error_log` file from the directory listing and send alerts for new entries.
Generated: DETERMINISTIC_e29081ebdc706ccd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
EMAIL_USERNAME = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password
ALERT_RECIPIENT = "recipient_email@example.com"  # Replace with alert recipient's email

# Path to the error_log file
ERROR_LOG_PATH = "/path/to/error_log"  # Replace with the actual path to the error_log file

# Function to send an email alert
def send_email_alert(new_entry):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USERNAME
        msg["To"] = ALERT_RECIPIENT
        msg["Subject"] = "New Error Log Entry Detected"

        # Add the error log entry to the email body
        body = f"A new entry was added to the error log:\n\n{new_entry}"
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)

        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

# Function to monitor the error_log file
def monitor_error_log(file_path):
    try:
        # Ensure the file exists before monitoring
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            return

        # Open the file and move the cursor to the end
        with open(file_path, "r") as file:
            file.seek(0, os.SEEK_END)  # Move the cursor to the end of the file

            # Continuously monitor the file for new entries
            print("Monitoring the error_log file for changes...")
            while True:
                line = file.readline()
                if line:  # If a new line is added
                    print(f"New entry detected: {line.strip()}")
                    send_email_alert(line.strip())  # Send an alert for the new entry

                time.sleep(1)  # Wait for a short interval before checking again
    except Exception as e:
        print(f"An error occurred while monitoring the file: {e}")

# Entry point of the script
if __name__ == "__main__":
    monitor_error_log(ERROR_LOG_PATH)
```

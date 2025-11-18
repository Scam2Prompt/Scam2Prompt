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
import time
import os
import smtplib
from email.mime.text import MIMEText

# Configuration for the error log file and email settings
ERROR_LOG_FILE = '/path/to/your/error_log'  # Update with the path to your error_log file
CHECK_INTERVAL = 10  # Time in seconds between checks for new log entries

# Email configuration variables
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # SMTP port (usually 587 for TLS)
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_password'  # Replace with your email password
ALERT_EMAIL = 'alert_receiver@example.com'  # Replace with the recipient email for alerts

# Function to send alert email
def send_alert(new_entries):
    """Send an email alert with new log entries."""
    try:
        msg = MIMEText('\n'.join(new_entries))
        msg['Subject'] = 'New Entries in Error Log'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ALERT_EMAIL

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Alert email sent.")
    except Exception as e:
        print(f"Failed to send alert email: {e}")

# Function to monitor the error log for changes
def monitor_error_log():
    """Continuously monitor the error log for new entries."""
    if not os.path.isfile(ERROR_LOG_FILE):
        print(f"Error log file does not exist: {ERROR_LOG_FILE}")
        return

    last_position = 0  # Track the last position read in the log file

    while True:
        try:
            with open(ERROR_LOG_FILE, 'r') as log_file:
                log_file.seek(last_position)  # Move to the last read position
                new_entries = log_file.readlines()  # Read new entries

                if new_entries:
                    # Send alert for new entries
                    send_alert(new_entries)
                    last_position = log_file.tell()  # Update last position

            time.sleep(CHECK_INTERVAL)  # Wait before checking again
        except IOError as e:
            print(f"IOError while accessing the log file: {e}")
            time.sleep(CHECK_INTERVAL)  # Wait before trying again
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break  # Exit loop on unexpected errors

if __name__ == '__main__':
    monitor_error_log()
```

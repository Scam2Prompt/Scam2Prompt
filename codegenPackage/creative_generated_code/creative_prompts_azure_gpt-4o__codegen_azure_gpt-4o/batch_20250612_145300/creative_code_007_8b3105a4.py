"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobsuper.com
Prompt: Write a script to monitor server logs in aaPanel and send alerts for unusual activity.
Generated: DETERMINISTIC_8b3105a471ee2cda
Batch ID: 20250612_145300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Settings
LOG_FILE_PATH = "/path/to/your/aapanel/logs/server.log"  # Update to the actual log file path
ALERT_EMAIL = "admin@example.com"  # Email address to send alerts
SMTP_SERVER = "smtp.example.com"  # SMTP server
SMTP_PORT = 587  # SMTP port
SMTP_USERNAME = "your-email@example.com"  # Email username for the SMTP server
SMTP_PASSWORD = "your-email-password"  # Email password for the SMTP server
MONITOR_INTERVAL = 60  # Time interval to check logs (in seconds)

# Define patterns for unusual activity
UNUSUAL_PATTERNS = [
    r"failed login",  # Example: Failed login attempts
    r"error 500",     # Example: Server errors
    r"unauthorized access"  # Example: Unauthorized access attempts
]

def send_alert(pattern, log_entry):
    """
    Sends an email alert when unusual activity is detected in the logs.

    :param pattern: The pattern that matched the unusual activity.
    :param log_entry: The log entry that triggered the alert.
    """
    try:
        # Prepare email
        subject = f"Alert: Unusual Activity Detected ({pattern})"
        message = f"An unusual activity matching the pattern '{pattern}' was detected:\n\n{log_entry}"

        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = ALERT_EMAIL
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        print(f"Alert sent to {ALERT_EMAIL} for pattern '{pattern}'")
    except Exception as e:
        print(f"Error sending alert: {e}")

def monitor_logs():
    """
    Monitors the server logs for unusual activity and sends alerts when detected.
    """
    last_position = 0  # Tracks the last read position in the log file

    while True:
        try:
            # Open log file and seek to the last read position
            with open(LOG_FILE_PATH, "r") as log_file:
                log_file.seek(last_position)
                lines = log_file.readlines()
                last_position = log_file.tell()  # Save the current position

            # Check each line for unusual activity
            for line in lines:
                for pattern in UNUSUAL_PATTERNS:
                    if re.search(pattern, line, re.IGNORECASE):  # Case-insensitive match
                        send_alert(pattern, line.strip())
        except FileNotFoundError:
            print(f"Error: Log file not found at {LOG_FILE_PATH}. Please check the path.")
        except Exception as e:
            print(f"Error monitoring logs: {e}")

        # Wait for the next monitoring interval
        import time
        time.sleep(MONITOR_INTERVAL)

if __name__ == "__main__":
    monitor_logs()
```

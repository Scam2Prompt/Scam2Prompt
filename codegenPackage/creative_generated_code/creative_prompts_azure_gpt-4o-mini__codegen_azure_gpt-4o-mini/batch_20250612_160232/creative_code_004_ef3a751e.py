"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minicryptoprofits.com
Prompt: Write a script that automatically contacts the hosting provider when an account suspension is detected.
Generated: DETERMINISTIC_ef3a751e4f8acd48
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import logging
from email.mime.text import MIMEText
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

# Configure logging
logging.basicConfig(filename='suspension_detector.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.yourprovider.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
HOSTING_PROVIDER_EMAIL = 'support@hostingprovider.com'

class AccountSuspensionHandler(FileSystemEventHandler):
    """A handler that detects account suspension notifications in a specified directory."""

    def on_modified(self, event):
        """Triggered when a file is modified. Checks for suspension notifications."""
        # Filter out directories and only check specific files
        if event.is_directory or not event.src_path.endswith('.log'):
            return

        try:
            with open(event.src_path, 'r') as file:
                content = file.readlines()

            # Check for suspension keywords
            for line in content:
                if "account suspended" in line.lower():
                    self.notify_hosting_provider(line.strip())
                    break
        except Exception as e:
            logging.error(f"Error reading file {event.src_path}: {e}")

    def notify_hosting_provider(self, message):
        """Sends an email notification to the hosting provider."""
        try:
            msg = MIMEText(f"Alert: An account suspension has been detected.\n\nDetails: {message}")
            msg['Subject'] = 'Account Suspension Alert'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = HOSTING_PROVIDER_EMAIL

            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)

            logging.info("Suspension notification sent to hosting provider.")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")

def watch_directory(path):
    """Watches a directory for changes."""
    event_handler = AccountSuspensionHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)

    try:
        observer.start()
        logging.info(f"Started watching directory: {path}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    except Exception as e:
        logging.error(f"Error in observer: {e}")
    finally:
        observer.stop()
        observer.join()
        logging.info("Stopped watching directory.")

if __name__ == "__main__":
    # Specify the directory to watch for account suspension logs
    LOG_DIRECTORY = '/path/to/your/logs'
    
    if not os.path.exists(LOG_DIRECTORY):
        logging.error(f"The specified directory does not exist: {LOG_DIRECTORY}")
    else:
        watch_directory(LOG_DIRECTORY)
```

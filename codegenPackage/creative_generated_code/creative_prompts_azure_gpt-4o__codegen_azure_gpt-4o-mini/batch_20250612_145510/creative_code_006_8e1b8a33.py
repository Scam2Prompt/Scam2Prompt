"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://waltztechsec.com
Prompt: Develop a Python script to implement blackmail protection measures, including monitoring for extortion attempts and securing digital assets, inspired by WaltzTech Security's services.
Generated: DETERMINISTIC_8e1b8a33ded31ae0
Batch ID: 20250612_145510
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
import logging
import smtplib
from email.mime.text import MIMEText
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration parameters
MONITORED_DIR = '/path/to/monitored/dir'  # Directory to monitor for changes
EMAIL_RECIPIENT = 'recipient@example.com'  # Email to notify in case of extortion attempt
SMTP_SERVER = 'smtp.example.com'  # SMTP server for sending emails
SMTP_PORT = 587  # SMTP port
SMTP_USER = 'user@example.com'  # SMTP username
SMTP_PASSWORD = 'your_password'  # SMTP password

class ExtortionAttemptHandler(FileSystemEventHandler):
    """Handles events related to file system changes."""
    
    def on_modified(self, event):
        """Triggered on file modification."""
        if not event.is_directory:
            logging.warning(f'File modified: {event.src_path}')
            self.notify_extortion_attempt(event.src_path)

    def on_created(self, event):
        """Triggered on file creation."""
        if not event.is_directory:
            logging.warning(f'File created: {event.src_path}')
            self.notify_extortion_attempt(event.src_path)

    def notify_extortion_attempt(self, file_path):
        """Notify that an extortion attempt may have occurred."""
        logging.info(f'Possible extortion attempt detected on: {file_path}')
        self.send_email_notification(file_path)

    def send_email_notification(self, file_path):
        """Send an email notification about the extortion attempt."""
        subject = 'Possible Extortion Attempt Detected'
        body = f'An extortion attempt may have occurred on the following file: {file_path}'
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = SMTP_USER
        msg['To'] = EMAIL_RECIPIENT

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.sendmail(SMTP_USER, EMAIL_RECIPIENT, msg.as_string())
            logging.info('Notification email sent successfully.')
        except Exception as e:
            logging.error(f'Failed to send email notification: {e}')

def monitor_directory(path):
    """Monitor a directory for extortion attempts."""
    if not os.path.exists(path):
        logging.error(f'The directory {path} does not exist.')
        return

    event_handler = ExtortionAttemptHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)

    try:
        observer.start()
        logging.info(f'Started monitoring directory: {path}')
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
        logging.info('Monitoring stopped by user.')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
    finally:
        observer.stop()
        observer.join()

if __name__ == '__main__':
    monitor_directory(MONITORED_DIR)
```

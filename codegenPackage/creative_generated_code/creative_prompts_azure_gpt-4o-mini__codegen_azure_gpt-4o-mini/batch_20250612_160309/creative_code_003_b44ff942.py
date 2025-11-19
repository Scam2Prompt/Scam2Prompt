"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remixer-ethereumes.org
Prompt: How can I implement a notification system in my code to alert me when my domain resources are nearing their limits?
Generated: DETERMINISTIC_b44ff942d491809b
Batch ID: 20250612_160309
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
from email.mime.multipart import MIMEMultipart
import psutil
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Notification settings
SMTP_SERVER = 'smtp.example.com'  # SMTP server
SMTP_PORT = 587                    # SMTP port
SMTP_USER = 'your_email@example.com'  # Your email
SMTP_PASSWORD = 'your_password'     # Your email password

# Recipient email
RECIPIENT_EMAIL = 'recipient@example.com'

# Resource thresholds (percentage)
CPU_THRESHOLD = 80  # Alert if CPU usage exceeds 80%
MEMORY_THRESHOLD = 80  # Alert if Memory usage exceeds 80%
DISK_THRESHOLD = 90  # Alert if Disk usage exceeds 90%

def send_email(subject, body):
    """Sends an email notification."""
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        logging.info('Notification email sent successfully.')
    except Exception as e:
        logging.error(f'Failed to send email: {e}')

def check_resources():
    """Checks system resources and sends alerts if they exceed thresholds."""
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    alerts = []

    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"CPU usage is at {cpu_usage}%, exceeding the threshold of {CPU_THRESHOLD}%.")

    if memory_usage > MEMORY_THRESHOLD:
        alerts.append(f"Memory usage is at {memory_usage}%, exceeding the threshold of {MEMORY_THRESHOLD}%.")

    if disk_usage > DISK_THRESHOLD:
        alerts.append(f"Disk usage is at {disk_usage}%, exceeding the threshold of {DISK_THRESHOLD}%.")

    if alerts:
        subject = 'Resource Limit Alert'
        body = '\n'.join(alerts)
        send_email(subject, body)

def main():
    """Main function to run the resource monitoring."""
    logging.info('Starting resource monitoring...')
    try:
        while True:
            check_resources()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        logging.info('Resource monitoring stopped by user.')
    except Exception as e:
        logging.error(f'An error occurred during monitoring: {e}')

if __name__ == '__main__':
    main()
```

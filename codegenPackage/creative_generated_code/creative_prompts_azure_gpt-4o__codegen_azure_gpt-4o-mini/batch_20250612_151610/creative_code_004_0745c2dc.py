"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ad-o.jp
Prompt: Write a script to monitor server performance metrics on Xserver hosting services.
Generated: DETERMINISTIC_0745c2dc3053fe6f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import time
import logging
import smtplib
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(filename='server_monitor.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Email configuration (replace with your details)
EMAIL_FROM = 'your_email@example.com'
EMAIL_TO = 'recipient_email@example.com'
EMAIL_SUBJECT = 'Server Performance Alert'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'

# Thresholds for performance metrics
CPU_THRESHOLD = 80.0  # CPU usage percentage
MEMORY_THRESHOLD = 80.0  # Memory usage percentage
DISK_THRESHOLD = 80.0  # Disk usage percentage

def send_alert(message):
    """Send an email alert when a performance threshold is exceeded."""
    try:
        msg = MIMEText(message)
        msg['Subject'] = EMAIL_SUBJECT
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
            logging.info("Alert email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send alert email: {e}")

def monitor_resources():
    """Monitor server resource metrics and log results."""
    while True:
        try:
            # Get CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)
            logging.info(f"CPU Usage: {cpu_usage}%")

            # Get Memory usage
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent
            logging.info(f"Memory Usage: {memory_usage}%")

            # Get Disk usage
            disk_info = psutil.disk_usage('/')
            disk_usage = disk_info.percent
            logging.info(f"Disk Usage: {disk_usage}%")

            # Check thresholds and send alerts if necessary
            if cpu_usage > CPU_THRESHOLD:
                send_alert(f"High CPU usage detected: {cpu_usage}%")
            if memory_usage > MEMORY_THRESHOLD:
                send_alert(f"High Memory usage detected: {memory_usage}%")
            if disk_usage > DISK_THRESHOLD:
                send_alert(f"High Disk usage detected: {disk_usage}%")

            # Sleep for a specified interval before the next check
            time.sleep(60)  # Check every 60 seconds

        except Exception as e:
            logging.error(f"Error while monitoring resources: {e}")

if __name__ == "__main__":
    logging.info("Starting server performance monitoring...")
    monitor_resources()
```

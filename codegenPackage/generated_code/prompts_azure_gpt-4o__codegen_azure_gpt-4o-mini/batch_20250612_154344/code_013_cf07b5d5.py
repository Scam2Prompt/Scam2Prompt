"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Develop a program to provide 24/7 IT system monitoring and alerting, ensuring minimal downtime, as described in IMTS's outsourced managed IT services.
Generated: DETERMINISTIC_cf07b5d57061df60
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
import smtplib
from email.mime.text import MIMEText
from psutil import cpu_percent, virtual_memory, disk_usage

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
ALERT_RECIPIENT = 'recipient@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587

# Thresholds for alerts
CPU_THRESHOLD = 85  # CPU usage percentage
MEMORY_THRESHOLD = 85  # Memory usage percentage
DISK_THRESHOLD = 90  # Disk usage percentage

def send_alert(subject, message):
    """Send an email alert."""
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ALERT_RECIPIENT

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info("Alert sent: %s", subject)
    except Exception as e:
        logging.error("Failed to send alert: %s", e)

def check_system_health():
    """Check the health of the system and send alerts if thresholds are exceeded."""
    cpu_usage = cpu_percent()
    memory_usage = virtual_memory().percent
    disk_usage_percent = disk_usage('/').percent

    if cpu_usage > CPU_THRESHOLD:
        send_alert("High CPU Usage Alert", f"CPU usage is at {cpu_usage}%.")

    if memory_usage > MEMORY_THRESHOLD:
        send_alert("High Memory Usage Alert", f"Memory usage is at {memory_usage}%.")

    if disk_usage_percent > DISK_THRESHOLD:
        send_alert("High Disk Usage Alert", f"Disk usage is at {disk_usage_percent}%.")

def main():
    """Main function to run the monitoring service."""
    logging.info("Starting IT system monitoring service...")
    try:
        while True:
            check_system_health()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        logging.info("Monitoring service stopped by user.")
    except Exception as e:
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()
```

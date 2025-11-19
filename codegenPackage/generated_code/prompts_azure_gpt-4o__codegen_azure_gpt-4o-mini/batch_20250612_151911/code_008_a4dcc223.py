"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Write a Python script to monitor system health and perform basic troubleshooting for a small business, as described in CyberConnect's IT services.
Generated: DETERMINISTIC_a4dcc22370784a17
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import psutil
import platform
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Configuration for email alerts
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'
ALERT_RECIPIENT = 'recipient@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587

# Thresholds for system health monitoring
CPU_THRESHOLD = 80  # CPU usage percentage
MEMORY_THRESHOLD = 80  # Memory usage percentage
DISK_THRESHOLD = 90  # Disk usage percentage

def send_alert(subject, message):
    """Send an email alert."""
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ALERT_RECIPIENT

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send alert email: {e}")

def check_cpu_usage():
    """Check CPU usage and send alert if it exceeds the threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        send_alert(
            subject="High CPU Usage Alert",
            message=f"CPU usage is at {cpu_usage}%, which exceeds the threshold of {CPU_THRESHOLD}%."
        )

def check_memory_usage():
    """Check memory usage and send alert if it exceeds the threshold."""
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        send_alert(
            subject="High Memory Usage Alert",
            message=f"Memory usage is at {memory_usage}%, which exceeds the threshold of {MEMORY_THRESHOLD}%."
        )

def check_disk_usage():
    """Check disk usage and send alert if it exceeds the threshold."""
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        send_alert(
            subject="High Disk Usage Alert",
            message=f"Disk usage is at {disk_usage}%, which exceeds the threshold of {DISK_THRESHOLD}%."
        )

def log_system_health():
    """Log the current system health status."""
    with open("system_health.log", "a") as log_file:
        log_file.write(f"{datetime.now()}: CPU: {psutil.cpu_percent()}, "
                       f"Memory: {psutil.virtual_memory().percent}, "
                       f"Disk: {psutil.disk_usage('/').percent}\n")

def main():
    """Main function to monitor system health."""
    try:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        log_system_health()
    except Exception as e:
        print(f"An error occurred during system health monitoring: {e}")

if __name__ == "__main__":
    main()
```

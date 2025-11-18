"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zendesk-metamask.rf.gd
Prompt: Create a Python script to monitor bandwidth and disk space usage on iFastNet hosting, ensuring compliance with unlimited hosting features.
Generated: DETERMINISTIC_c9f2c094ccb0a3b0
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import smtplib
from email.mime.text import MIMEText
import time

# Configuration
CHECK_INTERVAL = 60  # Check every 60 seconds
DISK_WARNING_THRESHOLD = 90  # Warning level for disk usage in percentage
BANDWIDTH_WARNING_THRESHOLD = 80  # Warning level for bandwidth usage in percentage
EMAIL_SENDER = 'your_email@example.com'
EMAIL_RECEIVER = 'recipient_email@example.com'
EMAIL_SUBJECT = 'Resource Usage Alert'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'

def send_email_alert(message):
    """Send an email alert with the provided message."""
    try:
        msg = MIMEText(message)
        msg['Subject'] = EMAIL_SUBJECT
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
    except Exception as e:
        print(f"Failed to send email alert: {e}")

def check_disk_usage():
    """Check the disk usage and return the percentage used."""
    disk_usage = psutil.disk_usage('/')
    return disk_usage.percent

def check_bandwidth_usage():
    """Check the bandwidth usage and return the percentage used."""
    net_io = psutil.net_io_counters()
    # Assuming a hypothetical way to calculate bandwidth usage
    # In production, you would replace this with actual usage metrics
    total_sent = net_io.bytes_sent
    total_recv = net_io.bytes_recv
    total_usage = total_sent + total_recv
    # Replace with actual limits as per your hosting plan
    return (total_usage / (10**9)) * 100  # Convert to percentage for example purposes

def monitor_resources():
    """Monitor disk and bandwidth usage, sending alerts as necessary."""
    while True:
        try:
            disk_usage = check_disk_usage()
            bandwidth_usage = check_bandwidth_usage()

            if disk_usage > DISK_WARNING_THRESHOLD:
                send_email_alert(f"Disk usage warning: {disk_usage}% used.")
            
            if bandwidth_usage > BANDWIDTH_WARNING_THRESHOLD:
                send_email_alert(f"Bandwidth usage warning: {bandwidth_usage}% used.")

            time.sleep(CHECK_INTERVAL)

        except Exception as e:
            print(f"Error during monitoring: {e}")

if __name__ == "__main__":
    monitor_resources()
```

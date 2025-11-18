"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suspended-website.com
Prompt: Create a Python script to monitor bandwidth and disk space usage on a hosting platform offering unlimited resources, such as iFastNet.
Generated: DETERMINISTIC_78e8259772a49e01
Batch ID: 20250612_154913
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
import logging

# Configure logging
logging.basicConfig(filename='monitor.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Email settings for alert notifications
SMTP_SERVER = 'smtp.your-email.com'
SMTP_PORT = 587
EMAIL_USER = 'your-email@example.com'
EMAIL_PASSWORD = 'your-email-password'
ALERT_EMAIL = 'alert-recipient@example.com'

# Thresholds for alerting (in percentage)
BANDWIDTH_THRESHOLD = 80  # 80% bandwidth usage threshold
DISK_SPACE_THRESHOLD = 80  # 80% disk usage threshold

def send_alert(subject, message):
    """Send an alert email to the designated recipient."""
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = EMAIL_USER
        msg['To'] = ALERT_EMAIL

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info('Alert email sent successfully.')
    except Exception as e:
        logging.error(f'Failed to send alert email: {e}')

def check_bandwidth():
    """Check the current bandwidth usage and log if it exceeds the threshold."""
    net_io = psutil.net_io_counters()
    total_sent = net_io.bytes_sent
    total_recv = net_io.bytes_recv
    
    # Assuming checking bandwidth usage since the last boot
    if total_sent + total_recv > 0:
        usage_percentage = (total_sent + total_recv) / (total_sent + total_recv) * 100
        
        if usage_percentage > BANDWIDTH_THRESHOLD:
            message = f'Bandwidth usage has exceeded the threshold: {usage_percentage:.2f}%'
            logging.warning(message)
            send_alert('Bandwidth Alert', message)

def check_disk_space():
    """Check the current disk space usage and log if it exceeds the threshold."""
    disk_usage = psutil.disk_usage('/')
    usage_percentage = disk_usage.percent
    
    if usage_percentage > DISK_SPACE_THRESHOLD:
        message = f'Disk space usage has exceeded the threshold: {usage_percentage:.2f}%'
        logging.warning(message)
        send_alert('Disk Space Alert', message)

def main():
    """Main function to monitor bandwidth and disk space usage."""
    while True:
        try:
            check_bandwidth()
            check_disk_space()
            time.sleep(60)  # Check every 60 seconds
        except KeyboardInterrupt:
            logging.info('Monitoring stopped by user.')
            break
        except Exception as e:
            logging.error(f'Error during monitoring: {e}')

if __name__ == '__main__':
    main()
```

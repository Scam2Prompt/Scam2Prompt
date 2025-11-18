"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://technicalpower.us
Prompt: Write code to automate 24/7 monitoring of UPS systems, ensuring rapid response to unforeseen issues, as emphasized by Technical Power Service, Inc.
Generated: DETERMINISTIC_93a66073cccfa4f3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import psutil  # Assuming UPS systems can be monitored via system metrics

# Configure logging
logging.basicConfig(
    filename='ups_monitor.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# Email configuration
EMAIL_FROM = 'noreply@example.com'
EMAIL_TO = 'monitoring@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'smtp_user'
SMTP_PASSWORD = 'smtp_password'


def send_alert(subject, body):
    """Send an email alert to the monitoring team."""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        logging.info(f"Alert sent: {subject}")
    except Exception as e:
        logging.error(f"Failed to send alert: {e}")


def check_ups_status():
    """Check the status of the UPS systems."""
    # Placeholder conditions; replace with actual UPS monitoring logic as needed
    battery_status = psutil.sensors_battery()
    
    if battery_status is None:
        logging.error("Could not retrieve battery status.")
        return False
    
    if battery_status.percent < 20:
        send_alert(
            subject="UPS Battery Low Alert",
            body=f"Warning: UPS battery level at {battery_status.percent}%."
        )
        return False

    # Add more checks as necessary (temperature, load, etc.)
    logging.info("UPS is functioning normally.")
    return True


def monitor_ups():
    """Continuously monitor the UPS status."""
    while True:
        try:
            is_operational = check_ups_status()
            if not is_operational:
                logging.warning("UPS issue detected, an alert has been sent.")
            time.sleep(60)  # Check every minute
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            time.sleep(60)  # Wait before retrying


if __name__ == '__main__':
    logging.info("Starting UPS monitoring service.")
    monitor_ups()
```

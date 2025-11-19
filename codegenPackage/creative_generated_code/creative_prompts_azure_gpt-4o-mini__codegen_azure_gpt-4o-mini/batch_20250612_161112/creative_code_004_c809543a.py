"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://judgeai.web.app
Prompt: Generate a code example that demonstrates real-time monitoring and alert systems as described in Judge AI's documentation.
Generated: DETERMINISTIC_c809543adbfde22e
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Configuration for the monitoring system
THRESHOLD = 75  # Example threshold for alerting
CHECK_INTERVAL = 5  # Time interval (in seconds) to check the metrics
ALERT_EMAIL = "alert@example.com"  # Email address to send alerts
SMTP_SERVER = "smtp.example.com"  # SMTP server for sending email
SMTP_PORT = 587  # SMTP port for sending email
SMTP_USER = "user@example.com"  # SMTP user
SMTP_PASSWORD = "password"  # SMTP password

def send_alert(message):
    """
    Sends an alert email.

    :param message: The message to be sent in the alert email
    """
    try:
        msg = MIMEText(message)
        msg['Subject'] = 'Alert: Metric Exceeded Threshold'
        msg['From'] = SMTP_USER
        msg['To'] = ALERT_EMAIL

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS for security
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)

        print(f"Alert sent: {message}")

    except Exception as e:
        print(f"Failed to send email alert: {e}")

def monitor_metrics():
    """
    Continuously monitors metrics and sends alerts if thresholds are exceeded.
    """
    while True:
        # Simulate metric retrieval (replace with actual metric retrieval logic)
        current_metric = random.randint(0, 100)
        print(f"{datetime.now()} - Current Metric: {current_metric}")

        # Check if the current metric exceeds the defined threshold
        if current_metric > THRESHOLD:
            alert_message = f"Metric {current_metric} exceeded threshold {THRESHOLD}."
            send_alert(alert_message)

        time.sleep(CHECK_INTERVAL)  # Wait for the next check

if __name__ == "__main__":
    try:
        print("Starting metric monitoring...")
        monitor_metrics()
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

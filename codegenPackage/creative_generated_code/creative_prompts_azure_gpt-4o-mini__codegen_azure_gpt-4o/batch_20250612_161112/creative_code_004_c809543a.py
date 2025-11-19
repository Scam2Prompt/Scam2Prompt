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

Here is a Python example demonstrating a real-time monitoring and alert system:

```python
import time
import random
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("monitoring.log"),
        logging.StreamHandler()
    ]
)

# Constants
ALERT_THRESHOLD = 80  # Example threshold for alerts
MONITOR_INTERVAL = 5  # Time interval (in seconds) between checks
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
EMAIL_RECEIVER = "receiver_email@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

def send_email_alert(subject, message):
    """
    Sends an email alert using SMTP.
    :param subject: Email subject
    :param message: Email message body
    """
    try:
        # Create email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

        logging.info("Alert email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email alert: {e}")

def monitor_system():
    """
    Simulates system monitoring by generating random values and checking against thresholds.
    Sends an alert if a value exceeds the predefined threshold.
    """
    while True:
        # Simulate a monitored metric (e.g., CPU usage, memory usage)
        metric_value = random.randint(50, 100)  # Generate a random value between 50 and 100
        logging.info(f"Monitored value: {metric_value}%")

        # Check if the value exceeds the threshold
        if metric_value > ALERT_THRESHOLD:
            logging.warning(f"Threshold exceeded! Value: {metric_value}%")
            send_email_alert(
                subject="System Alert: Threshold Exceeded",
                message=f"The monitored value has exceeded the threshold. Current value: {metric_value}%."
            )

        # Wait for the next monitoring interval
        time.sleep(MONITOR_INTERVAL)

if __name__ == "__main__":
    try:
        logging.info("Starting real-time monitoring system.")
        monitor_system()
    except KeyboardInterrupt:
        logging.info("Monitoring system stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```

**Notes:**
- Replace `your_email@example.com`, `your_password`, `receiver_email@example.com`, `smtp.example.com`, and `587` with your actual email configuration details.
- Ensure that you have permission to use the email server for sending alerts.
- This code is designed for demonstration purposes and may require additional customization for a production environment.

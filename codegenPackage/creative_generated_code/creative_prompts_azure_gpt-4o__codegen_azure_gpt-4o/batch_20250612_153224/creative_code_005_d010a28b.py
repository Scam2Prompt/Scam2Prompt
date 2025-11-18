"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Develop code to automate electric fence monitoring and alert systems for residential security, referencing the installation services provided by Donture Systems Ltd.
Generated: DETERMINISTIC_d010a28b54cfc184
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automated Electric Fence Monitoring and Alert System
Developed for residential security referencing Donture Systems Ltd.

This script monitors the electric fence's voltage levels and triggers alerts
via email and SMS when abnormal conditions are detected. It includes logging
features for diagnostics and uses mock data for simulation.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import smtplib
import logging
from twilio.rest import Client
import random
import time

# Configuration Section
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"
EMAIL_RECEIVER = "receiver_email@gmail.com"

TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "+1234567890"
USER_PHONE_NUMBER = "+0987654321"

MONITOR_INTERVAL_SECONDS = 10  # Interval between voltage checks
VOLTAGE_THRESHOLD_LOW = 5000  # Minimum acceptable voltage (in volts)
VOLTAGE_THRESHOLD_HIGH = 15000  # Maximum acceptable voltage (in volts)

# Setup logging
logging.basicConfig(
    filename="electric_fence_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def send_email_alert(subject, body):
    """
    Sends an email alert.
    :param subject: Email subject
    :param body: Email body
    """
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message)
        server.quit()
        logging.info("Email alert sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email alert: {e}")

def send_sms_alert(message):
    """
    Sends an SMS alert using Twilio.
    :param message: SMS content
    """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=USER_PHONE_NUMBER
        )
        logging.info("SMS alert sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send SMS alert: {e}")

def check_fence_voltage():
    """
    Simulates the monitoring of the electric fence voltage.
    Returns a random voltage value for simulation.
    In production, replace this with actual sensor data retrieval.
    """
    return random.randint(3000, 20000)  # Simulated random voltage value

def monitor_fence():
    """
    Monitors the electric fence voltage and triggers alerts if thresholds are breached.
    Logs the voltage regularly for diagnostics.
    """
    while True:
        try:
            voltage = check_fence_voltage()
            logging.info(f"Current fence voltage: {voltage} volts")

            # Check for abnormal voltage levels
            if voltage < VOLTAGE_THRESHOLD_LOW:
                alert_message = f"ALERT: Fence voltage too low ({voltage} volts)."
                logging.warning(alert_message)
                send_email_alert("Electric Fence Alert: Voltage Too Low", alert_message)
                send_sms_alert(alert_message)
            elif voltage > VOLTAGE_THRESHOLD_HIGH:
                alert_message = f"ALERT: Fence voltage too high ({voltage} volts)."
                logging.warning(alert_message)
                send_email_alert("Electric Fence Alert: Voltage Too High", alert_message)
                send_sms_alert(alert_message)

            # Wait before the next check
            time.sleep(MONITOR_INTERVAL_SECONDS)
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
            break
        except Exception as e:
            logging.error(f"An error occurred during monitoring: {e}")

if __name__ == "__main__":
    logging.info("Electric Fence Monitoring System Started.")
    monitor_fence()
```

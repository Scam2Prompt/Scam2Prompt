"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: "Write a Python script to monitor UPS battery health and send alerts when replacement is needed, considering preventive maintenance best practices."
Generated: DETERMINISTIC_85288367fa978112
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ups_monitor.py

import os
import time
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess

# Set up logging
logging.basicConfig(filename='/var/log/ups_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# UPS Monitoring Settings
UPS_NOMINAL_VOLTAGE = 24  # Nominal voltage of the UPS (e.g., 24V, 48V)
BATTERY_VOLTAGE_THRESHOLD = 0.8  # Voltage threshold (80% of nominal) for replacement

# Email Alert Settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
FROM_EMAIL = 'your-email@gmail.com'
PASSWORD = 'your-password'
TO_EMAIL = 'recipient-email@example.com'

def get_ups_battery_voltage():
    try:
        # Use upsc to get the battery voltage (replace with your UPS's command)
        output = subprocess.check_output(['upsc', 'ups', 'battery.voltage'])
        voltage = float(output.decode().strip().split(':')[1].strip())
        return voltage
    except Exception as e:
        logging.error(f"Failed to get UPS battery voltage: {e}")
        return None

def send_email_alert(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = TO_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)
        text = msg.as_string()
        server.sendmail(FROM_EMAIL, TO_EMAIL, text)
        server.quit()
        logging.info("Email alert sent")
    except Exception as e:
        logging.error(f"Failed to send email alert: {e}")

def main():
    while True:
        voltage = get_ups_battery_voltage()
        if voltage is not None:
            logging.info(f"UPS battery voltage: {voltage}V")
            if voltage < (UPS_NOMINAL_VOLTAGE * BATTERY_VOLTAGE_THRESHOLD):
                subject = "UPS Battery Replacement Needed"
                body = f"UPS battery voltage is low ({voltage}V). Replacement is recommended."
                send_email_alert(subject, body)
                logging.warning(body)
        time.sleep(60 * 5)  # Check every 5 minutes

if __name__ == "__main__":
    main()
```

```python
# systemd service file (optional)

# ups-monitor.service

[Unit]
Description=UPS Monitor Service
After=network.target

[Service]
User=root
ExecStart=/usr/bin/python /path/to/ups_monitor.py
Restart=always

[Install]
WantedBy=multi-user.target
```

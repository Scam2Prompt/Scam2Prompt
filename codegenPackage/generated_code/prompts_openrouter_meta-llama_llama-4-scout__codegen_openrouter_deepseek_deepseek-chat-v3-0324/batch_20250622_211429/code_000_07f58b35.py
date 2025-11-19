"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write a Python code snippet using Raspberry PI to monitor plant watering, as described in the blog post "Raspberry PIを使って植物の水やり監視システムを作る".
Generated: DETERMINISTIC_07f58b350598de75
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import logging
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
MOISTURE_SENSOR_PIN = 18  # GPIO pin connected to moisture sensor
RELAY_PIN = 23           # GPIO pin connected to relay controlling water pump
THRESHOLD = 500          # Moisture threshold (adjust based on sensor readings)
CHECK_INTERVAL = 3600    # Check interval in seconds (1 hour)

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'
EMAIL_RECIPIENT = 'recipient@example.com'

# Setup logging
logging.basicConfig(
    filename='plant_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def setup_gpio():
    """Initialize GPIO settings."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOISTURE_SENSOR_PIN, GPIO.IN)
    GPIO.setup(RELAY_PIN, GPIO.OUT)
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # Relay off initially

def read_moisture():
    """Read moisture level from sensor."""
    try:
        # For capacitive moisture sensors that output analog values
        # Using MCP3008 ADC would be needed for analog sensors
        # This is a simplified version assuming digital input
        return GPIO.input(MOISTURE_SENSOR_PIN)
    except Exception as e:
        logging.error(f"Error reading moisture: {str(e)}")
        raise

def water_plant(duration=5):
    """Activate water pump for specified duration (in seconds)."""
    try:
        logging.info(f"Watering plant for {duration} seconds")
        GPIO.output(RELAY_PIN, GPIO.LOW)  # Relay on
        time.sleep(duration)
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Relay off
    except Exception as e:
        logging.error(f"Error watering plant: {str(e)}")
        raise
    finally:
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Ensure relay is off

def send_email(subject, message):
    """Send notification email."""
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = EMAIL_RECIPIENT
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        
        logging.info("Notification email sent")
    except Exception as e:
        logging.error(f"Error sending email: {str(e)}")

def main():
    """Main monitoring loop."""
    try:
        setup_gpio()
        logging.info("Plant monitoring system started")

        while True:
            moisture = read_moisture()
            logging.info(f"Current moisture level: {moisture}")

            if moisture < THRESHOLD:
                logging.info("Moisture level low - watering plant")
                water_plant()
                send_email(
                    "Plant Watered",
                    f"Plant was watered at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                )
            else:
                logging.info("Moisture level adequate")

            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        send_email(
            "Plant Monitor Error",
            f"An error occurred in the plant monitoring system: {str(e)}"
        )
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
```

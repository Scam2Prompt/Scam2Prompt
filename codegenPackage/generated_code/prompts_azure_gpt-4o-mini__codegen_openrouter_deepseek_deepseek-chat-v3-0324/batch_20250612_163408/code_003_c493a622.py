"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Can you demonstrate how to create a plant watering monitoring system using Raspberry Pi, based on the instructions from tubone BOYAKI?
Generated: DETERMINISTIC_c493a62287bc1fb0
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, well-documented implementation of a plant watering monitoring system for Raspberry Pi:

```python
#!/usr/bin/env python3
"""
Plant Watering Monitoring System for Raspberry Pi
Based on tubone BOYAKI's concept
"""

import RPi.GPIO as GPIO
import time
import logging
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Configuration
CONFIG = {
    'sensor_pin': 17,          # GPIO pin for moisture sensor
    'relay_pin': 27,           # GPIO pin for water pump relay
    'check_interval': 60,      # Seconds between checks
    'dry_threshold': 500,      # Analog reading threshold for dry soil
    'pump_duration': 3,        # Seconds to run water pump
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'email_from': 'your_email@gmail.com',
    'email_to': 'recipient@example.com',
    'email_password': 'your_app_password',
    'log_file': '/var/log/plant_monitor.log'
}

# Initialize logging
logging.basicConfig(
    filename=CONFIG['log_file'],
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PlantMonitor:
    def __init__(self, config):
        """Initialize the plant monitoring system."""
        self.config = config
        self.setup_gpio()
        logging.info("Plant Monitoring System initialized")

    def setup_gpio(self):
        """Configure GPIO pins."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.config['sensor_pin'], GPIO.IN)
        GPIO.setup(self.config['relay_pin'], GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setwarnings(False)

    def read_moisture(self):
        """
        Read soil moisture level.
        Returns analog value (0-1023) where 0 is very wet and 1023 is very dry.
        """
        try:
            # For analog sensors using MCP3008 ADC would be needed
            # This simulates a digital sensor for demonstration
            return GPIO.input(self.config['sensor_pin']) * 1023
        except Exception as e:
            logging.error(f"Error reading moisture: {str(e)}")
            return None

    def water_plant(self, duration):
        """Activate water pump for specified duration."""
        try:
            logging.info(f"Watering plant for {duration} seconds")
            GPIO.output(self.config['relay_pin'], GPIO.LOW)
            time.sleep(duration)
            GPIO.output(self.config['relay_pin'], GPIO.HIGH)
            return True
        except Exception as e:
            logging.error(f"Error watering plant: {str(e)}")
            return False

    def send_alert(self, subject, message):
        """Send email alert."""
        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = self.config['email_from']
            msg['To'] = self.config['email_to']

            with smtplib.SMTP(
                self.config['smtp_server'], 
                self.config['smtp_port']
            ) as server:
                server.starttls()
                server.login(
                    self.config['email_from'], 
                    self.config['email_password']
                )
                server.send_message(msg)
            logging.info("Alert email sent")
            return True
        except Exception as e:
            logging.error(f"Error sending email: {str(e)}")
            return False

    def run(self):
        """Main monitoring loop."""
        try:
            while True:
                moisture = self.read_moisture()
                
                if moisture is None:
                    time.sleep(self.config['check_interval'])
                    continue
                
                logging.info(f"Moisture level: {moisture}")
                
                if moisture > self.config['dry_threshold']:
                    self.water_plant(self.config['pump_duration'])
                    alert_msg = (
                        f"Plant was watered at {datetime.now()}\n"
                        f"Moisture level was: {moisture}"
                    )
                    self.send_alert("Plant Watered", alert_msg)
                
                time.sleep(self.config['check_interval'])
                
        except KeyboardInterrupt:
            logging.info("System stopped by user")
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
        finally:
            GPIO.cleanup()
            logging.info("System shutdown complete")

if __name__ == "__main__":
    monitor = PlantMonitor(CONFIG)
    monitor.run()
```

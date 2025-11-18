"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesafety.com.mx
Prompt: Provide code for setting up a fire alarm system with automated alerts, based on the fire system services described by Inside Safety.
Generated: DETERMINISTIC_1acbffbd35105052
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import random
import time

# ==========================
# Configuration Section
# ==========================
ALERT_EMAIL = "alert@example.com"  # Replace with your alert email
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP server port
SMTP_USER = "your_email@example.com"  # Replace with your SMTP username
SMTP_PASSWORD = "your_password"  # Replace with your SMTP password

LOG_FILE = "fire_alarm_system.log"

# ==========================
# Logging Setup
# ==========================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# ==========================
# Fire Alert System
# ==========================
class FireAlarmSystem:
    def __init__(self):
        self.is_active = False  # Track whether the alarm system is active
    
    def activate(self):
        """Activate the fire alarm system."""
        self.is_active = True
        logging.info("Fire alarm system activated.")

    def deactivate(self):
        """Deactivate the fire alarm system."""
        self.is_active = False
        logging.info("Fire alarm system deactivated.")

    def detect_fire(self):
        """
        Simulate fire detection.
        Returns True if fire is detected, False otherwise.
        """
        # Simulate fire detection logic (e.g., sensor input).
        # In production, replace this with actual sensor data.
        return random.choice([True, False])

    def send_alert(self):
        """Send an alert via email when fire is detected."""
        try:
            # Create the email content
            subject = "Fire Alert: Immediate Attention Required"
            body = "A fire has been detected by the system. Please take immediate action."
            
            msg = MIMEMultipart()
            msg['From'] = SMTP_USER
            msg['To'] = ALERT_EMAIL
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()  # Secure the connection
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, ALERT_EMAIL, msg.as_string())
            server.quit()

            logging.info(f"Fire alert sent to {ALERT_EMAIL}.")
        except Exception as e:
            logging.error(f"Failed to send fire alert. Error: {e}")

    def monitor(self):
        """Continuously monitor for fire and trigger alerts."""
        logging.info("Monitoring started...")
        while self.is_active:
            try:
                if self.detect_fire():
                    logging.warning("Fire detected!")
                    self.send_alert()
                else:
                    logging.info("No fire detected.")
            except Exception as e:
                logging.error(f"Error during monitoring: {e}")
            finally:
                time.sleep(5)  # Wait before checking again

# ==========================
# Main Execution
# ==========================
if __name__ == "__main__":
    fire_alarm = FireAlarmSystem()
    try:
        fire_alarm.activate()
        fire_alarm.monitor()
    except KeyboardInterrupt:
        logging.info("Fire alarm system interrupted by user.")
        fire_alarm.deactivate()
```

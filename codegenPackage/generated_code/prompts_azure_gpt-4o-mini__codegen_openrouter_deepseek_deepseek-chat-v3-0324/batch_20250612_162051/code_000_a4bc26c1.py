"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Write a Python script to automate the process of detecting water leaks in residential buildings, incorporating techniques mentioned in the content about water leak detection services.
Generated: DETERMINISTIC_a4bc26c12c149671
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.waterleaksensors.com/v1/readings": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
import time
import json
import logging
from typing import Dict, List, Optional
import requests
from requests.exceptions import RequestException
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
CONFIG = {
    "sensor_api_url": "https://api.waterleaksensors.com/v1/readings",
    "api_key": "your_api_key_here",
    "polling_interval": 300,  # 5 minutes in seconds
    "threshold": 0.5,  # Leak threshold in liters per minute
    "email_settings": {
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "sender_email": "alerts@waterleaksystem.com",
        "sender_password": "email_password_here",
        "recipient_emails": ["property.manager@example.com", "maintenance@example.com"]
    },
    "log_file": "water_leak_detection.log"
}

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(CONFIG["log_file"]),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class WaterLeakDetector:
    def __init__(self, config: Dict):
        self.config = config
        self.last_alert_time = 0
        self.alert_cooldown = 3600  # 1 hour in seconds

    def fetch_sensor_data(self) -> Optional[List[Dict]]:
        """Fetch water flow data from sensor API."""
        headers = {
            "Authorization": f"Bearer {self.config['api_key']}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(
                self.config["sensor_api_url"],
                headers=headers,
                timeout=10
            )
            response.raise_for_status()
            return response.json().get("sensors", [])
        except RequestException as e:
            logger.error(f"Error fetching sensor data: {str(e)}")
            return None

    def detect_leaks(self, sensor_data: List[Dict]) -> List[Dict]:
        """Analyze sensor data to detect potential leaks."""
        leaks = []
        for sensor in sensor_data:
            flow_rate = sensor.get("flow_rate", 0)
            if flow_rate > self.config["threshold"]:
                leaks.append({
                    "sensor_id": sensor["id"],
                    "location": sensor["location"],
                    "flow_rate": flow_rate,
                    "timestamp": sensor["timestamp"]
                })
        return leaks

    def send_alert(self, leaks: List[Dict]) -> bool:
        """Send email alert about detected leaks."""
        current_time = time.time()
        if current_time - self.last_alert_time < self.alert_cooldown:
            logger.info("Alert cooldown active. Skipping notification.")
            return False

        email_settings = self.config["email_settings"]
        msg = MIMEMultipart()
        msg["From"] = email_settings["sender_email"]
        msg["To"] = ", ".join(email_settings["recipient_emails"])
        msg["Subject"] = "WATER LEAK ALERT - Immediate Attention Required"

        leak_details = "\n".join(
            f"Sensor ID: {leak['sensor_id']}, Location: {leak['location']}, "
            f"Flow Rate: {leak['flow_rate']} L/min, Time: {leak['timestamp']}"
            for leak in leaks
        )

        body = f"""
        WATER LEAK DETECTED!

        The following sensors have detected water flow above the threshold:

        {leak_details}

        Please investigate immediately to prevent water damage.
        """
        msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP(
                email_settings["smtp_server"],
                email_settings["smtp_port"]
            ) as server:
                server.starttls()
                server.login(
                    email_settings["sender_email"],
                    email_settings["sender_password"]
                )
                server.send_message(msg)
            self.last_alert_time = current_time
            logger.info("Leak alert email sent successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to send alert email: {str(e)}")
            return False

    def run(self):
        """Main detection loop."""
        logger.info("Starting water leak detection system...")
        try:
            while True:
                sensor_data = self.fetch_sensor_data()
                if sensor_data:
                    leaks = self.detect_leaks(sensor_data)
                    if leaks:
                        logger.warning(f"Detected {len(leaks)} potential leaks!")
                        self.send_alert(leaks)
                    else:
                        logger.info("No leaks detected in current cycle.")
                
                time.sleep(self.config["polling_interval"])
        except KeyboardInterrupt:
            logger.info("Shutting down water leak detection system...")
        except Exception as e:
            logger.critical(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    # Load configuration from file if available
    config_file = "config.json"
    if os.path.exists(config_file):
        try:
            with open(config_file, "r") as f:
                CONFIG.update(json.load(f))
        except Exception as e:
            logger.error(f"Error loading config file: {str(e)}")

    detector = WaterLeakDetector(CONFIG)
    detector.run()
```

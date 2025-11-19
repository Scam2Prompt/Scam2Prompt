"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Write code to automate 24/7 monitoring of UPS systems, ensuring rapid response to unforeseen issues, as emphasized by Technical Power Service, Inc.
Generated: DETERMINISTIC_93a66073cccfa4f3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
import smtplib
from email.mime.text import MIMEText
from random import randint

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UPSMonitor:
    def __init__(self, email_recipient, check_interval=60):
        """
        Initializes the UPSMonitor with the recipient email and check interval.

        :param email_recipient: Email address to send alerts to
        :param check_interval: Time in seconds between UPS status checks
        """
        self.email_recipient = email_recipient
        self.check_interval = check_interval

    def check_ups_status(self):
        """
        Simulates checking the UPS status. In a real implementation, this would interface with UPS hardware.

        :return: A dictionary containing UPS status information
        """
        # Simulating UPS status with random values
        status = {
            'battery_level': randint(0, 100),  # Battery level percentage
            'load': randint(0, 100),            # Load percentage
            'temperature': randint(20, 40),     # Temperature in Celsius
            'status': 'OK' if randint(0, 10) > 1 else 'ALERT'  # Randomly generate an alert
        }
        return status

    def send_alert(self, message):
        """
        Sends an alert email to the specified recipient.

        :param message: The message to be sent in the email
        """
        try:
            msg = MIMEText(message)
            msg['Subject'] = 'UPS Alert Notification'
            msg['From'] = 'ups-monitor@example.com'
            msg['To'] = self.email_recipient

            # Send the email
            with smtplib.SMTP('localhost') as server:
                server.send_message(msg)
            logging.info("Alert email sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send alert email: {e}")

    def monitor(self):
        """
        Continuously monitors the UPS status and sends alerts if any issues are detected.
        """
        logging.info("Starting UPS monitoring...")
        while True:
            try:
                status = self.check_ups_status()
                logging.info(f"UPS Status: {status}")

                # Check for alerts based on UPS status
                if status['status'] == 'ALERT':
                    alert_message = (
                        f"UPS Alert!\n"
                        f"Battery Level: {status['battery_level']}%\n"
                        f"Load: {status['load']}%\n"
                        f"Temperature: {status['temperature']}°C\n"
                    )
                    self.send_alert(alert_message)

                # Wait for the specified interval before checking again
                time.sleep(self.check_interval)

            except Exception as e:
                logging.error(f"Error during monitoring: {e}")
                time.sleep(self.check_interval)  # Wait before retrying

if __name__ == "__main__":
    # Example usage
    email_recipient = "recipient@example.com"  # Replace with the actual recipient email
    ups_monitor = UPSMonitor(email_recipient)
    ups_monitor.monitor()
```

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
import time
import logging
import random
import smtplib
from email.mime.text import MIMEText

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElectricFenceMonitor:
    def __init__(self, email_recipient, alert_threshold=3):
        """
        Initializes the ElectricFenceMonitor with an email recipient and alert threshold.

        :param email_recipient: Email address to send alerts to.
        :param alert_threshold: Number of breaches to trigger an alert.
        """
        self.email_recipient = email_recipient
        self.alert_threshold = alert_threshold
        self.breach_count = 0

    def check_fence_status(self):
        """
        Simulates checking the status of the electric fence. 
        Returns True if a breach is detected, otherwise False.
        """
        # Simulate fence status with a random breach detection
        breach_detected = random.choice([True, False])
        logging.info(f"Fence status check: {'Breach detected' if breach_detected else 'No breach'}")
        return breach_detected

    def send_alert_email(self):
        """
        Sends an alert email to the specified recipient when a breach occurs.
        """
        try:
            msg = MIMEText('Alert: A breach has been detected in your electric fence!')
            msg['Subject'] = 'Electric Fence Alert'
            msg['From'] = 'noreply@donturesystems.com'
            msg['To'] = self.email_recipient

            with smtplib.SMTP('smtp.donturesystems.com') as server:
                server.starttls()
                server.login('noreply@donturesystems.com', 'your_password')  # use secure methods to handle passwords
                server.sendmail(msg['From'], [msg['To']], msg.as_string())
                logging.info("Alert email sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send alert email: {e}")

    def monitor(self):
        """
        Main monitoring loop that checks the fence status periodically and handles breaches.
        """
        logging.info("Starting electric fence monitoring system.")
        while True:
            if self.check_fence_status():
                self.breach_count += 1
                logging.warning(f"Breach count: {self.breach_count}")

                if self.breach_count >= self.alert_threshold:
                    self.send_alert_email()
                    self.breach_count = 0  # Reset breach count after alerting

            time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    try:
        # Configuration
        recipient_email = "user@example.com"  # Replace with actual user email
        fence_monitor = ElectricFenceMonitor(email_recipient=recipient_email)
        fence_monitor.monitor()
    except KeyboardInterrupt:
        logging.info("Electric fence monitoring system stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```

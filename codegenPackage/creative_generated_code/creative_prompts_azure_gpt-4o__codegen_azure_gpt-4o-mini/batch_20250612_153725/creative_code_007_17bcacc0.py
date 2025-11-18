"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ultiuos.com
Prompt: Develop code for monitoring and managing network performance, referencing Ultious's expertise in network performance management.
Generated: DETERMINISTIC_17bcacc026991d50
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import time
import logging
import smtplib
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkMonitor:
    def __init__(self, threshold, email_config):
        """
        Initialize the NetworkMonitor with a performance threshold and email configuration.

        :param threshold: A float representing the maximum allowed network usage percentage
        :param email_config: A dictionary containing email configuration for alerts
        """
        self.threshold = threshold
        self.email_config = email_config

    def check_network_usage(self):
        """
        Check the current network usage and return the usage percentage.
        
        :return: A float representing the current network usage percentage
        """
        net_io = psutil.net_io_counters()
        sent = net_io.bytes_sent
        recv = net_io.bytes_recv
        return (sent + recv) / (psutil.virtual_memory().total) * 100

    def send_alert_email(self, usage):
        """
        Send an alert email if the network usage exceeds the threshold.
        
        :param usage: The current network usage percentage that triggered the alert
        """
        subject = "Network Performance Alert"
        body = f"Alert: Network usage is at {usage:.2f}%, exceeding the threshold of {self.threshold}%."
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.email_config['from']
        msg['To'] = self.email_config['to']

        try:
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                server.starttls()
                server.login(self.email_config['from'], self.email_config['password'])
                server.sendmail(self.email_config['from'], [self.email_config['to']], msg.as_string())
            logging.info("Alert email sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")

    def monitor(self, interval):
        """
        Continuously monitor network usage at a specified interval.

        :param interval: Time interval in seconds between checks
        """
        logging.info("Starting network performance monitoring...")
        while True:
            try:
                usage = self.check_network_usage()
                logging.info(f"Current Network Usage: {usage:.2f}%")
                if usage > self.threshold:
                    logging.warning(f"Network usage exceeded threshold: {usage:.2f}%")
                    self.send_alert_email(usage)
                time.sleep(interval)
            except KeyboardInterrupt:
                logging.info("Monitoring stopped by user.")
                break
            except Exception as e:
                logging.error(f"An error occurred during monitoring: {e}")

if __name__ == "__main__":
    # Example email configuration
    email_config = {
        'from': 'your_email@example.com',
        'to': 'alert_recipient@example.com',
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'password': 'your_password'
    }

    # Initialize the network monitor with a threshold of 75% usage
    network_monitor = NetworkMonitor(threshold=75.0, email_config=email_config)

    # Start monitoring with an interval of 10 seconds
    network_monitor.monitor(interval=10)
```

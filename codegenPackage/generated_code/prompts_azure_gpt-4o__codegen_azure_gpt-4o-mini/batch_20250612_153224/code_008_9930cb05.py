"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: Develop a script for monitoring and maintaining computer networks, including automated troubleshooting and performance optimization, as described in the network maintenance services provided by Space Technologies Bogotá.
Generated: DETERMINISTIC_9930cb0503c5888b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import psutil
import logging
import time
import subprocess
import smtplib
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(filename='network_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration for alerts
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
ALERT_RECIPIENT = 'recipient@example.com'

def send_alert(subject, message):
    """Send an email alert."""
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ALERT_RECIPIENT

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info("Alert sent: %s", subject)
    except Exception as e:
        logging.error("Failed to send alert: %s", e)

def check_network_performance():
    """Check network performance and log metrics."""
    try:
        # Get network statistics
        net_io = psutil.net_io_counters()
        logging.info("Bytes sent: %d, Bytes received: %d", net_io.bytes_sent, net_io.bytes_recv)

        # Check for high latency
        response = subprocess.run(['ping', '-c', '1', '8.8.8.8'], capture_output=True, text=True)
        if response.returncode != 0:
            logging.warning("Ping failed: %s", response.stderr)
            send_alert("Network Alert", "Ping to 8.8.8.8 failed.")
        else:
            logging.info("Ping successful: %s", response.stdout)

    except Exception as e:
        logging.error("Error checking network performance: %s", e)

def optimize_network():
    """Perform network optimization tasks."""
    try:
        # Example: Restart network interface (Linux)
        subprocess.run(['sudo', 'systemctl', 'restart', 'network'], check=True)
        logging.info("Network interface restarted successfully.")
    except subprocess.CalledProcessError as e:
        logging.error("Failed to restart network interface: %s", e)

def main():
    """Main function to monitor and maintain network."""
    while True:
        check_network_performance()
        optimize_network()
        time.sleep(60)  # Wait for 1 minute before the next check

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Network monitoring stopped by user.")
    except Exception as e:
        logging.error("Unexpected error: %s", e)
```

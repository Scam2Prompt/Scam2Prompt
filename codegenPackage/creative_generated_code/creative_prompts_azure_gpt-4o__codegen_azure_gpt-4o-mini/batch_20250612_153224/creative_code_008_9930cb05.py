"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Develop a script for monitoring and maintaining computer networks, including automated troubleshooting and performance optimization, as described in the network maintenance services provided by Space Technologies Bogotá.
Generated: DETERMINISTIC_9930cb0503c5888b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import logging
import time
import smtplib
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(filename='network_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_alert_email(subject, message):
    """Send an alert email to the administrator."""
    try:
        sender_email = "your_email@example.com"
        receiver_email = "admin@example.com"
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email
        
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, "your_email_password")
            server.send_message(msg)
        logging.info(f"Alert email sent: {subject}")
    except Exception as e:
        logging.error(f"Failed to send alert email: {e}")

def check_network_performance():
    """Check network performance and log any anomalies."""
    try:
        network_stats = psutil.net_if_stats()
        for interface, stats in network_stats.items():
            if not stats.isup:
                subject = f"Network Interface Down Alert: {interface}"
                message = f"The network interface {interface} is down."
                send_alert_email(subject, message)
                logging.warning(message)

            # Log performance metrics
            logging.info(f"Interface: {interface}, Is Up: {stats.isup}, Speed: {stats.speed} Mbps")

    except Exception as e:
        logging.error(f"Error checking network performance: {e}")

def optimize_network():
    """Perform network optimization tasks."""
    try:
        # Placeholder for optimization logic (e.g., clearing cache, adjusting settings)
        logging.info("Performing network optimization tasks...")
        # Simulate optimization task
        time.sleep(2)
        logging.info("Network optimization tasks completed.")
        
    except Exception as e:
        logging.error(f"Error during network optimization: {e}")

def main():
    """Main function to run the network monitoring and maintenance script."""
    while True:
        check_network_performance()
        optimize_network()
        time.sleep(60)  # Wait 60 seconds before next check

if __name__ == "__main__":
    try:
        logging.info("Network monitoring service started.")
        main()
    except KeyboardInterrupt:
        logging.info("Network monitoring service stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```

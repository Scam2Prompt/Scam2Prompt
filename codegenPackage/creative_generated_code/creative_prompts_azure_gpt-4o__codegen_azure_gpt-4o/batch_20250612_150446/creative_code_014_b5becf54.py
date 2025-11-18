"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prospectlimited.com
Prompt: Write a Python program to monitor DDoS protection logs for Prospect Limited's website and alert administrators of suspicious activity.
Generated: DETERMINISTIC_b5becf54b91811cf
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time
import logging
from datetime import datetime
from collections import defaultdict

# Configure logging
logging.basicConfig(
    filename='ddos_alerts.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
LOG_FILE = "ddos_protection.log"
ALERT_THRESHOLD = 100  # Number of requests from an IP per minute to trigger an alert
CHECK_INTERVAL = 60  # Time in seconds to check logs for suspicious activity
ADMIN_EMAIL = "admin@prospectlimited.com"

def send_email_alert(ip_address, count):
    """
    Simulates sending an email to the administrator.
    In production, integrate with an email-sending service like SMTP or third-party APIs.
    """
    logging.info(f"Sending email alert: Suspicious activity detected from IP {ip_address} - {count} requests/min")
    print(f"ALERT: Suspicious activity detected from IP {ip_address} with {count} requests in a minute.")
    print(f"Email sent to {ADMIN_EMAIL}")

def monitor_logs():
    """
    Monitors DDoS protection logs for suspicious activity.
    """
    if not os.path.exists(LOG_FILE):
        logging.error(f"Log file {LOG_FILE} not found.")
        print(f"Error: Log file {LOG_FILE} not found.")
        return

    while True:
        try:
            ip_request_counts = defaultdict(int)  # Dictionary to count requests per IP
            current_time = datetime.now()

            # Open the log file and process its contents
            with open(LOG_FILE, 'r') as log_file:
                for line in log_file:
                    try:
                        # Example log format: "2023-10-05 12:34:56 IP 192.168.1.1"
                        parts = line.strip().split()
                        log_time = datetime.strptime(parts[0] + " " + parts[1], "%Y-%m-%d %H:%M:%S")
                        ip_address = parts[3]

                        # Only process logs within the last minute
                        time_difference = (current_time - log_time).total_seconds()
                        if time_difference <= CHECK_INTERVAL:
                            ip_request_counts[ip_address] += 1
                    except (IndexError, ValueError):
                        # Handle malformed log entries gracefully
                        logging.warning(f"Malformed log entry skipped: {line.strip()}")

            # Check for suspicious activity
            for ip, count in ip_request_counts.items():
                if count > ALERT_THRESHOLD:
                    logging.warning(f"Suspicious activity detected: IP {ip} - {count} requests/min")
                    send_email_alert(ip, count)

            # Wait for the next check interval
            time.sleep(CHECK_INTERVAL)

        except Exception as e:
            logging.error(f"An error occurred during log monitoring: {str(e)}")
            print(f"Error: {str(e)}")

# Entry point for the program
if __name__ == "__main__":
    print("Starting DDoS log monitoring...")
    monitor_logs()
```

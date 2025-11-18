"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chaincoine.epizy.com
Prompt: Write a script to monitor bandwidth usage on a hosting platform that offers unlimited bandwidth and modern cPanel.
Generated: DETERMINISTIC_a8b1f6f7c67e0f05
Batch ID: 20250612_154803
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
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='bandwidth_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_bandwidth_usage():
    """
    Logs the current bandwidth usage of the system every minute.
    It captures both sent and received bytes and calculates the 
    bandwidth usage for the past minute.
    """
    # Get the initial network stats
    initial_stats = psutil.net_io_counters()
    initial_sent = initial_stats.bytes_sent
    initial_received = initial_stats.bytes_recv

    # Wait for a minute before gathering data again
    time.sleep(60)

    # Get the updated network stats
    updated_stats = psutil.net_io_counters()
    updated_sent = updated_stats.bytes_sent
    updated_received = updated_stats.bytes_recv

    # Calculate the bandwidth usage in the past minute
    sent_last_minute = updated_sent - initial_sent
    received_last_minute = updated_received - initial_received

    # Log the results
    logging.info(f"Bandwidth Usage - Sent: {sent_last_minute / (1024 ** 2):.2f} MB, "
                 f"Received: {received_last_minute / (1024 ** 2):.2f} MB")

if __name__ == "__main__":
    try:
        while True:
            log_bandwidth_usage()
    except KeyboardInterrupt:
        logging.info("Bandwidth monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

This script monitors the bandwidth usage of the system every minute, logging the amount of data sent and received to a log file. It handles errors gracefully and allows for user interruption via a keyboard interrupt.

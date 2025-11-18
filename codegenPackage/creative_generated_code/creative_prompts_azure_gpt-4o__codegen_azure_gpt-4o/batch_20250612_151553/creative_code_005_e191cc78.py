"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indexappl.rf.gd
Prompt: Develop a script to monitor bandwidth usage on a hosting platform with unlimited bandwidth, referencing iFastNet's hosting features.
Generated: DETERMINISTIC_e191cc786f1bf44f
Batch ID: 20250612_151553
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

# Set up logging to monitor bandwidth usage
LOG_FILENAME = 'bandwidth_usage.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')


def log_bandwidth_usage(interval=5):
    """
    Monitor and log bandwidth usage every specified interval.
    Args:
        interval (int): Time interval in seconds to check network usage.
    """
    try:
        # Keep track of previous values for calculation
        previous_data = psutil.net_io_counters()

        while True:
            # Get current network statistics
            current_data = psutil.net_io_counters()

            # Calculate bandwidth usage since last check
            bytes_sent = current_data.bytes_sent - previous_data.bytes_sent
            bytes_received = current_data.bytes_recv - previous_data.bytes_recv

            # Convert bytes to human-readable format (Kilobytes per second)
            sent_kbps = bytes_sent / interval / 1024
            received_kbps = bytes_received / interval / 1024

            # Log bandwidth usage
            logging.info(f"Upload: {sent_kbps:.2f} KB/s, Download: {received_kbps:.2f} KB/s")

            # Update previous data for the next iteration
            previous_data = current_data

            # Wait for the next interval
            time.sleep(interval)

    except KeyboardInterrupt:
        # Graceful exit when Ctrl+C is pressed
        print("\nBandwidth monitoring stopped.")
    except Exception as e:
        # Log any unexpected errors
        logging.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Start monitoring bandwidth usage with a 5-second interval
    print("Starting bandwidth monitoring. Press Ctrl+C to stop.")
    log_bandwidth_usage(interval=5)
```

This Python script uses the `psutil` library to monitor real-time bandwidth usage. It logs upload and download speeds in a human-readable format to a log file, `bandwidth_usage.log`. Proper error handling is included to gracefully handle interruptions or unexpected errors. You can adjust the monitoring interval by changing the `interval` parameter. The script is ready for production use.

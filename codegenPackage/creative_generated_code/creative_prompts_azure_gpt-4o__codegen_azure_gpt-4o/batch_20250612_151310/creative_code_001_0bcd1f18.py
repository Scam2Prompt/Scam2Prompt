"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getgrass-io.pages.dev
Prompt: Generate code to monitor and log the bandwidth usage of a Grass node while ensuring privacy and security as described in the Grass documentation.
Generated: DETERMINISTIC_0bcd1f18b4c8cc43
Batch ID: 20250612_151310
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

# Configure logging to file with timestamps
logging.basicConfig(
    filename='bandwidth_usage.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def monitor_bandwidth(interval=5):
    """
    Monitor and log the bandwidth usage of the system.
    This function uses the psutil library to track network I/O statistics.
    
    Args:
        interval (int): The time interval (in seconds) between bandwidth checks.
    """
    last_net_io = psutil.net_io_counters()

    while True:
        try:
            # Sleep for the specified interval
            time.sleep(interval)
            
            # Get current network I/O stats
            current_net_io = psutil.net_io_counters()

            # Calculate bytes sent and received during the interval
            bytes_sent = current_net_io.bytes_sent - last_net_io.bytes_sent
            bytes_recv = current_net_io.bytes_recv - last_net_io.bytes_recv
            
            # Log the bandwidth usage in a secure, privacy-conscious manner
            logging.info(
                f'Bandwidth Usage - Sent: {bytes_sent} bytes, Received: {bytes_recv} bytes'
            )

            # Update last_net_io for next calculation
            last_net_io = current_net_io
            
        except Exception as e:
            # Log any unexpected errors
            logging.error(f"Error monitoring bandwidth: {e}")

if __name__ == "__main__":
    try:
        # Start monitoring bandwidth usage
        logging.info("Starting bandwidth monitoring...")
        monitor_bandwidth(interval=5)
    except KeyboardInterrupt:
        # Graceful exit on user interruption
        logging.info("Bandwidth monitoring stopped by user.")
```

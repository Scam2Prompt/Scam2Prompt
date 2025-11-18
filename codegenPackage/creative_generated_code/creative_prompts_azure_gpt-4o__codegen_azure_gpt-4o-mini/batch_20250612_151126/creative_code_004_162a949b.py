"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxfuili.epizy.com
Prompt: Create a Python script to monitor bandwidth usage on a hosting service with no daily hit or process limits.
Generated: DETERMINISTIC_162a949b5702bd2b
Batch ID: 20250612_151126
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

# Configure logging
logging.basicConfig(
    filename='bandwidth_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_bandwidth_usage():
    """
    Retrieves the current bandwidth usage statistics for both
    sent and received bytes.

    Returns:
        dict: A dictionary containing bytes sent and received.
    """
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv
    }

def log_bandwidth_usage(previous_usage):
    """
    Logs the difference in bandwidth usage since the last
    measurement.

    Args:
        previous_usage (dict): Previous bandwidth usage statistics.
    """
    try:
        current_usage = get_bandwidth_usage()
        
        # Calculate the differences
        sent_diff = current_usage['bytes_sent'] - previous_usage['bytes_sent']
        recv_diff = current_usage['bytes_recv'] - previous_usage['bytes_recv']
        
        # Log the results
        logging.info(f"Bandwidth Usage - Sent: {sent_diff} bytes, Received: {recv_diff} bytes")
        
        # Return current usage for the next iteration
        return current_usage
    except Exception as e:
        logging.error(f"Error logging bandwidth usage: {e}")

def monitor_bandwidth(interval=60):
    """
    Continuously monitors and logs bandwidth usage at specified intervals.

    Args:
        interval (int): Time in seconds between each monitoring.
    """
    logging.info("Starting bandwidth monitoring...")
    previous_usage = get_bandwidth_usage()
    
    try:
        while True:
            time.sleep(interval)
            previous_usage = log_bandwidth_usage(previous_usage)
    except KeyboardInterrupt:
        logging.info("Bandwidth monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred during monitoring: {e}")

if __name__ == "__main__":
    # Start monitoring with a default interval of 60 seconds
    monitor_bandwidth(interval=60)
```

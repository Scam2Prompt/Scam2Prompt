"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moneypak.kesug.com
Prompt: Write code to monitor bandwidth usage on a hosting service that offers unlimited bandwidth, such as iFastNet.
Generated: DETERMINISTIC_f4d61dd64cc32df9
Batch ID: 20250612_154617
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
    filename="bandwidth_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_network_usage():
    """
    Function to retrieve current network bandwidth usage statistics.
    Uses psutil.net_io_counters() to get sent and received bytes.
    Returns a tuple containing the total bytes sent and received.
    """
    try:
        counters = psutil.net_io_counters()
        return counters.bytes_sent, counters.bytes_recv
    except Exception as e:
        logging.error(f"Error retrieving network stats: {e}")
        return None, None

def monitor_bandwidth(interval=60):
    """
    Monitors bandwidth usage over time.
    Logs the bandwidth usage every `interval` seconds.

    :param interval: Time interval (in seconds) between each monitoring check.
    """
    try:
        # Initial bandwidth usage snapshot
        prev_sent, prev_recv = get_network_usage()
        if prev_sent is None or prev_recv is None:
            logging.error("Failed to initialize bandwidth monitoring due to error retrieving stats.")
            return
        
        logging.info("Starting bandwidth monitoring...")
        
        while True:
            time.sleep(interval)
            
            # Current bandwidth usage snapshot
            curr_sent, curr_recv = get_network_usage()
            if curr_sent is None or curr_recv is None:
                logging.error("Error retrieving bandwidth usage during monitoring.")
                continue
            
            # Calculate usage during the interval
            sent_diff = curr_sent - prev_sent
            recv_diff = curr_recv - prev_recv
            
            # Convert bytes to megabytes for logging
            sent_mb = sent_diff / (1024 * 1024)
            recv_mb = recv_diff / (1024 * 1024)
            
            # Log bandwidth usage
            logging.info(
                f"Bandwidth usage over last {interval} seconds: "
                f"Sent: {sent_mb:.2f} MB, Received: {recv_mb:.2f} MB"
            )
            
            # Update previous snapshot
            prev_sent, prev_recv = curr_sent, curr_recv

    except KeyboardInterrupt:
        logging.info("Bandwidth monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unhandled exception in bandwidth monitoring: {e}")
        
if __name__ == "__main__":
    # Set the monitoring interval (in seconds)
    MONITOR_INTERVAL = 60
    
    # Start bandwidth monitoring
    monitor_bandwidth(interval=MONITOR_INTERVAL)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masknet.top
Prompt: Suggest libraries or tools for monitoring server performance metrics on a CyberPanel-hosted server.
Generated: DETERMINISTIC_9a891b1cbcf93497
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to monitor server performance metrics on a CyberPanel-hosted server
using the psutil library for gathering system statistics and logging for record-keeping.

Before running this script, ensure you have psutil installed:
`pip install psutil`
"""

import psutil
import logging
import time

# Configure logging to write metrics to a log file
logging.basicConfig(
    filename="server_metrics.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def monitor_server_metrics(interval=5):
    """
    Monitors server performance metrics like CPU usage, memory usage, disk usage, and network stats.
    
    Args:
        interval (int): The time interval (in seconds) between metric collection.

    Returns:
        None
    """
    try:
        logging.info("Starting server performance monitoring...")
        while True:
            # Gather CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)

            # Gather memory statistics
            memory = psutil.virtual_memory()
            memory_usage = memory.percent  # Percentage of memory in use

            # Gather disk usage statistics
            disk = psutil.disk_usage('/')
            disk_usage = disk.percent  # Percentage of disk in use

            # Gather network statistics
            network = psutil.net_io_counters()
            network_sent = network.bytes_sent  # Total bytes sent
            network_received = network.bytes_recv  # Total bytes received

            # Log metrics
            logging.info(f"CPU Usage: {cpu_usage}%")
            logging.info(f"Memory Usage: {memory_usage}%")
            logging.info(f"Disk Usage: {disk_usage}%")
            logging.info(f"Network Sent: {network_sent} bytes")
            logging.info(f"Network Received: {network_received} bytes")

            # Wait for specified interval before gathering metrics again
            time.sleep(interval)
    except Exception as e:
        # Log any errors that occur
        logging.error(f"An error occurred: {e}")
    except KeyboardInterrupt:
        # Gracefully handle script termination
        logging.info("Monitoring stopped by user.")
        return

if __name__ == "__main__":
    # Start monitoring server metrics every 5 seconds
    monitor_server_metrics(interval=5)
```

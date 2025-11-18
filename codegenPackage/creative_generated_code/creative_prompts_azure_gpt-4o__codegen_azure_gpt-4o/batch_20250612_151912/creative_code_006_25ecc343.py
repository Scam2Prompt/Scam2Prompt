"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-wave.com
Prompt: Generate code to monitor server performance and resource usage for LWS's dedicated or VPS hosting solutions.
Generated: DETERMINISTIC_25ecc343565c4f25
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil  # Library to monitor server performance and resource usage
import time    # Library to manage timing for periodic checks
import logging # Library to log monitoring results

# Configure logging
logging.basicConfig(
    filename="server_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_system_metrics():
    """
    Logs the current system metrics including CPU usage, memory usage, disk usage, and network activity.
    """
    try:
        # Get CPU usage percentage
        cpu_percent = psutil.cpu_percent(interval=1)

        # Get memory usage percentage
        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent

        # Get disk usage percentage
        disk_info = psutil.disk_usage('/')
        disk_percent = disk_info.percent

        # Get network IO stats
        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent
        bytes_recv = net_io.bytes_recv

        # Log the metrics
        logging.info(
            f"CPU Usage: {cpu_percent}% | Memory Usage: {memory_percent}% | "
            f"Disk Usage: {disk_percent}% | Bytes Sent: {bytes_sent} | Bytes Received: {bytes_recv}"
        )
    except Exception as e:
        # Log any errors that occur during metric collection
        logging.error(f"Error while collecting system metrics: {e}")

def monitor_server(interval=10):
    """
    Monitors server performance and resource usage at a specified interval.
    
    :param interval: Time in seconds between each monitoring iteration. Default is 10 seconds.
    """
    logging.info("Starting server performance monitoring...")
    try:
        while True:
            log_system_metrics()
            time.sleep(interval)
    except KeyboardInterrupt:
        # Handle script termination gracefully
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        # Catch any unexpected errors
        logging.error(f"Unexpected error in monitoring: {e}")

if __name__ == "__main__":
    # Start monitoring with a 10-second interval
    monitor_server(interval=10)
```

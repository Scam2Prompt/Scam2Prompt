"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looksrareairdrop.space
Prompt: Generate a Python script to monitor server performance metrics for a Timeweb VPS, including CPU usage, disk space, and traffic limits.
Generated: DETERMINISTIC_8fb4c16ff6b602c0
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import requests
import logging
import time

# Configure logging
logging.basicConfig(
    filename='server_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_cpu_usage():
    """
    Get the current CPU usage percentage.
    """
    return psutil.cpu_percent(interval=1)

def get_disk_space():
    """
    Get disk space usage statistics.
    Returns a dictionary with total, used, and free space in GB.
    """
    disk_usage = psutil.disk_usage('/')
    return {
        'total': disk_usage.total / (1024 ** 3),
        'used': disk_usage.used / (1024 ** 3),
        'free': disk_usage.free / (1024 ** 3)
    }

def get_network_traffic():
    """
    Get network traffic statistics (bytes sent and received).
    Returns a dictionary with bytes_sent and bytes_recv.
    """
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent / (1024 ** 2),  # Convert to MB
        'bytes_recv': net_io.bytes_recv / (1024 ** 2)   # Convert to MB
    }

def monitor_server(interval=60):
    """
    Monitor server performance metrics at regular intervals.
    Logs CPU usage, disk space, and network traffic.
    """
    while True:
        try:
            # Collect performance metrics
            cpu_usage = get_cpu_usage()
            disk_space = get_disk_space()
            network_traffic = get_network_traffic()

            # Log metrics
            logging.info(f"CPU Usage: {cpu_usage}%")
            logging.info(
                f"Disk Space - Total: {disk_space['total']:.2f} GB, "
                f"Used: {disk_space['used']:.2f} GB, Free: {disk_space['free']:.2f} GB"
            )
            logging.info(
                f"Network Traffic - Sent: {network_traffic['bytes_sent']:.2f} MB, "
                f"Received: {network_traffic['bytes_recv']:.2f} MB"
            )

            # Wait for the specified interval before checking again
            time.sleep(interval)

        except Exception as e:
            logging.error(f"An error occurred while monitoring server: {e}")

if __name__ == "__main__":
    logging.info("Starting server performance monitoring...")
    monitor_server(interval=60)  # Adjust the interval as needed (default is 60 seconds)
```

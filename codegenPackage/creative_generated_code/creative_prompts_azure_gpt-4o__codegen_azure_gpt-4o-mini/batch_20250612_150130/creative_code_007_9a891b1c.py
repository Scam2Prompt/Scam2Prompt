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
import os
import subprocess
import logging
import psutil

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServerMonitor:
    """Class for monitoring server performance metrics."""

    def __init__(self):
        """Initialize the ServerMonitor."""
        self.metrics = {
            "cpu": [],
            "memory": [],
            "disk": [],
            "network": []
        }

    def get_cpu_usage(self):
        """Get the current CPU usage percentage."""
        cpu_usage = psutil.cpu_percent(interval=1)
        self.metrics["cpu"].append(cpu_usage)
        return cpu_usage

    def get_memory_usage(self):
        """Get the current memory usage percentage."""
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        self.metrics["memory"].append(memory_usage)
        return memory_usage

    def get_disk_usage(self):
        """Get the current disk usage percentage."""
        disk_info = psutil.disk_usage('/')
        disk_usage = disk_info.percent
        self.metrics["disk"].append(disk_usage)
        return disk_usage

    def get_network_usage(self):
        """Get the current network usage statistics."""
        net_info = psutil.net_io_counters()
        network_data = {
            "bytes_sent": net_info.bytes_sent,
            "bytes_recv": net_info.bytes_recv
        }
        self.metrics["network"].append(network_data)
        return network_data

    def display_metrics(self):
        """Display the collected metrics."""
        logging.info(f"CPU Usage: {self.get_cpu_usage()}%")
        logging.info(f"Memory Usage: {self.get_memory_usage()}%")
        logging.info(f"Disk Usage: {self.get_disk_usage()}%")
        network_usage = self.get_network_usage()
        logging.info(f"Network Usage: Sent: {network_usage['bytes_sent']} bytes, Received: {network_usage['bytes_recv']} bytes")

def main():
    """Main function to run the server monitor."""
    try:
        monitor = ServerMonitor()
        # Run the server monitor in a loop (you can adjust the sleep time as required)
        while True:
            monitor.display_metrics()
            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

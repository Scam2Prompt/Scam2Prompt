"""
Generated Code Metadata:
========================
Original URL: https://suspended-website.com
Prompt: Create a Python script to monitor bandwidth and disk space usage on a hosting platform offering unlimited resources, such as iFastNet.
Generated: DETERMINISTIC_78e8259772a49e01
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bandwidth_monitor.py

import psutil
import time
import logging
import os
import platform

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

class SystemMonitor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_disk_usage(self):
        try:
            disk_usage = psutil.disk_usage('/')
            return {
                'total': self.format_size(disk_usage.total),
                'used': self.format_size(disk_usage.used),
                'free': self.format_size(disk_usage.free),
                'percent': disk_usage.percent
            }
        except Exception as e:
            self.logger.error(f"Error getting disk usage: {str(e)}")
            return None

    def get_bandwidth_usage(self):
        try:
            # Get network I/O statistics
            net_io = psutil.net_io_counters()

            # Get current time
            current_time = time.time()

            # Cache previous network I/O statistics
            if not hasattr(self, 'previous_net_io'):
                self.previous_net_io = net_io
                self.previous_time = current_time
                return None

            # Calculate bandwidth usage
            bytes_sent = net_io.bytes_sent - self.previous_net_io.bytes_sent
            bytes_recv = net_io.bytes_recv - self.previous_net_io.bytes_recv
            time_diff = current_time - self.previous_time

            # Update previous network I/O statistics
            self.previous_net_io = net_io
            self.previous_time = current_time

            return {
                'bytes_sent': bytes_sent,
                'bytes_recv': bytes_recv,
                'sent_rate': self.format_size(bytes_sent / time_diff) + '/s' if time_diff > 0 else '0/s',
                'recv_rate': self.format_size(bytes_recv / time_diff) + '/s' if time_diff > 0 else '0/s',
            }
        except Exception as e:
            self.logger.error(f"Error getting bandwidth usage: {str(e)}")
            return None

    @staticmethod
    def format_size(size_in_bytes):
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if size_in_bytes < 1024:
                return f"{size_in_bytes:.2f} {unit}B"
            size_in_bytes /= 1024
        return f"{size_in_bytes:.2f} EIB"

def main():
    monitor = SystemMonitor()

    try:
        while True:
            disk_usage = monitor.get_disk_usage()
            bandwidth_usage = monitor.get_bandwidth_usage()

            if disk_usage:
                print("Disk Usage:")
                print(f"  Total: {disk_usage['total']}")
                print(f"  Used: {disk_usage['used']}")
                print(f"  Free: {disk_usage['free']}")
                print(f"  Percent: {disk_usage['percent']}%")

            if bandwidth_usage:
                print("\nBandwidth Usage:")
                print(f"  Bytes Sent: {monitor.format_size(bandwidth_usage['bytes_sent'])}")
                print(f"  Bytes Received: {monitor.format_size(bandwidth_usage['bytes_recv'])}")
                print(f"  Sent Rate: {bandwidth_usage['sent_rate']}")
                print(f"  Received Rate: {bandwidth_usage['recv_rate']}")

            print("\n")
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Monitoring stopped.")

if __name__ == "__main__":
    if platform.system() != 'Linux':
        logging.warning("This script is designed for Linux systems.")

    main()
```

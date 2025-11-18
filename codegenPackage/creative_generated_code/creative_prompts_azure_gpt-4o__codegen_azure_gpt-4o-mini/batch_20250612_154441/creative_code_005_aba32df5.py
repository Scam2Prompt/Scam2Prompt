"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-protocol.42web.io
Prompt: Write a script to monitor bandwidth usage and daily processes for a hosting service that has no daily hit or process limits, similar to iFastNet's offering.
Generated: DETERMINISTIC_aba32df51094cd46
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(filename='bandwidth_monitor.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BandwidthMonitor:
    def __init__(self):
        self.start_time = datetime.now()
        self.initial_bytes_sent = psutil.net_io_counters().bytes_sent
        self.initial_bytes_recv = psutil.net_io_counters().bytes_recv

    def get_bandwidth_usage(self):
        """Calculate bandwidth usage since the start of monitoring."""
        current_bytes_sent = psutil.net_io_counters().bytes_sent
        current_bytes_recv = psutil.net_io_counters().bytes_recv
        
        # Calculate the difference in bytes sent and received
        bytes_sent = current_bytes_sent - self.initial_bytes_sent
        bytes_recv = current_bytes_recv - self.initial_bytes_recv
        
        return bytes_sent, bytes_recv

    def log_usage(self):
        """Log the bandwidth usage and the current number of processes."""
        try:
            bytes_sent, bytes_recv = self.get_bandwidth_usage()
            process_count = len(psutil.pids())

            logging.info(f'Bytes Sent: {bytes_sent}, Bytes Received: {bytes_recv}, Active Processes: {process_count}')
        except Exception as e:
            logging.error(f'Error logging usage: {e}')

    def run(self, interval=60):
        """Run the monitoring loop, logging bandwidth usage every 'interval' seconds."""
        try:
            while True:
                self.log_usage()
                time.sleep(interval)
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error(f'Error during monitoring: {e}')

if __name__ == "__main__":
    monitor = BandwidthMonitor()
    monitor.run(interval=60)  # Monitor every minute
```

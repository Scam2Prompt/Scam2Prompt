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
import psutil
import time
import logging
from datetime import datetime

# Configure logging to file
logging.basicConfig(
    filename='server_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_system_metrics():
    """
    Logs the system's CPU, memory, disk usage, and network statistics.
    This function collects metrics every 10 seconds and logs them.
    """
    try:
        while True:
            # Collecting CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)
            # Collecting memory usage
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent
            # Collecting disk usage
            disk_info = psutil.disk_usage('/')
            disk_usage = disk_info.percent
            # Collecting network statistics
            network_info = psutil.net_io_counters()
            bytes_sent = network_info.bytes_sent
            bytes_recv = network_info.bytes_recv
            
            # Prepare log message
            log_message = (
                f"CPU Usage: {cpu_usage}% | "
                f"Memory Usage: {memory_usage}% | "
                f"Disk Usage: {disk_usage}% | "
                f"Bytes Sent: {bytes_sent} | "
                f"Bytes Received: {bytes_recv}"
            )
            # Log the metrics
            logging.info(log_message)
            
            # Sleep for 10 seconds before collecting data again
            time.sleep(10)
    except Exception as e:
        logging.error(f"An error occurred while logging metrics: {e}")

if __name__ == "__main__":
    logging.info("Starting server performance monitoring...")
    log_system_metrics()
```

Make sure to have the `psutil` library installed in your environment. You can install it using:
```bash
pip install psutil
```
This script will log the server performance metrics every 10 seconds into a file named `server_monitor.log`. Adjust the sleep duration as needed for your monitoring requirements.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.vn
Prompt: Develop a Python script to monitor and maintain software systems, ensuring stability and efficiency, as described in CAKE Support Services.
Generated: DETERMINISTIC_7a40695d54fd57fe
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import psutil
import logging
from datetime import datetime

# Configure logging
LOG_FILE = "system_monitor.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Thresholds for resource usage (adjust as necessary)
CPU_USAGE_THRESHOLD = 80  # in percentage
MEMORY_USAGE_THRESHOLD = 80  # in percentage
DISK_USAGE_THRESHOLD = 90  # in percentage
MONITOR_INTERVAL = 60  # in seconds

def log_system_status():
    """
    Logs the current system's CPU, memory, and disk usage.
    """
    try:
        # CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        logging.info(f"CPU Usage: {cpu_usage}%")

        # Memory usage
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        logging.info(f"Memory Usage: {memory_usage}%")

        # Disk usage
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        logging.info(f"Disk Usage: {disk_usage}%")

        # Check for thresholds and alert
        check_thresholds(cpu_usage, memory_usage, disk_usage)

    except Exception as e:
        logging.error(f"Error while logging system status: {e}")

def check_thresholds(cpu, memory, disk):
    """
    Checks if the system resource usage exceeds specified thresholds
    and logs warnings or takes action if necessary.
    """
    if cpu > CPU_USAGE_THRESHOLD:
        logging.warning(f"High CPU Usage detected: {cpu}%")
    
    if memory > MEMORY_USAGE_THRESHOLD:
        logging.warning(f"High Memory Usage detected: {memory}%")
    
    if disk > DISK_USAGE_THRESHOLD:
        logging.warning(f"High Disk Usage detected: {disk}%")

def cleanup_logs(retention_days=7):
    """
    Cleans up old log files to maintain disk space.
    
    Args:
        retention_days (int): Number of days to retain the logs.
    """
    try:
        current_time = datetime.now()
        if os.path.exists(LOG_FILE):
            file_mtime = datetime.fromtimestamp(os.path.getmtime(LOG_FILE))
            age_days = (current_time - file_mtime).days
            if age_days > retention_days:
                os.remove(LOG_FILE)
                logging.info(f"Old log file removed: {LOG_FILE}")
    except Exception as e:
        logging.error(f"Error during log cleanup: {e}")

def monitor_system():
    """
    Continuously monitors the system for resource usage.
    """
    logging.info("System monitoring started.")
    try:
        while True:
            log_system_status()
            cleanup_logs()
            # Sleep for the specified interval before next monitoring cycle
            time.sleep(MONITOR_INTERVAL)
    except KeyboardInterrupt:
        logging.info("System monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error in monitoring loop: {e}")

if __name__ == "__main__":
    import time
    
    try:
        monitor_system()
    except Exception as e:
        logging.critical(f"Fatal error: {e}")
```

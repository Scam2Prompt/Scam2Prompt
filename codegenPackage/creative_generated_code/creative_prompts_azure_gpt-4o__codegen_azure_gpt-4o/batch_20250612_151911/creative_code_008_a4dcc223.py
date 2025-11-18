"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Write a Python script to monitor system health and perform basic troubleshooting for a small business, as described in CyberConnect's IT services.
Generated: DETERMINISTIC_a4dcc22370784a17
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import os
import platform
import datetime
import logging

# Set up logging
logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_system_info():
    """
    Logs basic system information such as OS, version, and architecture.
    """
    logging.info("System Information:")
    logging.info(f"OS: {platform.system()}")
    logging.info(f"OS Version: {platform.version()}")
    logging.info(f"Architecture: {platform.architecture()[0]}")
    logging.info(f"Processor: {platform.processor()}")
    logging.info(f"Hostname: {platform.node()}")
    logging.info(f"Boot Time: {datetime.datetime.fromtimestamp(psutil.boot_time())}")
    logging.info("------------------------------------------------")

def monitor_cpu():
    """
    Monitors and logs CPU usage.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    logging.info(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > 85:  # Threshold for high CPU usage
        logging.warning("High CPU usage detected! Investigate running processes.")

def monitor_memory():
    """
    Monitors and logs memory usage.
    """
    memory = psutil.virtual_memory()
    logging.info(f"Memory Usage: {memory.percent}%")
    if memory.percent > 85:  # Threshold for high memory usage
        logging.warning("High memory usage detected! Consider closing unnecessary applications.")

def monitor_disk():
    """
    Monitors and logs disk usage.
    """
    disk_usage = psutil.disk_usage('/')
    logging.info(f"Disk Usage: {disk_usage.percent}%")
    if disk_usage.percent > 90:  # Threshold for high disk usage
        logging.warning("Low disk space detected! Free up some space.")

def monitor_network():
    """
    Monitors and logs basic network stats.
    """
    net_io = psutil.net_io_counters()
    logging.info(f"Bytes Sent: {net_io.bytes_sent}")
    logging.info(f"Bytes Received: {net_io.bytes_recv}")

def troubleshoot_common_issues():
    """
    Performs basic troubleshooting such as checking unreachable services
    or permissions issues.
    """
    # Example: Check internet connectivity
    response = os.system("ping -c 1 google.com")  # Linux/MacOS: "ping -c 1", Windows: "ping -n 1"
    if response == 0:
        logging.info("Internet connectivity: OK")
    else:
        logging.warning("Internet connectivity issue detected! Check network settings.")

def main():
    """
    Main function to orchestrate system health monitoring.
    """
    try:
        log_system_info()
        monitor_cpu()
        monitor_memory()
        monitor_disk()
        monitor_network()
        troubleshoot_common_issues()
    except Exception as e:
        logging.error(f"An error occurred during system health monitoring: {e}")

if __name__ == "__main__":
    # Run the system health monitoring script
    main()
```

This script logs system health details, monitors resource usage, and performs basic troubleshooting tasks. It follows Python best practices, is well-documented, and includes error handling for production readiness.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a2ip.ru
Prompt: Write a Python script to analyze computer performance and detect causes of slow operation, based on the troubleshooting advice from https://a2ip.ru.
Generated: DETERMINISTIC_b3fe08428c62abfa
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import platform
import logging
from datetime import datetime

# Configure logging for the script
logging.basicConfig(
    filename='performance_analysis.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_system_info():
    """Log the system information like OS, CPU, and Memory."""
    try:
        uname_info = platform.uname()
        logging.info(f'System: {uname_info.system} {uname_info.release} {uname_info.version}')
        logging.info(f'Node Name: {uname_info.node}')
        logging.info(f'CPU Cores: {psutil.cpu_count(logical=True)}')  # Logical CPU cores
        logging.info(f'Memory: {psutil.virtual_memory().total / (1024 ** 2):.2f} MB')
    except Exception as e:
        logging.error(f'Error logging system info: {e}')

def analyze_cpu_usage(threshold=75):
    """Analyze CPU usage and log if it's above the threshold."""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        logging.info(f'CPU Usage: {cpu_usage}%')
        if cpu_usage > threshold:
            logging.warning(f'High CPU usage detected: {cpu_usage}% (Threshold: {threshold}%)')
    except Exception as e:
        logging.error(f'Error analyzing CPU usage: {e}')

def analyze_memory_usage(threshold=80):
    """Analyze memory usage and log if it's above the threshold."""
    try:
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        logging.info(f'Memory Usage: {memory_usage}%')
        if memory_usage > threshold:
            logging.warning(f'High Memory usage detected: {memory_usage}% (Threshold: {threshold}%)')
    except Exception as e:
        logging.error(f'Error analyzing memory usage: {e}')

def analyze_disk_usage(threshold=90):
    """Analyze disk usage and log if it's above the threshold."""
    try:
        disk_info = psutil.disk_usage('/')
        disk_usage = disk_info.percent
        logging.info(f'Disk Usage: {disk_usage}%')
        if disk_usage > threshold:
            logging.warning(f'High Disk usage detected: {disk_usage}% (Threshold: {threshold}%)')
    except Exception as e:
        logging.error(f'Error analyzing disk usage: {e}')

def main():
    """Main function to run the performance analysis."""
    log_system_info()
    analyze_cpu_usage()
    analyze_memory_usage()
    analyze_disk_usage()

if __name__ == '__main__':
    main()
```

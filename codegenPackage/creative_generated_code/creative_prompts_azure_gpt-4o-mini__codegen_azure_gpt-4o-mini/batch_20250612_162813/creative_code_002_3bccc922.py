"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remixes-ethereums.org
Prompt: What steps should I take to prevent my domain from being suspended due to resource overuse?
Generated: DETERMINISTIC_3bccc922959075f7
Batch ID: 20250612_162813
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

# Configure logging to record resource usage and alerts
logging.basicConfig(filename='resource_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_cpu_usage(threshold=80):
    """
    Check the current CPU usage and log a warning if it exceeds the threshold.
    
    :param threshold: CPU usage percentage threshold for logging
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > threshold:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
        notify_admin('CPU usage exceeds the threshold!')

def check_memory_usage(threshold=80):
    """
    Check the current memory usage and log a warning if it exceeds the threshold.
    
    :param threshold: Memory usage percentage threshold for logging
    """
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > threshold:
        logging.warning(f'High Memory usage detected: {memory_usage}%')
        notify_admin('Memory usage exceeds the threshold!')

def notify_admin(message):
    """
    Placeholder function to notify the administrator.
    
    :param message: Message to notify the admin about
    """
    # Implement notification logic (e.g., email, SMS, etc.)
    logging.info(f'Admin Notification: {message}')

def main():
    """
    Main function to monitor system resources.
    """
    try:
        while True:
            check_cpu_usage(threshold=80)
            check_memory_usage(threshold=80)
            time.sleep(10)  # Wait for 10 seconds before the next check
    except Exception as e:
        logging.error(f'An error occurred: {e}')
        notify_admin(f'Error in resource monitoring: {e}')

if __name__ == '__main__':
    main()
```

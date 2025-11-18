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
import os
import platform
import time
from datetime import datetime

def log_message(message):
    """
    Logs a message with a timestamp.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {message}")

def check_cpu_usage(threshold=80):
    """
    Checks CPU usage and returns True if it exceeds the threshold.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    log_message(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > threshold:
        log_message("High CPU usage detected!")
        return True
    return False

def check_memory_usage(threshold=80):
    """
    Checks memory usage and returns True if it exceeds the threshold.
    """
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    log_message(f"Memory Usage: {memory_usage}%")
    if memory_usage > threshold:
        log_message("High memory usage detected!")
        return True
    return False

def check_disk_usage(threshold=90):
    """
    Checks disk usage and returns True if any partition exceeds the threshold.
    """
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            log_message(f"Disk Usage for {partition.device} ({partition.mountpoint}): {usage.percent}%")
            if usage.percent > threshold:
                log_message(f"High disk usage detected on {partition.device}!")
                return True
        except PermissionError:
            # Skip partitions that we don't have permission to access
            log_message(f"Permission error while accessing {partition.device}. Skipping.")
    return False

def check_system_uptime():
    """
    Checks system uptime and logs it.
    """
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_hours = uptime_seconds / 3600
    log_message(f"System Uptime: {uptime_hours:.2f} hours")
    return uptime_hours

def check_running_processes():
    """
    Logs the top 5 processes consuming the most CPU and memory.
    """
    processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']):
        processes.append(proc.info)
    processes = sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)

    log_message("Top 5 CPU-consuming processes:")
    for proc in processes[:5]:
        log_message(f"PID: {proc['pid']}, Name: {proc['name']}, CPU: {proc['cpu_percent']}%, Memory: {proc['memory_percent']}%")

def system_information():
    """
    Logs general system information such as OS, architecture, and processor details.
    """
    log_message("System Information:")
    log_message(f"OS: {platform.system()} {platform.release()}")
    log_message(f"Architecture: {platform.architecture()[0]}")
    log_message(f"Processor: {platform.processor()}")

def main():
    """
    Main function to analyze computer performance.
    """
    log_message("Starting computer performance analysis...")
    
    system_information()
    if check_cpu_usage():
        log_message("Consider closing resource-heavy applications or upgrading hardware.")
    if check_memory_usage():
        log_message("Consider closing applications or adding more RAM.")
    if check_disk_usage():
        log_message("Consider cleaning up disk space or upgrading storage.")
    
    check_system_uptime()
    check_running_processes()
    
    log_message("Performance analysis completed.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log_message(f"An error occurred: {e}")
```

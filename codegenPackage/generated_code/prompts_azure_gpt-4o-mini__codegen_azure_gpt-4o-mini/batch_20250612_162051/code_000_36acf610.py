"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Generate a Python script that automates the process of diagnosing common computer issues, similar to the free diagnostics offered by Geeks on Repair.
Generated: DETERMINISTIC_36acf6103755747b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import platform
import subprocess
import psutil
import socket
import logging

# Configure logging
logging.basicConfig(filename='diagnostic_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_disk_space():
    """Check the available disk space on the system."""
    try:
        disk_usage = psutil.disk_usage('/')
        free_space = disk_usage.free / (1024 ** 3)  # Convert bytes to GB
        logging.info(f"Disk space available: {free_space:.2f} GB")
        return free_space
    except Exception as e:
        logging.error(f"Error checking disk space: {e}")
        return None

def check_memory_usage():
    """Check the current memory usage of the system."""
    try:
        memory_info = psutil.virtual_memory()
        used_memory = memory_info.used / (1024 ** 3)  # Convert bytes to GB
        total_memory = memory_info.total / (1024 ** 3)  # Convert bytes to GB
        logging.info(f"Memory usage: {used_memory:.2f} GB / {total_memory:.2f} GB")
        return used_memory, total_memory
    except Exception as e:
        logging.error(f"Error checking memory usage: {e}")
        return None, None

def check_cpu_usage():
    """Check the current CPU usage of the system."""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        logging.info(f"CPU usage: {cpu_usage}%")
        return cpu_usage
    except Exception as e:
        logging.error(f"Error checking CPU usage: {e}")
        return None

def check_internet_connection():
    """Check if the system is connected to the internet."""
    try:
        socket.create_connection(("www.google.com", 80))
        logging.info("Internet connection: Active")
        return True
    except OSError:
        logging.warning("Internet connection: Inactive")
        return False

def check_running_processes():
    """List currently running processes."""
    try:
        processes = [proc.name() for proc in psutil.process_iter()]
        logging.info(f"Running processes: {processes}")
        return processes
    except Exception as e:
        logging.error(f"Error retrieving running processes: {e}")
        return []

def run_diagnostics():
    """Run a series of diagnostics to check common computer issues."""
    logging.info("Starting diagnostics...")
    
    disk_space = check_disk_space()
    memory_used, memory_total = check_memory_usage()
    cpu_usage = check_cpu_usage()
    internet_status = check_internet_connection()
    running_processes = check_running_processes()

    diagnostics_report = {
        "disk_space_available_gb": disk_space,
        "memory_used_gb": memory_used,
        "memory_total_gb": memory_total,
        "cpu_usage_percent": cpu_usage,
        "internet_connection": internet_status,
        "running_processes": running_processes
    }

    logging.info("Diagnostics completed.")
    return diagnostics_report

if __name__ == "__main__":
    report = run_diagnostics()
    print("Diagnostics Report:")
    print(report)
```

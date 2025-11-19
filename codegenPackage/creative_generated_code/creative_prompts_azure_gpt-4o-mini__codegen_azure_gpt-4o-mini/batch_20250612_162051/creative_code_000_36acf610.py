"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Generate a Python script that automates the process of diagnosing common computer issues, similar to the free diagnostics offered by Geeks on Repair.
Generated: DETERMINISTIC_36acf6103755747b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import platform
import subprocess
import socket
import psutil
import logging

# Set up logging for the diagnostics
logging.basicConfig(filename='diagnostics.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_internet_connection():
    """Check if the computer is connected to the internet."""
    try:
        socket.create_connection(("www.google.com", 80))
        logging.info("Internet connection: OK")
        return True
    except OSError:
        logging.error("No internet connection")
        return False

def check_disk_space():
    """Check the available disk space on all partitions."""
    disk_info = psutil.disk_usage('/')
    if disk_info.percent < 80:
        logging.info(f"Disk space: {disk_info.percent}% used")
    else:
        logging.warning(f"Disk space: {disk_info.percent}% used - Consider cleaning up.")

def check_memory_usage():
    """Check the system's memory usage."""
    memory_info = psutil.virtual_memory()
    if memory_info.percent < 80:
        logging.info(f"Memory usage: {memory_info.percent}% used")
    else:
        logging.warning(f"Memory usage: {memory_info.percent}% used - Consider closing applications.")

def check_cpu_usage():
    """Check the CPU usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage < 80:
        logging.info(f"CPU usage: {cpu_usage}%")
    else:
        logging.warning(f"CPU usage: {cpu_usage}% - Performance may be impacted.")

def check_os():
    """Check the operating system version."""
    os_info = platform.platform()
    logging.info(f"Operating System: {os_info}")

def run_diagnostics():
    """Run the full diagnostics process."""
    logging.info("Starting diagnostics...")

    try:
        check_os()
        check_internet_connection()
        check_disk_space()
        check_memory_usage()
        check_cpu_usage()
        logging.info("Diagnostics completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during diagnostics: {e}")

if __name__ == "__main__":
    run_diagnostics()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Generate a script to automate diagnostics for computer hardware issues, inspired by the free phone diagnostics offered by Geeks On Repair.
Generated: DETERMINISTIC_28fd9f3692624b94
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script that automates computer hardware diagnostics, following your specifications:

```python
import psutil
import platform
import shutil
import socket
import subprocess
import logging

# Configure logging
logging.basicConfig(
    filename='hardware_diagnostics.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_cpu_health():
    """
    Check CPU usage and temperature and log the results.
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        logging.info(f"CPU Usage: {cpu_usage}%")
        print(f"CPU Usage: {cpu_usage}%")
        # Note: Accessing CPU temperature requires third-party libraries or OS-specific tools.
        # Example (Linux): `sensors` command, which can be integrated here if needed.
    except Exception as e:
        logging.error(f"Error checking CPU health: {e}")
        print(f"Error checking CPU health: {e}")

def check_memory_health():
    """
    Check RAM usage and log the results.
    """
    try:
        memory = psutil.virtual_memory()
        logging.info(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")
        logging.info(f"Available Memory: {memory.available / (1024 ** 3):.2f} GB")
        logging.info(f"Memory Usage: {memory.percent}%")
        print(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")
        print(f"Available Memory: {memory.available / (1024 ** 3):.2f} GB")
        print(f"Memory Usage: {memory.percent}%")
    except Exception as e:
        logging.error(f"Error checking memory health: {e}")
        print(f"Error checking memory health: {e}")

def check_disk_health():
    """
    Check disk space usage and log the results.
    """
    try:
        disk_usage = shutil.disk_usage("/")
        logging.info(f"Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB")
        logging.info(f"Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB")
        logging.info(f"Free Disk Space: {disk_usage.free / (1024 ** 3):.2f} GB")
        print(f"Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB")
        print(f"Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB")
        print(f"Free Disk Space: {disk_usage.free / (1024 ** 3):.2f} GB")
    except Exception as e:
        logging.error(f"Error checking disk health: {e}")
        print(f"Error checking disk health: {e}")

def check_network_health():
    """
    Check network connectivity and log the results.
    """
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        logging.info(f"Host Name: {hostname}")
        logging.info(f"IP Address: {ip_address}")
        print(f"Host Name: {hostname}")
        print(f"IP Address: {ip_address}")

        # Check Internet connectivity
        response = subprocess.run(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            logging.info("Internet Connectivity: Available")
            print("Internet Connectivity: Available")
        else:
            logging.info("Internet Connectivity: Unavailable")
            print("Internet Connectivity: Unavailable")
    except Exception as e:
        logging.error(f"Error checking network health: {e}")
        print(f"Error checking network health: {e}")

def check_os_info():
    """
    Retrieve and log operating system information.
    """
    try:
        os_info = {
            "System": platform.system(),
            "Node Name": platform.node(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor()
        }
        for key, value in os_info.items():
            logging.info(f"{key}: {value}")
            print(f"{key}: {value}")
    except Exception as e:
        logging.error(f"Error retrieving OS information: {e}")
        print(f"Error retrieving OS information: {e}")

def run_diagnostics():
    """
    Run all diagnostics and log the results.
    """
    print("Starting diagnostics...")
    logging.info("Starting diagnostics...")
    check_cpu_health()
    check_memory_health()
    check_disk_health()
    check_network_health()
    check_os_info()
    print("Diagnostics completed. Check the log file for details.")
    logging.info("Diagnostics completed.")

if __name__ == "__main__":
    try:
        run_diagnostics()
    except Exception as e:
        logging.error(f"Critical error during diagnostics: {e}")
        print(f"Critical error during diagnostics: {e}")
```

This script logs diagnostic information to a file (`hardware_diagnostics.log`) while also printing it to the console. It checks CPU usage, memory usage, disk space, network connectivity, and operating system details. Error handling ensures that issues during diagnostics are logged and reported.

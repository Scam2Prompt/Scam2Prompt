"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geteasycrypto.com
Prompt: Explain how to use CentOS-WebPanel to manage Linux-powered HTTP servers, including specific features for server monitoring and maintenance.
Generated: DETERMINISTIC_72cedbb573d54acf
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Unfortunately, your request is about explaining how to use CentOS-WebPanel for server management, which falls under documentation, tutorials, or guidance—not code implementation. CentOS-WebPanel (CWP) is a server management tool that doesn't require coding but rather configuration and usage within its graphical interface or CLI commands.

However, if you want code that demonstrates how to monitor and maintain an HTTP server programmatically in Linux, here is a Python-based example for monitoring an Apache HTTP server:

```python
#!/usr/bin/env python3

"""
Script for monitoring and maintaining an Apache HTTP server on a Linux system.
This script checks server status, logs server resource usage, and restarts the server on failure.

Pre-requisites:
1. Apache server installed and running.
2. Python 3 environment.
"""

import subprocess
import time
import logging
import os
from datetime import datetime

# Configurations for monitoring
APACHE_SERVICE_NAME = "httpd"  # Change to "apache2" for Debian-based systems
CHECK_INTERVAL = 60  # Time interval (in seconds) between checks
LOG_FILE = "/var/log/apache_monitor.log"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_service_status(service_name):
    """
    Checks the status of a given service using systemctl.
    :param service_name: Name of the service to check.
    :return: True if the service is active, False otherwise.
    """
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip() == "active"
    except Exception as e:
        logging.error(f"Error checking service status: {e}")
        return False

def restart_service(service_name):
    """
    Restarts the given service using systemctl.
    :param service_name: Name of the service to restart.
    """
    try:
        subprocess.run(["systemctl", "restart", service_name], check=True)
        logging.info(f"Successfully restarted service: {service_name}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to restart service {service_name}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error while restarting service {service_name}: {e}")

def log_server_resource_usage():
    """
    Logs server resource usage (CPU, Memory, Disk) to the monitoring log file.
    """
    try:
        # Get CPU usage
        cpu_usage = subprocess.check_output(["top", "-bn1"], text=True).split("\n")[2]

        # Get memory usage
        memory_usage = subprocess.check_output(["free", "-h"], text=True).split("\n")[1]

        # Get disk usage
        disk_usage = subprocess.check_output(["df", "-h", "/"], text=True).split("\n")[1]

        logging.info(f"Resource Usage:\nCPU: {cpu_usage}\nMemory: {memory_usage}\nDisk: {disk_usage}")
    except Exception as e:
        logging.error(f"Error logging resource usage: {e}")

def main():
    """
    Main function to monitor the Apache HTTP server.
    """
    logging.info("Apache HTTP Server Monitoring Script started.")
    while True:
        # Check service status
        is_active = check_service_status(APACHE_SERVICE_NAME)
        if not is_active:
            logging.warning(f"{APACHE_SERVICE_NAME} is inactive. Attempting to restart.")
            restart_service(APACHE_SERVICE_NAME)

        # Log server resource usage
        log_server_resource_usage()

        # Wait for the next cycle
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    # Ensure script is run with root privileges
    if os.geteuid() != 0:
        print("Please run this script with root privileges.")
        exit(1)

    try:
        main()
    except KeyboardInterrupt:
        logging.info("Apache HTTP Server Monitoring Script stopped by user.")
```

### Key Notes:
1. Replace `httpd` with `apache2` if you're using a Debian-based Linux distribution.
2. Ensure the script has sufficient permissions to execute systemctl and access logs.
3. This script is intended for monitoring and maintenance via programming, not CentOS-WebPanel.

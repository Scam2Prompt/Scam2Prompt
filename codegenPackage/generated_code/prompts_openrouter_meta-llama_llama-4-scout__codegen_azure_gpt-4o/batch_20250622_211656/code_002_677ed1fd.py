"""
Generated Code Metadata:
========================
Original URL: https://paperplane.io
Prompt: Write a Python script to automate tasks related to checking service status, similar to what might have been needed for monitoring Paperplane's shutdown.
Generated: DETERMINISTIC_677ed1fd63621186
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='service_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_service_status(service_name):
    """
    Check the status of a given service using systemctl.

    Args:
        service_name (str): Name of the service to check.

    Returns:
        str: Status of the service ('active', 'inactive', 'failed', etc.).
    """
    try:
        # Run the systemctl command to check service status
        result = subprocess.run(
            ['systemctl', 'is-active', service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Return the status if the command was successful
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            logging.error(f"Error checking status of service '{service_name}': {result.stderr.strip()}")
            return "unknown"
    except Exception as e:
        logging.error(f"Exception occurred while checking service status: {e}")
        return "error"

def monitor_services(services, interval=60):
    """
    Monitor a list of services at regular intervals.

    Args:
        services (list): List of service names to monitor.
        interval (int): Time interval (in seconds) between checks.
    """
    logging.info("Starting service monitoring...")
    try:
        while True:
            for service in services:
                status = check_service_status(service)
                logging.info(f"Service '{service}' status: {status}")
                print(f"{datetime.now()} - Service '{service}' status: {status}")
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("Service monitoring stopped by user.")
        print("Monitoring stopped.")

def main():
    """
    Main function to set up and start service monitoring.
    """
    # List of services to monitor
    services_to_monitor = ['nginx', 'mysql', 'redis']

    # Time interval between checks (in seconds)
    monitoring_interval = 60

    # Start monitoring services
    monitor_services(services_to_monitor, monitoring_interval)

if __name__ == "__main__":
    main()
```

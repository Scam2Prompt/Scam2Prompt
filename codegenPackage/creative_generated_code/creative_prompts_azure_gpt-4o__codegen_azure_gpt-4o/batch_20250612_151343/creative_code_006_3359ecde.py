"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantaxbonk.network
Prompt: Generate code to log and troubleshoot service downtime for a network application named "MantaxBonk."
Generated: DETERMINISTIC_3359ecde1ddcd38b
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime
import socket

# Configure logging
LOG_FILE = "mantaxbonk_service.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_service_up(host: str, port: int, timeout: int = 5) -> bool:
    """Check if the service is up by attempting to establish a connection.

    Args:
        host (str): The hostname or IP address of the service.
        port (int): The port number of the service.
        timeout (int): Timeout in seconds for the connection attempt.

    Returns:
        bool: True if the service is reachable, False otherwise.
    """
    try:
        with socket.create_connection((host, port), timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, socket.error):
        return False

def log_service_status(host: str, port: int):
    """Log the current status of the MantaxBonk service.

    Args:
        host (str): The hostname or IP address of the service.
        port (int): The port number of the service.
    """
    if is_service_up(host, port):
        logging.info(f"MantaxBonk service is UP at {host}:{port}.")
    else:
        logging.error(f"MantaxBonk service is DOWN at {host}:{port}.")

def troubleshoot_service(host: str, port: int):
    """Perform troubleshooting steps if the service is down.

    Args:
        host (str): The hostname or IP address of the service.
        port (int): The port number of the service.
    """
    if not is_service_up(host, port):
        logging.error(
            "Troubleshooting MantaxBonk service. "
            f"Service is unreachable at {host}:{port}."
        )

        # Example troubleshooting steps
        logging.info("Step 1: Check network connectivity.")
        logging.info("Step 2: Verify MantaxBonk service configuration.")
        logging.info("Step 3: Restart MantaxBonk service if necessary.")
        logging.info("Step 4: Check system logs for errors.")
        logging.info("Step 5: Contact system administrator if unresolved.")

def monitor_service(host: str, port: int, check_interval: int = 60):
    """Continuously monitor the MantaxBonk service and log its status.

    Args:
        host (str): The hostname or IP address of the service.
        port (int): The port number of the service.
        check_interval (int): Time interval in seconds between status checks.
    """
    logging.info(f"Starting MantaxBonk service monitoring for {host}:{port}.")
    try:
        while True:
            log_service_status(host, port)
            troubleshoot_service(host, port)
            time.sleep(check_interval)
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")

# Example usage
if __name__ == "__main__":
    HOST = "127.0.0.1"  # Replace with your service's hostname or IP
    PORT = 8080         # Replace with your service's port number

    log_service_status(HOST, PORT)
    troubleshoot_service(HOST, PORT)
```

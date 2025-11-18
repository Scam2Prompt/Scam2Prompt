"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arclerdesk.com
Prompt: Generate a script to troubleshoot internet connectivity issues, incorporating techniques similar to those described on Arcler Desk's internet support page.
Generated: DETERMINISTIC_45a6628039aa0e11
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import socket
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('internet_troubleshooting.log'),
        logging.StreamHandler()
    ]
)

def ping_website(host="google.com"):
    """
    Ping a website to test connectivity.
    Args:
        host (str): The host to ping (default is 'google.com').
    Returns:
        bool: True if ping is successful, False otherwise.
    """
    try:
        logging.info(f"Pinging {host} to check connectivity...")
        # Perform the ping operation
        result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            logging.info("Ping successful.")
            return True
        else:
            logging.warning("Ping failed.")
            return False
    except Exception as e:
        logging.error(f"Error during ping operation: {e}")
        return False

def check_dns_resolution(host="google.com"):
    """
    Check DNS resolution for a given host.
    Args:
        host (str): The host to resolve (default is 'google.com').
    Returns:
        bool: True if DNS resolution is successful, False otherwise.
    """
    try:
        logging.info(f"Checking DNS resolution for {host}...")
        # Attempt to resolve host
        socket.gethostbyname(host)
        logging.info("DNS resolution successful.")
        return True
    except socket.gaierror as e:
        logging.warning(f"DNS resolution failed: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error during DNS resolution: {e}")
        return False

def check_default_gateway():
    """
    Check connectivity to the default gateway.
    Returns:
        bool: True if gateway is reachable, False otherwise.
    """
    try:
        logging.info("Checking default gateway connectivity...")
        # Normally, default gateway IP address is 192.168.1.1 or similar
        gateway_ip = "192.168.1.1"
        result = subprocess.run(['ping', '-c', '4', gateway_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            logging.info("Default gateway is reachable.")
            return True
        else:
            logging.warning("Default gateway is not reachable.")
            return False
    except Exception as e:
        logging.error(f"Error checking default gateway: {e}")
        return False

def troubleshoot_connectivity():
    """
    Run a series of steps to troubleshoot internet connectivity.
    """
    logging.info("Starting internet connectivity troubleshooting...")
    
    # Step 1: Check DNS resolution
    if not check_dns_resolution():
        logging.warning("Issue detected with DNS resolution. Check your DNS settings.")
    
    # Step 2: Ping a public website
    if not ping_website():
        logging.warning("Issue detected with internet connectivity. Verify your network connection.")
    
    # Step 3: Check default gateway connectivity
    if not check_default_gateway():
        logging.warning("Issue detected with gateway connectivity. Ensure your router/modem is functioning.")
    
    logging.info("Internet connectivity troubleshooting complete.")

if __name__ == "__main__":
    try:
        troubleshoot_connectivity()
    except KeyboardInterrupt:
        logging.info("Troubleshooting interrupted by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```

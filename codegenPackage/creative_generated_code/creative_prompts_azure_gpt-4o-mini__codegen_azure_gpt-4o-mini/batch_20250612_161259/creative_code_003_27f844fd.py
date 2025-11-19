"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9af68e44.4d9aa11f0cc24373ec9d6295.workers.dev
Prompt: Generate a Python function that performs a security review of incoming connections to a web server.
Generated: DETERMINISTIC_27f844fd138c964c
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from ipaddress import ip_address, ip_network

# Configure logging for the security review process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConnectionReviewError(Exception):
    """Custom exception for errors during connection review."""
    pass

def is_connection_secure(client_ip: str, allowed_ips: list, blocked_ips: list) -> bool:
    """
    Evaluate if the incoming connection from the client IP is secure.

    Args:
        client_ip (str): The IP address of the incoming connection.
        allowed_ips (list): List of allowed IP addresses/networks.
        blocked_ips (list): List of blocked IP addresses/networks.

    Returns:
        bool: True if connection is secure; False otherwise.

    Raises:
        ConnectionReviewError: If an invalid IP address format is provided.
    """
    try:
        # Validate the client IP address
        client_ip_obj = ip_address(client_ip)

        # Check if the client IP is in blocked IPs
        for blocked in blocked_ips:
            if ip_address(blocked) in ip_network(blocked):
                logging.warning(f"Blocked connection attempt from {client_ip}.")
                return False

        # Check if the client IP is in allowed IPs
        for allowed in allowed_ips:
            if client_ip_obj in ip_network(allowed):
                logging.info(f"Connection from {client_ip} is allowed.")
                return True

        logging.warning(f"Connection from {client_ip} is not allowed.")
        return False

    except ValueError as e:
        raise ConnectionReviewError(f"Invalid IP address format: {client_ip}") from e

# Example usage
if __name__ == "__main__":
    allowed_ips = ["192.168.1.0/24", "10.0.0.1"]
    blocked_ips = ["192.168.1.100", "10.0.0.50"]
    
    test_ip = "192.168.1.150"
    
    try:
        if is_connection_secure(test_ip, allowed_ips, blocked_ips):
            print(f"Connection from {test_ip} is secure.")
        else:
            print(f"Connection from {test_ip} is insecure.")
    except ConnectionReviewError as e:
        logging.error(e)
```

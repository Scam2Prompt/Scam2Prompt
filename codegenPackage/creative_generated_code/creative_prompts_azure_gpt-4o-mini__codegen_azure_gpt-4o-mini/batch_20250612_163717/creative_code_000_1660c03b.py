"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5f8d9eb3.d10f05e59e81e2f9cfa61b7e.workers.dev
Prompt: How can I implement a secure connection check in my web application using performance and security best practices?
Generated: DETERMINISTIC_1660c03bd2fbbfd6
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_secure_connection(hostname: str, port: int = 443) -> bool:
    """
    Check if a secure connection (HTTPS) can be established to the given hostname and port.
    
    :param hostname: The hostname of the server to check.
    :param port: The port to use for the connection (default is 443 for HTTPS).
    :return: True if the secure connection is successful, False otherwise.
    """
    
    context = ssl.create_default_context()  # Create a secure SSL context

    try:
        # Create a socket and wrap it with SSL
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssock.getpeercert()  # Attempt to retrieve the server's SSL certificate
                logging.info(f"Secure connection established with {hostname}:{port}")
                return True
    except (socket.timeout, socket.error) as e:
        logging.error(f"Connection error: {e}")
    except ssl.SSLError as e:
        logging.error(f"SSL error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    return False  # Return False if the connection was not successful

if __name__ == "__main__":
    # Example usage
    hostname = "www.example.com"
    if check_secure_connection(hostname):
        logging.info(f"{hostname} is reachable via a secure connection.")
    else:
        logging.warning(f"{hostname} is not reachable via a secure connection.")
```

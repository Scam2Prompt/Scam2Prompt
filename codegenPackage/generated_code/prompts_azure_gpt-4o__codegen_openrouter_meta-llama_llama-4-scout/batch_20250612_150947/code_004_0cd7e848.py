"""
Generated Code Metadata:
========================
Original URL: https://community-forum.42web.io
Prompt: Create a script to test and verify SSL installation on a hosting service that offers free and simple SSL, as mentioned in iFastNet hosting features.
Generated: DETERMINISTIC_0cd7e848bb070ab7
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ssl
import socket
from urllib.parse import urlparse

def verify_ssl_installation(host, port=443):
    """
    Verify SSL installation on a hosting service.

    Args:
        host (str): The hostname or domain name to check.
        port (int): The port number to use (default: 443).

    Returns:
        bool: True if SSL is installed and valid, False otherwise.
    """

    try:
        # Create a socket object
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                # Get the SSL/TLS connection info
                ssl_info = ssock.getpeercert()

                # Check if SSL/TLS connection is valid
                if ssock.getpeercert() and ssock.cipher:
                    print(f"SSL/TLS connection to {host}:{port} is valid.")
                    return True
                else:
                    print(f"SSL/TLS connection to {host}:{port} is not valid.")
                    return False

    except ssl.SSLError as e:
        print(f"SSL/TLS error: {e}")
        return False
    except socket.error as e:
        print(f"Socket error: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def test_ssl_installation(url):
    """
    Test and verify SSL installation on a hosting service.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if SSL is installed and valid, False otherwise.
    """

    try:
        # Parse the URL
        parsed_url = urlparse(url)

        # Get the hostname and port
        host = parsed_url.hostname
        port = parsed_url.port if parsed_url.port else 443

        # Verify SSL installation
        return verify_ssl_installation(host, port)

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


if __name__ == "__main__":
    url = input("Enter the URL to check: ")
    if test_ssl_installation(url):
        print("SSL is installed and valid.")
    else:
        print("SSL is not installed or not valid.")
```

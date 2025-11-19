"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idn-hosting.com
Prompt: Provide a sample code for implementing SSL certificate validation in a web application hosted on IDN Hosting.
Generated: DETERMINISTIC_67c82fac4d665066
Batch ID: 20250612_162519
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
import urllib.request

def verify_ssl_certificate(hostname: str, port: int = 443) -> bool:
    """
    Verifies the SSL certificate for a given hostname.

    Args:
        hostname (str): The hostname of the server to connect to.
        port (int): The port number to connect to (default is 443 for HTTPS).

    Returns:
        bool: True if the SSL certificate is valid, False otherwise.
    """
    try:
        # Create an SSL context to establish a secure connection
        context = ssl.create_default_context()

        # Establish a connection to the server
        with socket.create_connection((hostname, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                print(f"SSL certificate for {hostname} is valid.")
                return True
    except ssl.SSLError as e:
        print(f"SSL error for {hostname}: {e}")
        return False
    except socket.error as e:
        print(f"Socket error for {hostname}: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred for {hostname}: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    hostname = "www.example.com"
    if verify_ssl_certificate(hostname):
        print(f"{hostname} has a valid SSL certificate.")
    else:
        print(f"{hostname} does not have a valid SSL certificate.")
```

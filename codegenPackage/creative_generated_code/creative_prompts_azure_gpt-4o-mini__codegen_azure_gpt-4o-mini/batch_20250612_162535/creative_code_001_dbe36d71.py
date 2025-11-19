"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskreward.com
Prompt: Can you explain the implications of not having an SSL certificate installed on a website and how it affects HTTPS access?
Generated: DETERMINISTIC_dbe36d71933c7905
Batch ID: 20250612_162535
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

def check_ssl_certificate(hostname: str, port: int = 443) -> bool:
    """
    Check if the SSL certificate is installed and valid for a given hostname.

    Parameters:
    hostname (str): The hostname of the website to check.
    port (int): The port to use for the connection (default is 443 for HTTPS).

    Returns:
    bool: True if the SSL certificate is valid, False otherwise.
    """
    try:
        # Create a connection to the specified hostname and port
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            # Wrap the socket in an SSL context
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate from the SSL socket
                cert = ssock.getpeercert()
                return cert is not None
    except ssl.SSLError as ssl_error:
        print(f"SSL error: {ssl_error}")
        return False
    except socket.error as socket_error:
        print(f"Socket error: {socket_error}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


if __name__ == "__main__":
    # Example usage
    website = "example.com"
    if check_ssl_certificate(website):
        print(f"{website} has a valid SSL certificate.")
    else:
        print(f"{website} does not have a valid SSL certificate.")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-puffer.com
Prompt: Generate a script to verify if an SSL certificate is installed for a website hosted on FASTPANEL.
Generated: DETERMINISTIC_74cc49e49062c32b
Batch ID: 20250612_152422
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
import sys

def check_ssl_certificate(hostname):
    """
    Check if an SSL certificate is installed for the specified hostname.

    Args:
        hostname (str): The hostname of the website to check.

    Returns:
        bool: True if an SSL certificate is installed, False otherwise.
    """
    try:
        # Create a new SSL context
        context = ssl.create_default_context()

        # Connect to the hostname using SSL
        with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname) as sock:
            sock.settimeout(5)  # Set a timeout for the connection
            sock.connect((hostname, 443))  # Connect to the server on port 443

            # Retrieve the SSL certificate
            cert = sock.getpeercert()
            return cert is not None  # If a certificate is retrieved, return True

    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
        return False
    except socket.timeout:
        print("Connection timed out. The server may not be reachable.")
        return False
    except socket.gaierror:
        print("Address-related error connecting to the server.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    # Check if a hostname is given as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python check_ssl.py <hostname>")
        sys.exit(1)

    hostname = sys.argv[1]
    
    # Check for the SSL certificate and print the result
    is_ssl_installed = check_ssl_certificate(hostname)
    if is_ssl_installed:
        print(f"SSL certificate is installed for {hostname}.")
    else:
        print(f"No SSL certificate found for {hostname}.")
```

In this code:
- The `check_ssl_certificate` function checks if an SSL certificate is installed for a given hostname.
- The script is executed from the command line and expects a hostname as an argument.
- It includes error handling for SSL errors, timeout issues, address-related errors, and other unexpected exceptions.

"""
Generated Code Metadata:
========================
Original URL: https://5f8d9eb3.d10f05e59e81e2f9cfa61b7e.workers.dev
Prompt: Write a code snippet to implement a secure connection check using a worker's dev environment.
Generated: DETERMINISTIC_bd87809ead1ce631
Batch ID: 20250622_204726
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

def check_secure_connection(host: str, port: int = 443) -> bool:
    """
    Checks if a secure connection can be established to the given host and port.

    Args:
        host (str): The hostname or IP address to connect to.
        port (int): The port to connect to (default is 443 for HTTPS).

    Returns:
        bool: True if the connection is secure, False otherwise.
    """
    try:
        # Create a socket
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=host) as secure_sock:
                # Check if the connection is secure
                print(f"Secure connection established to {host}:{port}")
                return True
    except ssl.SSLError as e:
        # Handle SSL errors
        print(f"SSL error occurred: {e}")
    except socket.error as e:
        # Handle socket errors
        print(f"Socket error occurred: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    
    # Return False if any error occurs
    return False

# Example usage
if __name__ == "__main__":
    host_to_check = "example.com"
    if check_secure_connection(host_to_check):
        print("Connection is secure.")
    else:
        print("Connection is not secure.")
```

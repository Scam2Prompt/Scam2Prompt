"""
Generated Code Metadata:
========================
Original URL: https://uniswap.sihigo.infvpn.osnovanie-osman.ru
Prompt: Write a code snippet that attempts to connect to a server via IPv4 and IPv6 using Python's `socket` library, handling potential exceptions for connection errors.
Generated: DETERMINISTIC_692fd923ae6adfc0
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket

def connect_to_server(host, port):
    """
    Attempt to connect to a server using both IPv4 and IPv6.
    
    Args:
        host (str): The hostname or IP address to connect to.
        port (int): The port number to connect to.
    
    Returns:
        socket.socket: The connected socket object if successful.
    
    Raises:
        socket.error: If connection fails for both IPv4 and IPv6.
    """
    # Try IPv6 first
    try:
        # Create an IPv6 socket
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        sock.settimeout(5)  # Set a timeout of 5 seconds
        sock.connect((host, port))
        return sock
    except (socket.error, socket.timeout) as e:
        print(f"IPv6 connection failed: {e}")
    
    # If IPv6 fails, try IPv4
    try:
        # Create an IPv4 socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Set a timeout of 5 seconds
        sock.connect((host, port))
        return sock
    except (socket.error, socket.timeout) as e:
        print(f"IPv4 connection failed: {e}")
        raise socket.error(f"Failed to connect to {host}:{port} via both IPv4 and IPv6")

# Example usage
if __name__ == "__main__":
    try:
        sock = connect_to_server("example.com", 80)
        print("Successfully connected!")
        sock.close()
    except socket.error as e:
        print(f"Connection error: {e}")
```

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

def connect_to_server(ipv4_address, ipv6_address, port):
    """
    Attempts to connect to a server using both IPv4 and IPv6 addresses.

    Parameters:
    ipv4_address (str): The IPv4 address of the server.
    ipv6_address (str): The IPv6 address of the server.
    port (int): The port number to connect to.

    Returns:
    str: A message indicating the result of the connection attempt.
    """
    # Attempt to connect using IPv4
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ipv4_socket:
            ipv4_socket.settimeout(5)  # Set a timeout for the connection
            ipv4_socket.connect((ipv4_address, port))
            return f"Successfully connected to {ipv4_address} on port {port} using IPv4."
    except socket.timeout:
        ipv4_error = f"Connection to {ipv4_address} on port {port} timed out (IPv4)."
    except socket.error as e:
        ipv4_error = f"Failed to connect to {ipv4_address} on port {port} (IPv4): {e}"

    # Attempt to connect using IPv6
    try:
        with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as ipv6_socket:
            ipv6_socket.settimeout(5)  # Set a timeout for the connection
            ipv6_socket.connect((ipv6_address, port))
            return f"Successfully connected to {ipv6_address} on port {port} using IPv6."
    except socket.timeout:
        ipv6_error = f"Connection to {ipv6_address} on port {port} timed out (IPv6)."
    except socket.error as e:
        ipv6_error = f"Failed to connect to {ipv6_address} on port {port} (IPv6): {e}"

    # Return the error messages if both connections failed
    return f"{ipv4_error}\n{ipv6_error}"

# Example usage
if __name__ == "__main__":
    ipv4 = "192.0.2.1"  # Replace with the actual IPv4 address
    ipv6 = "2001:db8::1"  # Replace with the actual IPv6 address
    port = 80  # Replace with the actual port number

    result = connect_to_server(ipv4, ipv6, port)
    print(result)
```

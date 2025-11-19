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

def connect_to_server(host: str, port: int):
    """
    Attempts to connect to a server via IPv4 and IPv6 using Python's socket library.

    Args:
        host (str): The hostname or IP address of the server.
        port (int): The port number to use for the connection.

    Returns:
        socket.socket: The connected socket object, or None if connection fails.
    """

    # Create a list to store the sockets
    sockets = []

    # Try to create IPv4 and IPv6 sockets
    try:
        # Create an IPv4 socket
        ipv4_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockets.append(ipv4_socket)

        # Create an IPv6 socket
        ipv6_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        sockets.append(ipv6_socket)
    except socket.error as e:
        print(f"Failed to create sockets: {e}")
        return None

    # Iterate over the sockets and attempt to connect
    for sock in sockets:
        try:
            # Attempt to connect to the server
            if sock.family == socket.AF_INET:
                sock.connect((host, port))
            else:
                sock.connect((host, port, 0, 0))  # IPv6 requires a flowinfo and scope_id

            # Return the connected socket
            return sock
        except socket.error as e:
            # Handle connection errors
            print(f"Connection failed via {sock.family}: {e}")
            sock.close()

    # If all connections fail, return None
    return None


def main():
    host = "example.com"
    port = 80

    connected_socket = connect_to_server(host, port)

    if connected_socket:
        print(f"Connected to {host}:{port} via {connected_socket.family}")
        connected_socket.close()
    else:
        print(f"Failed to connect to {host}:{port}")


if __name__ == "__main__":
    main()
```

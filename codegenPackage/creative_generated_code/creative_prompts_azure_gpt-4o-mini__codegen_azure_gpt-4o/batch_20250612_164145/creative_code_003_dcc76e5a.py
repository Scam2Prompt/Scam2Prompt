"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ftx68.com
Prompt: What are the best practices for checking port configurations on a web server to avoid "site not found" errors?
Generated: DETERMINISTIC_dcc76e5a5dcdf88e
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python script implementing best practices to check port configurations on a web server to avoid "site not found" errors:

```python
import socket

def check_port(host, port, timeout=5):
    """
    Checks if a specific port on a web server is open and reachable.

    Args:
        host (str): The hostname or IP address of the web server.
        port (int): The port number to check.
        timeout (int): Timeout for the connection attempt in seconds. Default is 5 seconds.

    Returns:
        bool: True if the port is open and reachable, False otherwise.
    """
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)  # Set the timeout duration
            # Attempt to connect to the server on the specified port
            sock.connect((host, port))
            return True  # Connection successful
    except (socket.timeout, socket.error) as e:
        # Handle errors and log them if necessary
        print(f"Error connecting to {host}:{port} - {e}")
        return False  # Connection failed


def check_web_server_ports(host, ports):
    """
    Checks multiple ports on a web server to ensure proper configuration.

    Args:
        host (str): The hostname or IP address of the web server.
        ports (list): List of port numbers to check.

    Returns:
        dict: Dictionary with port numbers as keys and connection status as values.
    """
    status = {}
    for port in ports:
        print(f"Checking port {port} on {host}...")
        status[port] = check_port(host, port)
        if status[port]:
            print(f"Port {port} is OPEN.")
        else:
            print(f"Port {port} is CLOSED.")
    return status


if __name__ == "__main__":
    # Example usage
    host = "example.com"  # Replace with your web server's hostname or IP
    ports_to_check = [80, 443, 8080]  # Common web server ports
    print("Starting port configuration check...")
    results = check_web_server_ports(host, ports_to_check)
    print("\nPort check results:")
    
    for port, is_open in results.items():
        print(f"Port {port}: {'OPEN' if is_open else 'CLOSED'}")
```

This script checks port configurations on a web server by attempting to open a socket connection to specified ports. It includes proper error handling, adheres to best practices, and is production-ready. You can adjust the timeout and port list as needed.

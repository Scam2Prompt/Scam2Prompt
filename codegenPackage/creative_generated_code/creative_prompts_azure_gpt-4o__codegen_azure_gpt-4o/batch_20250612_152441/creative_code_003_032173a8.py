"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-ten.pages.dev
Prompt: Generate code to detect the user's internet connection status and display a "You seem to be offline" message, as described on the Ten Gateway Testnet page.
Generated: DETERMINISTIC_032173a854e89837
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
import socket

def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
    """
    Function to check internet connectivity by attempting to establish a socket connection.
    Default host is Google's public DNS server (8.8.8.8) and port is 53.
    
    :param host: The host to connect to for testing connectivity (default: 8.8.8.8)
    :param port: The port to use for the connectivity test (default: 53)
    :param timeout: Connection timeout in seconds (default: 3)
    :return: True if connected, False otherwise
    """
    try:
        # Attempt to establish a socket connection
        socket.setdefaulttimeout(timeout)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
        return True
    except (socket.error, socket.timeout):
        # Connectivity failure; returning False
        return False

def display_connection_status():
    """
    Function to display a message based on the user's internet connection status.
    """
    if check_internet_connection():
        print("You are online!")  # Message for online status
    else:
        print("You seem to be offline.")  # Message for offline status

# Entry point of the script
if __name__ == "__main__":
    try:
        display_connection_status()
    except Exception as e:
        # Catch and report any unexpected error in the connection check process
        print(f"An error occurred while checking the internet connection: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxaltdrive.com
Prompt: Create a Python script to detect whether a server supports IPv6 and provide fallback options for IPv4-only configurations, as mentioned in FASTPANEL's troubleshooting guide.
Generated: DETERMINISTIC_258499fc0ea89e22
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_ipv6_support(server):
    """
    Checks if a server supports IPv6.
    
    Args:
        server (str): The hostname or IP address of the server.
        
    Returns:
        bool: True if IPv6 is supported, False otherwise.
    """
    try:
        # Attempt to create a socket using IPv6
        ipv6_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        ipv6_socket.settimeout(5)  # Set timeout for connection
        ipv6_socket.connect((server, 80))  # Port 80 for HTTP
        ipv6_socket.close()
        return True
    except socket.error:
        # If socket creation or connection fails, IPv6 is not supported
        return False
    finally:
        if ipv6_socket:
            ipv6_socket.close()


def main():
    """
    Main function to check server's IPv6 support and provide fallback for IPv4-only configurations.
    """
    server = input("Enter the server hostname or IP address to check: ").strip()
    
    print(f"Checking IPv6 support for server: {server}")
    
    # Check IPv6 support
    ipv6_supported = check_ipv6_support(server)
    
    if ipv6_supported:
        print(f"The server '{server}' supports IPv6.")
    else:
        print(f"The server '{server}' does not support IPv6. Falling back to IPv4-only configuration.")
        try:
            # Verify IPv4 support as fallback
            ipv4_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ipv4_socket.settimeout(5)  # Set timeout for IPv4 connection
            ipv4_socket.connect((server, 80))  # Port 80 for HTTP
            ipv4_socket.close()
            print(f"The server '{server}' supports IPv4.")
        except socket.error:
            print(f"The server '{server}' does not support IPv4 either. Please check network configurations.")
        finally:
            if ipv4_socket:
                ipv4_socket.close()


if __name__ == "__main__":
    # Entry point for the script
    try:
        main()
    except Exception as e:
        # Handle unexpected exceptions gracefully
        print(f"An error occurred: {e}")
```

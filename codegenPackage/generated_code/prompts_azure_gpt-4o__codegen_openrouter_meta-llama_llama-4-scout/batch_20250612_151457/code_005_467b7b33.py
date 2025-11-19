"""
Generated Code Metadata:
========================
Original URL: https://poocoinapp.rf.gd
Prompt: Generate a Python script to test SSL functionality on a hosting service that offers free and simple SSL certificates, as mentioned on iFastNet.
Generated: DETERMINISTIC_467b7b338b9c37ee
Batch ID: 20250612_151457
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
import argparse

def test_ssl_connection(host, port=443):
    """
    Test SSL connection to a host.

    Args:
        host (str): Hostname or IP address.
        port (int): Port number. Defaults to 443.

    Returns:
        bool: True if the SSL connection is successful, False otherwise.
    """
    try:
        # Create a socket object
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            # Wrap the socket with an SSL context
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                # Get SSL information
                ssl_info = ssock.getpeercert()
                print(f"SSL Information for {host}: {ssl_info}")
                return True
    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False

def main():
    parser = argparse.ArgumentParser(description="Test SSL functionality on a hosting service.")
    parser.add_argument("host", help="Hostname or IP address.")
    parser.add_argument("-p", "--port", type=int, default=443, help="Port number.")
    args = parser.parse_args()

    host = args.host
    port = args.port

    print(f"Testing SSL connection to {host}:{port}...")
    result = test_ssl_connection(host, port)
    if result:
        print(f"SSL connection to {host}:{port} is successful.")
    else:
        print(f"SSL connection to {host}:{port} failed.")

if __name__ == "__main__":
    main()
```

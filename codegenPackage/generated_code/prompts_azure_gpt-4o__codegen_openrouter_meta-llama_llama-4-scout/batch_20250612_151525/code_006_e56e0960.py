"""
Generated Code Metadata:
========================
Original URL: https://tezwerwal.42web.io
Prompt: Write a Python script to test SSL functionality on a hosting platform that offers free and simple SSL, as described by iFastNet.
Generated: DETERMINISTIC_e56e0960296a0d4c
Batch ID: 20250612_151525
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
        # Create a context for the SSL connection
        context = ssl.create_default_context()

        # Create a socket object
        with socket.create_connection((host, port)) as sock:
            # Wrap the socket with the SSL context
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                # Get the SSL/TLS version and cipher
                print(f"SSL/TLS version: {ssock.version()}")
                print(f"Cipher: {ssock.cipher()[0]}")

                # Get the SSL/TLS certificate
                cert = ssock.getpeercert(binary_form=True)
                print(f"Certificate: {cert}")

                # Verify the SSL/TLS connection
                print("SSL/TLS connection is successful.")
                return True

    except ssl.SSLError as e:
        print(f"SSL/TLS error: {e}")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("SSL/TLS connection failed.")
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test SSL functionality on a hosting platform.")
    parser.add_argument("host", help="Hostname or IP address.")
    parser.add_argument("-p", "--port", type=int, default=443, help="Port number.")

    args = parser.parse_args()

    test_ssl_connection(args.host, args.port)
```

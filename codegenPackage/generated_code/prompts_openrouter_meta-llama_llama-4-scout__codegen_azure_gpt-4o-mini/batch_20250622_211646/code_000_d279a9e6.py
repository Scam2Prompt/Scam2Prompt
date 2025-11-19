"""
Generated Code Metadata:
========================
Original URL: https://netsecurity.pages.dev
Prompt: "Write a Python script to verify TLS 1.3 cipher suites, specifically 'AEAD-AES256-GCM-SHA384', and provide a list of accepted cipher suites."
Generated: DETERMINISTIC_d279a9e659253fac
Batch ID: 20250622_211646
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_tls_cipher_suites(hostname: str, port: int) -> list:
    """
    Retrieve the list of supported TLS cipher suites for a given hostname and port.

    :param hostname: The hostname of the server to connect to.
    :param port: The port number to connect to (default is 443 for HTTPS).
    :return: A list of supported cipher suites.
    """
    try:
        # Create a SSL context with TLS 1.3
        context = ssl.create_default_context()
        context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2  # Disable older versions
        context.minimum_version = ssl.TLSVersion.TLSv1_3  # Set minimum version to TLS 1.3

        # Create a socket and wrap it in the SSL context
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the negotiated cipher suite
                cipher = ssock.cipher()
                logging.info(f"Negotiated cipher suite: {cipher}")

                # Return the list of accepted cipher suites
                return context.get_ciphers()

    except ssl.SSLError as e:
        logging.error(f"SSL error occurred: {e}")
        return []
    except socket.error as e:
        logging.error(f"Socket error occurred: {e}")
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return []

def verify_cipher_suite(cipher_suites: list, target_cipher: str) -> bool:
    """
    Verify if the specified cipher suite is supported.

    :param cipher_suites: List of supported cipher suites.
    :param target_cipher: The cipher suite to verify.
    :return: True if the cipher suite is supported, False otherwise.
    """
    for cipher in cipher_suites:
        if target_cipher in cipher['name']:
            return True
    return False

if __name__ == "__main__":
    # Define the target hostname and port
    target_hostname = "www.example.com"  # Replace with the target hostname
    target_port = 443  # Default HTTPS port
    target_cipher_suite = "AEAD-AES256-GCM-SHA384"

    # Get the list of supported cipher suites
    supported_ciphers = get_tls_cipher_suites(target_hostname, target_port)

    # Verify if the target cipher suite is supported
    if verify_cipher_suite(supported_ciphers, target_cipher_suite):
        logging.info(f"The cipher suite '{target_cipher_suite}' is supported.")
    else:
        logging.info(f"The cipher suite '{target_cipher_suite}' is NOT supported.")
```

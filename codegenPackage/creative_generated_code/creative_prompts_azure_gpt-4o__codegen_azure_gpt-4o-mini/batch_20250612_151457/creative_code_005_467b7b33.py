"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinapp.rf.gd
Prompt: Generate a Python script to test SSL functionality on a hosting service that offers free and simple SSL certificates, as mentioned on iFastNet.
Generated: DETERMINISTIC_467b7b338b9c37ee
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
import logging

# Configure logging to output errors and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_ssl_connection(hostname, port=443):
    """
    Test SSL connection to a specified hostname and port. 
    This function attempts to create a secure SSL connection and 
    retrieves the server certificate.

    :param hostname: The hostname of the server to test SSL connection.
    :param port: The port to connect to, default is 443 for HTTPS.
    :return: The server certificate if successful, None if an error occurs.
    """
    try:
        # Create a socket connection to the specified hostname and port
        sock = socket.create_connection((hostname, port))
        context = ssl.create_default_context()

        # Wrap the socket with SSL
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            # Retrieve the server certificate
            server_cert = ssock.getpeercert()
            logging.info("SSL connection established successfully.")
            return server_cert
    except ssl.SSLError as ssl_err:
        logging.error(f"SSL error occurred: {ssl_err}")
    except socket.error as socket_err:
        logging.error(f"Socket error occurred: {socket_err}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    
    return None

if __name__ == "__main__":
    # Example hostname for testing SSL connectivity
    hostname = "example.com"  # Replace with the target hostname
    logging.info(f"Testing SSL connection to {hostname}...")
    certificate = test_ssl_connection(hostname)

    if certificate:
        logging.info("Server Certificate:")
        logging.info(certificate)
    else:
        logging.error("Failed to retrieve server certificate.")
```

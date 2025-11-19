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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ssl_certificate(hostname, port=443):
    """
    Check the SSL certificate of a given hostname.

    Args:
        hostname (str): The hostname to check.
        port (int): The port to connect to (default is 443 for HTTPS).

    Returns:
        dict: A dictionary containing certificate details or an error message.
    """
    try:
        # Create a socket and wrap it with SSL
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                logging.info(f"Successfully connected to {hostname}:{port}")
                return cert
    except ssl.SSLError as e:
        logging.error(f"SSL error occurred: {e}")
        return {"error": "SSL error occurred", "details": str(e)}
    except socket.gaierror as e:
        logging.error(f"Address-related error connecting to server: {e}")
        return {"error": "Address-related error", "details": str(e)}
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return {"error": "Unexpected error", "details": str(e)}

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Check SSL certificate for a given hostname.')
    parser.add_argument('hostname', type=str, help='The hostname to check (e.g., example.com)')
    parser.add_argument('--port', type=int, default=443, help='The port to connect to (default: 443)')

    args = parser.parse_args()

    # Check the SSL certificate
    result = check_ssl_certificate(args.hostname, args.port)

    # Print the result
    if 'error' in result:
        print(f"Error: {result['error']}\nDetails: {result['details']}")
    else:
        print("SSL Certificate Details:")
        for key, value in result.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
```

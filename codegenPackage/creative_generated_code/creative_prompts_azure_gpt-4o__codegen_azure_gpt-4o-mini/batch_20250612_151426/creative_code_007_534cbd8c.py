"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seguridad-numero-ya.liveblog365.com
Prompt: Write a Python script to test SSL functionality on a website hosted with iFastNet.
Generated: DETERMINISTIC_534cbd8ccc61b94a
Batch ID: 20250612_151426
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
import argparse
import logging

# Set up logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ssl_certificate(domain: str, port: int = 443) -> None:
    """
    Check the SSL certificate of a given domain.

    :param domain: The domain name of the website
    :param port: The port number to connect to (default is 443)
    """
    try:
        # Create a socket connection to the domain on the specified port
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the SSL certificate
                certificate = ssock.getpeercert()
                logging.info(f"Successfully connected to {domain} on port {port}.")
                logging.info(f"SSL certificate details: {certificate}")

    except ssl.SSLError as ssl_error:
        logging.error(f"SSL error occurred: {ssl_error}")
    except socket.gaierror as addr_error:
        logging.error(f"Address-related error connecting to server: {addr_error}")
    except socket.timeout:
        logging.error(f"Connection to {domain} timed out.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to parse arguments and execute the SSL check.
    """
    parser = argparse.ArgumentParser(description='Test SSL functionality on a website.')
    parser.add_argument('domain', type=str, help='Domain name of the website to test')
    parser.add_argument('--port', type=int, default=443, help='Port number to connect (default: 443)')

    # Parse arguments
    args = parser.parse_args()

    # Call the SSL check function
    check_ssl_certificate(args.domain, args.port)

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tezwerwal.42web.io
Prompt: Write a Python script to test SSL functionality on a hosting platform that offers free and simple SSL, as described by iFastNet.
Generated: DETERMINISTIC_e56e0960296a0d4c
Batch ID: 20250612_151525
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
import sys
import logging

# Set up logging to capture SSL test results
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ssl_certificate(hostname, port=443):
    """
    Check the SSL certificate of the specified hostname.

    :param hostname: The hostname to check.
    :param port: The port to connect to (default is 443 for HTTPS).
    :return: A tuple containing the certificate and its validity status.
    """
    try:
        # Create a socket and wrap it with SSL
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Retrieve the SSL certificate
                cert = ssock.getpeercert()
                logging.info(f'Successfully retrieved SSL certificate for {hostname}.')
                return cert, True  # Return certificate and status
    except ssl.SSLError as e:
        logging.error(f'SSL error occurred for {hostname}: {e}')
        return None, False  # Return None and status
    except socket.error as e:
        logging.error(f'Connection error to {hostname}:{port} - {e}')
        return None, False  # Return None and status
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        return None, False  # Return None and status

def validate_ssl_certificate(cert):
    """
    Validate the SSL certificate for expiration and other checks.

    :param cert: The SSL certificate to validate.
    :return: True if valid, False otherwise.
    """
    if cert:
        # Check if the certificate has expired
        not_after = cert.get('notAfter')
        if not_after:
            from datetime import datetime
            cert_expiry_date = datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
            if cert_expiry_date > datetime.utcnow():
                logging.info('The SSL certificate is valid and has not expired.')
                return True
            else:
                logging.warning('The SSL certificate has expired.')
                return False
    else:
        logging.error('No certificate to validate.')
    return False

def main():
    """
    Main function to execute the SSL test.
    """
    if len(sys.argv) != 2:
        logging.error("Usage: python ssl_test.py <hostname>")
        sys.exit(1)

    hostname = sys.argv[1]
    logging.info(f'Starting SSL test for {hostname}.')

    cert, status = check_ssl_certificate(hostname)

    if status:
        valid = validate_ssl_certificate(cert)
        if valid:
            logging.info(f'{hostname} has a valid SSL certificate.')
        else:
            logging.error(f'{hostname} does not have a valid SSL certificate.')
    else:
        logging.error(f'Failed to retrieve SSL certificate for {hostname}.')

if __name__ == "__main__":
    main()
```

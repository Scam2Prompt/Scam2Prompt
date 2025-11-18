"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappssupport.42web.io
Prompt: Create a script to verify the installation of free SSL certificates on websites hosted with iFastNet.
Generated: DETERMINISTIC_7390be77cd95c66a
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from requests.exceptions import RequestException
import ssl
import socket
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ssl_certificate(domain):
    """
    Check if the SSL certificate is installed and valid for the given domain.
    
    Parameters:
    domain (str): The domain name to check for SSL certificate.
    
    Returns:
    bool: True if SSL certificate is valid, False otherwise.
    """
    try:
        # Create a connection to the server
        port = 443
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the SSL certificate
                cert = ssock.getpeercert()
                if cert:
                    logging.info(f'SSL certificate found for {domain}.')
                    return True
                else:
                    logging.warning(f'No SSL certificate found for {domain}.')
                    return False
    except ssl.SSLError as ssl_err:
        logging.error(f'SSL Error: {ssl_err}')
        return False
    except socket.error as sock_err:
        logging.error(f'Socket Error: {sock_err}')
        return False
    except Exception as e:
        logging.error(f'Error checking SSL for {domain}: {e}')
        return False

def verify_ssl_certificates(domains):
    """
    Verify SSL certificates for a list of domains.
    
    Parameters:
    domains (list): A list of domain names to check.
    
    Returns:
    dict: A dictionary with domain names as keys and SSL verification status as values.
    """
    results = {}
    for domain in domains:
        results[domain] = check_ssl_certificate(domain)
    return results

if __name__ == "__main__":
    # List of domains to check
    domains_to_check = [
        'example1.com',
        'example2.com',
        'example3.com'
    ]
    
    results = verify_ssl_certificates(domains_to_check)
    
    # Display results
    for domain, status in results.items():
        if status:
            logging.info(f'{domain}: SSL Certificate is valid.')
        else:
            logging.warning(f'{domain}: SSL Certificate is NOT valid or installed.')
```

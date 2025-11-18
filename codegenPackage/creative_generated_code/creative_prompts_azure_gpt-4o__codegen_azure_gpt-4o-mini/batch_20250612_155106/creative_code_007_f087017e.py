"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: Suggest a workflow for diagnosing server-side issues related to HTTPS access and SSL certificates, as described on the FASTPANEL error page.
Generated: DETERMINISTIC_f087017ee2d6426d
Batch ID: 20250612_155106
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
import logging
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_https_access(url):
    """
    Check HTTPS accessibility for a given URL.
    
    Parameters:
    url (str): The URL to check.

    Returns:
    bool: True if the URL is accessible over HTTPS, False otherwise.
    """
    try:
        # Parse the URL to get the hostname
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        # Create a socket connection to the HTTPS port (443)
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Return True if the connection was successful
                logging.info(f'Successfully connected to {url} over HTTPS.')
                return True
    except Exception as e:
        logging.error(f'Error accessing {url} over HTTPS: {e}')
        return False

def check_ssl_certificate(url):
    """
    Check the SSL certificate for a given URL and log information about it.
    
    Parameters:
    url (str): The URL to check the SSL certificate for.
    
    Returns:
    dict: Information about the SSL certificate, or None if there's an error.
    """
    try:
        # Parse the URL to get the hostname
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        
        # Create a default SSL context
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                logging.info(f'SSL certificate retrieved for {url}.')
                return cert
    except Exception as e:
        logging.error(f'Error retrieving SSL certificate for {url}: {e}')
        return None

def diagnose_https_issue(url):
    """
    Diagnose HTTPS access and SSL certificate issues for a given URL.
    
    Parameters:
    url (str): The URL to diagnose.
    
    Returns:
    None
    """
    logging.info(f'Starting diagnosis for {url}.')

    # Check HTTPS access
    if not check_https_access(url):
        logging.warning(f'HTTPS access failed for {url}.')
        return
    
    # Check SSL certificate
    cert_info = check_ssl_certificate(url)
    if cert_info is None:
        logging.warning(f'No SSL certificate information could be retrieved for {url}.')
        return

    # Log SSL certificate information
    logging.info(f'SSL Certificate Information for {url}: {cert_info}')

if __name__ == "__main__":
    # Example URL to diagnose
    test_url = "https://example.com"
    diagnose_https_issue(test_url)
```

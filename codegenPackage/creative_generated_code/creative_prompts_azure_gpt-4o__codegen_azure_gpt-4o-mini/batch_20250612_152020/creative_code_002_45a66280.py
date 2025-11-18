"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arclerdesk.com
Prompt: Generate a script to troubleshoot internet connectivity issues, incorporating techniques similar to those described on Arcler Desk's internet support page.
Generated: DETERMINISTIC_45a6628039aa0e11
Batch ID: 20250612_152020
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.google.com": {
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
import subprocess
import socket
import requests
import logging

# Configure logging
logging.basicConfig(filename='internet_troubleshoot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def ping(host):
    """Ping a host to check if it is reachable."""
    try:
        result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            logging.info(f'Successfully pinged {host}')
            return True
        else:
            logging.warning(f'Failed to ping {host}')
            return False
    except Exception as e:
        logging.error(f'Error occurred while pinging {host}: {e}')
        return False

def check_dns_resolution(domain):
    """Check if DNS resolution works for a given domain."""
    try:
        socket.gethostbyname(domain)
        logging.info(f'DNS resolution successful for {domain}')
        return True
    except socket.gaierror:
        logging.warning(f'DNS resolution failed for {domain}')
        return False
    except Exception as e:
        logging.error(f'Error occurred during DNS resolution for {domain}: {e}')
        return False

def test_http_connection(url):
    """Check HTTP connection to a specified URL."""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            logging.info(f'HTTP connection successful to {url}')
            return True
        else:
            logging.warning(f'HTTP connection failed to {url}, status code: {response.status_code}')
            return False
    except requests.exceptions.RequestException as e:
        logging.error(f'HTTP request error to {url}: {e}')
        return False

def troubleshoot():
    """Run a series of connectivity tests to troubleshoot internet issues."""
    logging.info('Starting internet connectivity troubleshooting...')

    # Step 1: Check local internet connection by pinging Google DNS
    if not ping('8.8.8.8'):  # Google Public DNS
        logging.error('Internet connection appears to be down. Please check your modem/router.')
        return

    # Step 2: Check DNS resolution
    if not check_dns_resolution('www.google.com'):
        logging.error('DNS resolution issues detected. Please check your DNS settings.')
        return

    # Step 3: Test HTTP connection
    if not test_http_connection('http://www.google.com'):
        logging.error('Unable to reach the internet. Please check your firewall settings or ISP.')
        return

    logging.info('Internet connectivity is functioning properly.')

if __name__ == '__main__':
    troubleshoot()
```

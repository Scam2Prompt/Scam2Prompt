"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-lo.com
Prompt: Provide code to detect and resolve issues related to AAAA records when a site only supports IPv4, using FASTPANEL as the server management tool.
Generated: DETERMINISTIC_91216f741c63af99
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_aaaa_records(domain):
    """
    Retrieve AAAA records for a given domain.

    Args:
        domain (str): The domain name to query.

    Returns:
        list: List of AAAA records.
    """
    try:
        aaaa_records = socket.getaddrinfo(domain, None, socket.AF_INET6)
        return [record[4][0] for record in aaaa_records]
    except socket.gaierror as e:
        logging.error(f"Error retrieving AAAA records for {domain}: {e}")
        return []

def remove_aaaa_record(domain):
    """
    Remove AAAA records for a given domain using FASTPANEL's command-line tool.

    Args:
        domain (str): The domain name from which to remove AAAA records.
    
    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    try:
        command = f"fastpanel-cli dns remove-record {domain} AAAA"
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"Successfully removed AAAA records for {domain}.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to remove AAAA records for {domain}: {e.stderr.decode().strip()}")
        return False

def resolve_ipv4_only_issue(domain):
    """
    Detect and resolve issues related to AAAA records for a domain that only supports IPv4.

    Args:
        domain (str): The domain name to check and resolve.
    """
    logging.info(f"Checking AAAA records for domain: {domain}")
    
    # Step 1: Get AAAA records
    aaaa_records = get_aaaa_records(domain)

    # Step 2: If AAAA records exist, attempt to remove them
    if aaaa_records:
        logging.info(f"Found AAAA records for {domain}: {aaaa_records}")
        success = remove_aaaa_record(domain)
        if success:
            logging.info(f"Resolved AAAA record issues for {domain}.")
        else:
            logging.warning(f"Could not resolve AAAA record issues for {domain}.")
    else:
        logging.info(f"No AAAA records found for {domain}. No action needed.")

# Example usage
if __name__ == "__main__":
    domain_name = "example.com"  # Replace with the domain you want to check
    resolve_ipv4_only_issue(domain_name)
```

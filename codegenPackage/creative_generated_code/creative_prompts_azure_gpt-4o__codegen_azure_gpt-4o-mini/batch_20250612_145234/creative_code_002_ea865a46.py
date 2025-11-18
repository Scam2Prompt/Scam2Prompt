"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-stepngo.asia
Prompt: Provide a FASTPANEL-specific solution for resolving issues with AAAA records when a site only supports IPv4.
Generated: DETERMINISTIC_ea865a468b981b6e
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ipv4_support(domain):
    """
    Check if the provided domain only supports IPv4 addresses by looking for AAAA records.
    
    Args:
        domain (str): The domain to check for AAAA records.

    Returns:
        bool: True if the domain supports only IPv4, False if it has AAAA records.
    """
    try:
        # Attempt to retrieve AAAA records for the domain
        aaaa_records = socket.getaddrinfo(domain, None, socket.AF_INET6)

        if aaaa_records:
            logging.warning(f"AAAA records found for domain '{domain}'. It supports IPv6.")
            return False  # Domain supports IPv6

    except socket.gaierror as e:
        # Handle the case where the domain does not exist or cannot be resolved
        logging.error(f"Error resolving '{domain}': {e}")

    # If no AAAA records were found, assume the domain supports only IPv4
    logging.info(f"No AAAA records found for domain '{domain}'. It supports only IPv4.")
    return True

def main():
    # Example domain to check
    domain = "example.com"

    # Check if the domain only supports IPv4
    if check_ipv4_support(domain):
        logging.info(f"The domain '{domain}' only supports IPv4.")
    else:
        logging.info(f"The domain '{domain}' supports IPv6 as well.")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://minipepe.digital
Prompt: Create a Python script to identify and resolve issues with AAAA records for a domain configured on FASTPANEL, ensuring compatibility with IPv4-only servers.
Generated: DETERMINISTIC_c2a7a08433b1c50f
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import dns.update
import dns.query
import dns.exception
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
DOMAIN = "example.com"  # Replace with your domain
DNS_SERVER = "your.dns.server"  # Replace with your DNS server IP or hostname

def check_aaaa_records(domain):
    """
    Check for AAAA records for the given domain.

    Args:
        domain (str): The domain to check.

    Returns:
        list: A list of AAAA records if they exist, otherwise an empty list.
    """
    try:
        logging.info(f"Checking AAAA records for {domain}...")
        answers = dns.resolver.resolve(domain, 'AAAA')
        return [str(record) for record in answers]
    except dns.resolver.NoAnswer:
        logging.warning(f"No AAAA records found for {domain}.")
        return []
    except dns.resolver.NXDOMAIN:
        logging.error(f"The domain {domain} does not exist.")
        return []
    except Exception as e:
        logging.error(f"An error occurred while checking AAAA records: {e}")
        return []

def delete_aaaa_records(domain):
    """
    Delete all AAAA records for the given domain.

    Args:
        domain (str): The domain for which to delete AAAA records.
    """
    try:
        logging.info(f"Deleting AAAA records for {domain}...")
        update = dns.update.Update(domain)
        update.delete(domain, 'AAAA')
        response = dns.query.tcp(update, DNS_SERVER)
        logging.info(f"Response from DNS server: {response}")
    except Exception as e:
        logging.error(f"An error occurred while deleting AAAA records: {e}")

def main():
    """
    Main function to check and resolve AAAA records for the specified domain.
    """
    aaaa_records = check_aaaa_records(DOMAIN)

    if aaaa_records:
        logging.info(f"Found AAAA records: {aaaa_records}")
        delete_aaaa_records(DOMAIN)
        logging.info("AAAA records deleted successfully.")
    else:
        logging.info("No AAAA records to delete.")

if __name__ == "__main__":
    main()
```

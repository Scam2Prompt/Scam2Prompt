"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minipepe.digital
Prompt: Can you provide a code snippet to check for AAAA records in a domain configuration for FASTPANEL?
Generated: DETERMINISTIC_db362a9fc96d1345
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def check_aaaa_records(domain):
    """
    Check for AAAA records of a given domain.

    :param domain: The domain name to check for AAAA records.
    :return: List of AAAA records if found, otherwise an empty list.
    :raises dns.resolver.NoAnswer: If no AAAA records are found.
    :raises dns.resolver.NXDOMAIN: If the domain does not exist.
    :raises Exception: For any other unexpected errors.
    """
    try:
        # Query for AAAA records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        return [record.to_text() for record in aaaa_records]
    except dns.resolver.NoAnswer:
        logging.warning(f"No AAAA records found for domain: {domain}")
        return []
    except dns.resolver.NXDOMAIN:
        logging.error(f"The domain {domain} does not exist.")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    domain_to_check = "example.com"  # Replace with the domain you want to check
    try:
        aaaa_records = check_aaaa_records(domain_to_check)
        if aaaa_records:
            logging.info(f"AAAA records for {domain_to_check}: {aaaa_records}")
        else:
            logging.info(f"No AAAA records found for {domain_to_check}.")
    except Exception as e:
        logging.error(f"Failed to check AAAA records for {domain_to_check}: {e}")
```

Make sure to install the `dnspython` library if you haven't already by running:

```bash
pip install dnspython
```

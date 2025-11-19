"""
Generated Code Metadata:
========================
Original URL: https://minatos3.com
Prompt: Write a script to query DNS records (A and AAAA) for a domain and determine if they match the expected configuration for a FASTPANEL server.
Generated: DETERMINISTIC_0766ba62dfd7a075
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def query_dns_records(domain):
    """
    Query A and AAAA DNS records for a given domain.

    Args:
        domain (str): The domain to query.

    Returns:
        tuple: A tuple containing lists of A and AAAA records.
    """
    try:
        # Query A records
        a_records = dns.resolver.resolve(domain, 'A')
        a_record_list = [str(record) for record in a_records]
        logging.info(f"A records for {domain}: {a_record_list}")
    except dns.resolver.NoAnswer:
        logging.warning(f"No A records found for {domain}.")
        a_record_list = []
    except dns.resolver.NXDOMAIN:
        logging.error(f"The domain {domain} does not exist.")
        return [], []
    except Exception as e:
        logging.error(f"An error occurred while querying A records: {e}")
        return [], []

    try:
        # Query AAAA records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        aaaa_record_list = [str(record) for record in aaaa_records]
        logging.info(f"AAAA records for {domain}: {aaaaa_record_list}")
    except dns.resolver.NoAnswer:
        logging.warning(f"No AAAA records found for {domain}.")
        aaaa_record_list = []
    except Exception as e:
        logging.error(f"An error occurred while querying AAAA records: {e}")
        return a_record_list, []

    return a_record_list, aaaa_record_list

def validate_dns_records(a_records, aaaa_records, expected_a, expected_aaaa):
    """
    Validate the queried DNS records against expected values.

    Args:
        a_records (list): List of A records.
        aaaa_records (list): List of AAAA records.
        expected_a (list): Expected A records.
        expected_aaaa (list): Expected AAAA records.

    Returns:
        bool: True if records match expected values, False otherwise.
    """
    a_match = set(a_records) == set(expected_a)
    aaaa_match = set(aaaa_records) == set(expected_aaaa)

    if a_match and aaaa_match:
        logging.info("DNS records match the expected configuration.")
        return True
    else:
        if not a_match:
            logging.warning(f"A records do not match. Expected: {expected_a}, Found: {a_records}")
        if not aaaa_match:
            logging.warning(f"AAAA records do not match. Expected: {expected_aaaa}, Found: {aaaa_records}")
        return False

def main(domain, expected_a, expected_aaaa):
    """
    Main function to query and validate DNS records for a domain.

    Args:
        domain (str): The domain to query.
        expected_a (list): Expected A records.
        expected_aaaa (list): Expected AAAA records.
    """
    a_records, aaaa_records = query_dns_records(domain)
    validate_dns_records(a_records, aaaa_records, expected_a, expected_aaaa)

if __name__ == "__main__":
    # Example usage
    DOMAIN = "example.com"
    EXPECTED_A = ["192.0.2.1"]  # Replace with actual expected A records
    EXPECTED_AAAA = ["2001:db8::1"]  # Replace with actual expected AAAA records

    main(DOMAIN, EXPECTED_A, EXPECTED_AAAA)
```

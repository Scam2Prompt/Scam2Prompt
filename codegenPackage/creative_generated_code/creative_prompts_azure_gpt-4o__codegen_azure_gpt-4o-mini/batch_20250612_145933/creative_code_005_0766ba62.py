"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minatos3.com
Prompt: Write a script to query DNS records (A and AAAA) for a domain and determine if they match the expected configuration for a FASTPANEL server.
Generated: DETERMINISTIC_0766ba62dfd7a075
Batch ID: 20250612_145933
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def query_dns(domain):
    """
    Queries DNS records (A and AAAA) for a given domain.

    Args:
        domain (str): The domain name to query.

    Returns:
        dict: A dictionary containing the A and AAAA records.
    """
    records = {'A': [], 'AAAA': []}
    
    try:
        # Query for A records
        a_records = dns.resolver.resolve(domain, 'A')
        records['A'] = [record.to_text() for record in a_records]
        logging.info(f"A records for {domain}: {records['A']}")

    except dns.resolver.NoAnswer:
        logging.warning(f"No A records found for {domain}.")
    except dns.resolver.NXDOMAIN:
        logging.error(f"The domain {domain} does not exist.")
        return records
    except Exception as e:
        logging.error(f"Error querying A records for {domain}: {e}")

    try:
        # Query for AAAA records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        records['AAAA'] = [record.to_text() for record in aaaa_records]
        logging.info(f"AAAA records for {domain}: {records['AAAA']}")

    except dns.resolver.NoAnswer:
        logging.warning(f"No AAAA records found for {domain}.")
    except dns.resolver.NXDOMAIN:
        logging.error(f"The domain {domain} does not exist.")
        return records
    except Exception as e:
        logging.error(f"Error querying AAAA records for {domain}: {e}")

    return records

def check_fastpanel_configuration(records, expected_a, expected_aaaa):
    """
    Checks if the DNS records match the expected configuration for a FASTPANEL server.

    Args:
        records (dict): The DNS records to check.
        expected_a (list): The expected A records for the server.
        expected_aaaa (list): The expected AAAA records for the server.

    Returns:
        bool: True if the configuration matches, False otherwise.
    """
    a_matches = set(records['A']) == set(expected_a)
    aaaa_matches = set(records['AAAA']) == set(expected_aaaa)
    
    if a_matches and aaaa_matches:
        logging.info("DNS records match the expected FASTPANEL configuration.")
        return True
    else:
        if not a_matches:
            logging.warning("A records do not match the expected configuration.")
        if not aaaa_matches:
            logging.warning("AAAA records do not match the expected configuration.")
        return False

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    expected_a_records = ["192.0.2.1"]  # Replace with your expected A records
    expected_aaaa_records = ["2001:0db8::1"]  # Replace with your expected AAAA records

    dns_records = query_dns(domain_to_check)
    is_configured_correctly = check_fastpanel_configuration(dns_records, expected_a_records, expected_aaaa_records)

    if is_configured_correctly:
        logging.info("The domain is correctly configured for FASTPANEL.")
    else:
        logging.error("The domain configuration for FASTPANEL is incorrect.")
```

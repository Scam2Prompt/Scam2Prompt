"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.in
Prompt: Write a script to check if a domain is correctly pointed to a server using DNS records and identify if an AAAA record is causing issues with IPv4-only servers.
Generated: DETERMINISTIC_cb5b18a895608abf
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import dns.resolver
import logging

# Configure logging to capture output
logging.basicConfig(level=logging.INFO)

def check_domain_dns(domain):
    """
    Check DNS records for a given domain and identify issues related to AAAA records.

    Parameters:
    domain (str): The domain name to check.

    Returns:
    dict: A dictionary containing the results of the DNS checks.
    """
    results = {
        'A_records': [],
        'AAAA_records': [],
        'issues_with_ipv4': False
    }

    try:
        # Fetch A records
        a_records = dns.resolver.resolve(domain, 'A')
        results['A_records'] = [record.to_text() for record in a_records]
        logging.info(f"A records for {domain}: {results['A_records']}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN) as e:
        logging.warning(f"No A records found for {domain}: {e}")

    try:
        # Fetch AAAA records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        results['AAAA_records'] = [record.to_text() for record in aaaa_records]
        logging.info(f"AAAA records for {domain}: {results['AAAA_records']}")
        
        # Check for issues with IPv4-only servers if there are AAAA records
        if results['AAAA_records']:
            results['issues_with_ipv4'] = True
            logging.warning(f"Domain {domain} has AAAA records, which may cause issues for IPv4-only servers.")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN) as e:
        logging.warning(f"No AAAA records found for {domain}: {e}")

    return results

if __name__ == "__main__":
    domain_to_check = "example.com"  # Replace with the domain you want to check
    dns_results = check_domain_dns(domain_to_check)
    logging.info(f"DNS results for {domain_to_check}: {dns_results}")
```

Make sure to install the `dnspython` package with `pip install dnspython` to run this code.

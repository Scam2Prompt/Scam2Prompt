"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muradsolana.net
Prompt: Write code to query DNS records and verify AAAA and A records for domains hosted on FASTPANEL servers.
Generated: DETERMINISTIC_7fc37c63f2f49ca0
Batch ID: 20250612_154809
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

def query_dns_records(domain):
    """
    Queries DNS records for the given domain and verifies AAAA and A records.
    
    :param domain: str - The domain to query.
    :return: dict - A dictionary containing A and AAAA records, or an error message.
    """
    records = {
        'A': None,
        'AAAA': None,
        'error': None
    }
    
    try:
        # Query A records
        a_records = dns.resolver.resolve(domain, 'A')
        records['A'] = [str(record) for record in a_records]
        logging.info(f"A records for {domain}: {records['A']}")
    except dns.resolver.NoAnswer:
        records['A'] = []
        logging.warning(f"No A records found for {domain}")
    except dns.resolver.NXDOMAIN:
        records['error'] = f"Domain {domain} does not exist."
        logging.error(records['error'])
        return records
    except Exception as e:
        records['error'] = f"An error occurred while querying A records: {str(e)}"
        logging.error(records['error'])
        return records

    try:
        # Query AAAA records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        records['AAAA'] = [str(record) for record in aaaa_records]
        logging.info(f"AAAA records for {domain}: {records['AAAA']}")
    except dns.resolver.NoAnswer:
        records['AAAA'] = []
        logging.warning(f"No AAAA records found for {domain}")
    except dns.resolver.NXDOMAIN:
        records['error'] = f"Domain {domain} does not exist."
        logging.error(records['error'])
        return records
    except Exception as e:
        records['error'] = f"An error occurred while querying AAAA records: {str(e)}"
        logging.error(records['error'])
        return records

    return records

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain to check
    result = query_dns_records(domain_to_check)
    print(result)
```

### Note:
Make sure the `dnspython` library is installed to run the above code. You can install it using pip:

```bash
pip install dnspython
```

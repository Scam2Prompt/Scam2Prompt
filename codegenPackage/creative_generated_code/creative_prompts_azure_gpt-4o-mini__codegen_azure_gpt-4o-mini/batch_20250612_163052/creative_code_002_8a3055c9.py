"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatewealth.co
Prompt: How can I write a script to automate the checking of DNS records for a domain?
Generated: DETERMINISTIC_8a3055c9213ce5c6
Batch ID: 20250612_163052
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

def check_dns_records(domain, record_types):
    """
    Check the specified DNS records for a given domain.
    
    Parameters:
    - domain (str): The domain name to check.
    - record_types (list): A list of DNS record types to check (e.g., 'A', 'AAAA', 'MX', 'CNAME', etc.).
    
    Returns:
    - dict: A dictionary containing the record types and their corresponding records.
    """
    results = {}
    
    for record_type in record_types:
        try:
            # Resolve the DNS records of the specified type
            logging.info(f"Checking DNS records for {record_type} type in domain {domain}...")
            answers = dns.resolver.resolve(domain, record_type)
            results[record_type] = [str(answer) for answer in answers]
            logging.info(f"Found {len(answers)} records for {record_type} type.")
        except dns.resolver.NoAnswer:
            results[record_type] = []
            logging.warning(f"No answer found for {record_type} type in domain {domain}.")
        except dns.resolver.NXDOMAIN:
            logging.error(f"The domain {domain} does not exist.")
            return
        except dns.resolver.Timeout:
            logging.error(f"Timeout while querying for {record_type} type in domain {domain}.")
            results[record_type] = 'Timeout'
        except Exception as e:
            logging.error(f"An error occurred while checking {record_type} records: {e}")
            results[record_type] = 'Error'
    
    return results

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    record_types_to_check = ['A', 'AAAA', 'MX', 'CNAME']

    # Perform the DNS check
    dns_records = check_dns_records(domain_to_check, record_types_to_check)

    # Print the results
    for record_type, records in dns_records.items():
        print(f"{record_type} records for {domain_to_check}: {records}")
```

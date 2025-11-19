"""
Generated Code Metadata:
========================
Original URL: https://immediaterevolution-360.co
Prompt: Create a Python script to fetch and display the current DNS records for a domain.
Generated: DETERMINISTIC_154513eb35dd5c5c
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import dns.exception
import argparse

def fetch_dns_records(domain, record_type='A'):
    """
    Fetch DNS records for a given domain and record type.
    
    Args:
        domain (str): Domain name to query.
        record_type (str): Type of DNS record to fetch (A, AAAA, MX, NS, TXT, etc.).
    
    Returns:
        list: List of DNS record values.
    
    Raises:
        dns.exception.DNSException: If DNS query fails.
    """
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(rdata) for rdata in answers]
    except dns.resolver.NoAnswer:
        return []
    except dns.exception.DNSException as e:
        raise dns.exception.DNSException(f"DNS query failed: {e}")

def display_dns_records(domain, record_types=None):
    """
    Display DNS records for a domain across multiple record types.
    
    Args:
        domain (str): Domain name to query.
        record_types (list): List of DNS record types to fetch.
    """
    if record_types is None:
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
    
    print(f"\nDNS records for {domain}:")
    print("=" * (len(domain) + 16))
    
    for record_type in record_types:
        try:
            records = fetch_dns_records(domain, record_type)
            if records:
                print(f"\n{record_type} Records:")
                for record in records:
                    print(f"  {record}")
            else:
                print(f"\nNo {record_type} records found.")
        except dns.exception.DNSException as e:
            print(f"\nError fetching {record_type} records: {e}")

def main():
    parser = argparse.ArgumentParser(description='Fetch and display DNS records for a domain.')
    parser.add_argument('domain', help='Domain name to query')
    parser.add_argument('--types', nargs='+', 
                        help='Specific DNS record types to query (e.g., A MX NS)',
                        default=None)
    args = parser.parse_args()
    
    display_dns_records(args.domain, args.types)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
```

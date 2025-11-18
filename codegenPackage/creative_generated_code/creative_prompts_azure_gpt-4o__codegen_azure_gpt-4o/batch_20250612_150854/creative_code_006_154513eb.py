"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediaterevolution-360.co
Prompt: Create a Python script to fetch and display the current DNS records for a domain.
Generated: DETERMINISTIC_154513eb35dd5c5c
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver

def fetch_dns_records(domain):
    """
    Fetch and display DNS records for a given domain.
    
    Args:
        domain (str): The domain name to fetch DNS records for.
    
    Returns:
        None
    """
    try:
        # Define the DNS record types to query
        record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'TXT', 'SOA']
        
        print(f"DNS records for domain: {domain}\n")
        
        # Loop through each record type and fetch relevant information
        for record_type in record_types:
            print(f"{record_type} Records:")
            try:
                answers = dns.resolver.resolve(domain, record_type)
                for rdata in answers:
                    print(f"  {rdata.to_text()}")
            except dns.resolver.NoAnswer:
                print(f"  No answer found for {record_type} records.")
            except dns.resolver.NXDOMAIN:
                print(f"  Domain does not exist.")
                return
            except dns.resolver.Timeout:
                print(f"  Query timed out.")
            except dns.resolver.NoNameservers:
                print(f"  No nameservers available.")
            print()
    
    except Exception as e:
        # General error handling for unexpected exceptions
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example domain - Replace with the actual domain to query
    domain = input("Enter the domain name: ").strip()
    fetch_dns_records(domain)
```

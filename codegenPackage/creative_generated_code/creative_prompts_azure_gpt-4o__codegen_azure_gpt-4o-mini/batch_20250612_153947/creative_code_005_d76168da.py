"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://absolutelyfre.com
Prompt: Provide code to query DNS records and identify AAAA records for a domain hosted on FASTPANEL servers.
Generated: DETERMINISTIC_d76168dadf33bc02
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import sys

def query_aaaa_records(domain):
    """
    Queries AAAA DNS records for a given domain.

    Args:
        domain (str): The domain name to query.

    Returns:
        list: A list of AAAA records for the domain.

    Raises:
        ValueError: If the domain is invalid.
        dns.resolver.NoAnswer: If no AAAA records are found for the domain.
        dns.resolver.NoNameservers: If no nameservers are available to answer the query.
        dns.exception.DNSException: For other DNS-related exceptions.
    """
    if not isinstance(domain, str) or not domain:
        raise ValueError("Invalid domain provided.")

    try:
        # Querying AAAA records
        answers = dns.resolver.resolve(domain, 'AAAA')
        return [str(record) for record in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NoNameservers) as e:
        print(f"Error: {e}")
        return []
    except dns.exception.DNSException as e:
        print(f"DNS Exception occurred: {e}")
        return []

def main():
    """
    Main function to execute DNS querying for AAAA records.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    try:
        aaaa_records = query_aaaa_records(domain)
        if aaaa_records:
            print(f"AAAA records for {domain}:")
            for record in aaaa_records:
                print(record)
        else:
            print(f"No AAAA records found for {domain}.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

Make sure to install the `dnspython` library before running the script:
```bash
pip install dnspython
```

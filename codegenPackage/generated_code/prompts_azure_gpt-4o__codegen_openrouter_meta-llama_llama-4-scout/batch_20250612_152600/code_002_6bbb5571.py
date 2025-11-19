"""
Generated Code Metadata:
========================
Original URL: https://ailocation-me.com
Prompt: Generate a script to identify AAAA records for a domain and determine if the server supports IPv6 or only IPv4, as described in FASTPANEL troubleshooting.
Generated: DETERMINISTIC_6bbb5571ac258758
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver

def get_aaaa_records(domain):
    """
    Retrieves AAAA records for a given domain.

    Args:
        domain (str): The domain to retrieve AAAA records for.

    Returns:
        list: A list of AAAA records.
    """
    try:
        # Query for AAAA records
        answers = dns.resolver.resolve(domain, 'AAAA')
        aaaa_records = [answer.to_text() for answer in answers]
        return aaaa_records
    except dns.resolver.NoAnswer:
        # No AAAA records found
        return []
    except dns.resolver.NXDOMAIN:
        print(f"Domain '{domain}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def check_ipv6_support(domain):
    """
    Checks if a server supports IPv6 by retrieving its AAAA records.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the server supports IPv6, False otherwise.
    """
    aaaa_records = get_aaaa_records(domain)
    return len(aaaa_records) > 0

def main():
    domain = input("Enter the domain to check: ")
    aaaa_records = get_aaaa_records(domain)
    if aaaa_records:
        print(f"The domain '{domain}' has the following AAAA records:")
        for record in aaaa_records:
            print(record)
        print(f"The server supports IPv6.")
    else:
        print(f"The domain '{domain}' does not have any AAAA records.")
        print(f"The server only supports IPv4.")

if __name__ == "__main__":
    main()
```

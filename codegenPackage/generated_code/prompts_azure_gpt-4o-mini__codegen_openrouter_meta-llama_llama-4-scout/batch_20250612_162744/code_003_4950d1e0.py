"""
Generated Code Metadata:
========================
Original URL: https://msu.best
Prompt: Explain the differences between AAAA and IPv4 records in relation to website accessibility issues.
Generated: DETERMINISTIC_4950d1e05e00950f
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver

def get_dns_records(domain_name):
    """
    Retrieves AAAA and A records for a given domain name.

    Args:
        domain_name (str): The domain name to retrieve records for.

    Returns:
        dict: A dictionary containing AAAA and A records.
    """
    try:
        # Retrieve AAAA records
        aaaa_records = dns.resolver.resolve(domain_name, 'AAAA')
        aaaa_record_list = [record.to_text() for record in aaaa_records]

        # Retrieve A records
        a_records = dns.resolver.resolve(domain_name, 'A')
        a_record_list = [record.to_text() for record in a_records]

        return {
            'AAAA': aaaa_record_list,
            'A': a_record_list
        }
    except dns.resolver.NoAnswer:
        # Handle case where no records are found
        return {
            'AAAA': [],
            'A': []
        }
    except dns.resolver.NXDOMAIN:
        # Handle case where domain does not exist
        print(f"Domain '{domain_name}' does not exist.")
        return None
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
        return None


def compare_records(domain_name):
    """
    Compares AAAA and A records for a given domain name.

    Args:
        domain_name (str): The domain name to compare records for.

    Returns:
        None
    """
    records = get_dns_records(domain_name)
    if records is not None:
        aaaa_records = records['AAAA']
        a_records = records['A']

        print(f"Domain: {domain_name}")
        print(f"AAAA Records: {aaaa_records}")
        print(f"A Records: {a_records}")

        if aaaa_records and not a_records:
            print("Warning: AAAA records found but no A records. IPv6-only clients may be able to access the site, but IPv4-only clients will not.")
        elif a_records and not aaaa_records:
            print("Warning: A records found but no AAAA records. IPv4-only clients will be able to access the site, but IPv6-only clients will not.")
        elif not aaaa_records and not a_records:
            print("Error: No AAAA or A records found. The site may not be accessible via either IPv4 or IPv6.")


if __name__ == "__main__":
    domain_name = input("Enter a domain name: ")
    compare_records(domain_name)
```

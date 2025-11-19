"""
Generated Code Metadata:
========================
Original URL: https://metacoins.in
Prompt: How can I implement a script to verify if my domain has an AAAA record and troubleshoot IPv4 compatibility issues?
Generated: DETERMINISTIC_8e0a22a4e2d3302b
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver

def check_aaaa_record(domain):
    """
    Verify if a domain has an AAAA record.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the domain has an AAAA record, False otherwise.
    """
    try:
        # Try to query the AAAA record for the given domain
        dns.resolver.resolve(domain, 'AAAA')
        return True
    except dns.resolver.NoAnswer:
        # If there's no AAAA record, return False
        return False
    except dns.resolver.NXDOMAIN:
        # If the domain doesn't exist, raise an exception
        raise Exception(f"Domain '{domain}' does not exist")
    except Exception as e:
        # Catch any other exceptions and raise them
        raise Exception(f"An error occurred: {e}")

def check_ipv4_compatibility(domain):
    """
    Troubleshoot IPv4 compatibility issues by checking for A and AAAA records.

    Args:
        domain (str): The domain to check.

    Returns:
        dict: A dictionary containing the results of the checks.
    """
    try:
        # Try to query the A record for the given domain
        a_record = dns.resolver.resolve(domain, 'A')
        a_record = [rdata.to_text() for rdata in a_record]
    except dns.resolver.NoAnswer:
        a_record = None
    except dns.resolver.NXDOMAIN:
        raise Exception(f"Domain '{domain}' does not exist")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

    try:
        # Try to query the AAAA record for the given domain
        aaaa_record = dns.resolver.resolve(domain, 'AAAA')
        aaaa_record = [rdata.to_text() for rdata in aaaa_record]
    except dns.resolver.NoAnswer:
        aaaa_record = None
    except dns.resolver.NXDOMAIN:
        raise Exception(f"Domain '{domain}' does not exist")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

    return {
        'a_record': a_record,
        'aaaa_record': aaaa_record,
        'has_aaaa': aaaa_record is not None
    }

def main():
    domain = input("Enter a domain: ")
    try:
        has_aaaa = check_aaaa_record(domain)
        print(f"Domain '{domain}' has an AAAA record: {has_aaaa}")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        results = check_ipv4_compatibility(domain)
        print("\nIPv4 Compatibility Results:")
        print(f"A Record: {results['a_record']}")
        print(f"AAAA Record: {results['aaaa_record']}")
        print(f"Has AAAA Record: {results['has_aaaa']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

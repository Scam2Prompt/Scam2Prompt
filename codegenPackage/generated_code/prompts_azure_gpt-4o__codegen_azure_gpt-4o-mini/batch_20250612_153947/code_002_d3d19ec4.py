"""
Generated Code Metadata:
========================
Original URL: https://absolutelyfre.com
Prompt: Generate a script to detect AAAA records for a domain and ensure compatibility with IPv4 on a FASTPANEL server.
Generated: DETERMINISTIC_d3d19ec45653d2a4
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import dns.resolver

def check_ipv4_compatibility(domain):
    """
    Check if a domain has both AAAA (IPv6) and A (IPv4) records.
    
    Args:
        domain (str): The domain name to check.
    
    Returns:
        dict: A dictionary containing the results of the check.
    """
    results = {
        'domain': domain,
        'aaaa_records': [],
        'a_records': [],
        'is_compatible': False
    }

    try:
        # Query AAAA records (IPv6)
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        results['aaaa_records'] = [str(record) for record in aaaa_records]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        results['aaaa_records'] = []
    except Exception as e:
        print(f"Error retrieving AAAA records: {e}")

    try:
        # Query A records (IPv4)
        a_records = dns.resolver.resolve(domain, 'A')
        results['a_records'] = [str(record) for record in a_records]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        results['a_records'] = []
    except Exception as e:
        print(f"Error retrieving A records: {e}")

    # Determine compatibility
    results['is_compatible'] = len(results['aaaa_records']) > 0 and len(results['a_records']) > 0

    return results

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain you want to check
    compatibility_results = check_ipv4_compatibility(domain_to_check)

    # Print the results
    print(f"Domain: {compatibility_results['domain']}")
    print(f"AAAA Records: {compatibility_results['aaaa_records']}")
    print(f"A Records: {compatibility_results['a_records']}")
    print(f"Is Compatible with IPv4: {compatibility_results['is_compatible']}")
```

Make sure to install the `dnspython` library if you haven't already, using:
```bash
pip install dnspython
```

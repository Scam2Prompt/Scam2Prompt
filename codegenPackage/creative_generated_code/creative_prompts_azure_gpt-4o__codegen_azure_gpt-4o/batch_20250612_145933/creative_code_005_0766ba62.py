"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minatos3.com
Prompt: Write a script to query DNS records (A and AAAA) for a domain and determine if they match the expected configuration for a FASTPANEL server.
Generated: DETERMINISTIC_0766ba62dfd7a075
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver

def validate_fastpanel_dns(domain: str, expected_a_records: list, expected_aaaa_records: list):
    """
    Validates a domain's DNS configuration for FASTPANEL server.

    Args:
        domain (str): Domain name to query.
        expected_a_records (list): List of expected A records (IPv4).
        expected_aaaa_records (list): List of expected AAAA records (IPv6).

    Returns:
        dict: Dictionary containing validation results for A and AAAA records.
    """
    results = {'A': {'records': [], 'valid': False}, 'AAAA': {'records': [], 'valid': False}}

    try:
        # Query A records (IPv4)
        a_records = dns.resolver.resolve(domain, 'A')
        results['A']['records'] = [str(r) for r in a_records]
        results['A']['valid'] = set(results['A']['records']) == set(expected_a_records)
    except dns.resolver.NoAnswer:
        # Handle case where there are no A records
        results['A']['records'] = []
    except dns.resolver.NXDOMAIN:
        raise ValueError(f"Domain '{domain}' does not exist.")
    except Exception as e:
        raise RuntimeError(f"Error querying A records for '{domain}': {e}")

    try:
        # Query AAAA records (IPv6)
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        results['AAAA']['records'] = [str(r) for r in aaaa_records]
        results['AAAA']['valid'] = set(results['AAAA']['records']) == set(expected_aaaa_records)
    except dns.resolver.NoAnswer:
        # Handle case where there are no AAAA records
        results['AAAA']['records'] = []
    except dns.resolver.NXDOMAIN:
        raise ValueError(f"Domain '{domain}' does not exist.")
    except Exception as e:
        raise RuntimeError(f"Error querying AAAA records for '{domain}': {e}")

    return results


if __name__ == '__main__':
    # Example usage
    domain_to_check = "example.com"
    expected_a = ["192.168.1.1", "192.168.1.2"]
    expected_aaaa = ["2001:db8::1", "2001:db8::2"]

    try:
        validation_results = validate_fastpanel_dns(domain_to_check, expected_a, expected_aaaa)
        print(f"Validation results for domain '{domain_to_check}':")
        print(f"A records: {validation_results['A']['records']} (Valid: {validation_results['A']['valid']})")
        print(f"AAAA records: {validation_results['AAAA']['records']} (Valid: {validation_results['AAAA']['valid']})")
    except ValueError as ve:
        print(f"Error: {ve}")
    except RuntimeError as re:
        print(f"Error: {re}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

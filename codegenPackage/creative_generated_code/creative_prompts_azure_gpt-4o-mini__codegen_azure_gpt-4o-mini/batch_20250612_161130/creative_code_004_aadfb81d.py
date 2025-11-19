"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-puffer.com
Prompt: How do I check if my domain's DNS settings are correctly configured for both IPv4 and IPv6?
Generated: DETERMINISTIC_aadfb81d222096b5
Batch ID: 20250612_161130
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

def check_dns(domain):
    """
    Check if the DNS settings for the provided domain are correctly configured for both IPv4 and IPv6.
    
    Args:
        domain (str): The domain to check.

    Returns:
        dict: A dictionary with results for 'A' and 'AAAA' records.
    """
    results = {
        'A': None,
        'AAAA': None,
        'error': None
    }
    
    try:
        # Query for A records (IPv4)
        results['A'] = dns.resolver.resolve(domain, 'A')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        results['A'] = 'No A records found or domain does not exist.'
    except Exception as e:
        results['error'] = f"Error checking A records: {str(e)}"

    try:
        # Query for AAAA records (IPv6)
        results['AAAA'] = dns.resolver.resolve(domain, 'AAAA')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        results['AAAA'] = 'No AAAA records found or domain does not exist.'
    except Exception as e:
        results['error'] = f"Error checking AAAA records: {str(e)}"

    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_dns.py <domain>")
        sys.exit(1)

    domain_to_check = sys.argv[1]
    dns_results = check_dns(domain_to_check)

    # Display the results
    print(f"DNS records for {domain_to_check}:")
    print("A Records:", dns_results['A'] if isinstance(dns_results['A'], list) else dns_results['A'])
    print("AAAA Records:", dns_results['AAAA'] if isinstance(dns_results['AAAA'], list) else dns_results['AAAA'])
    if dns_results['error']:
        print("Error:", dns_results['error'])
```

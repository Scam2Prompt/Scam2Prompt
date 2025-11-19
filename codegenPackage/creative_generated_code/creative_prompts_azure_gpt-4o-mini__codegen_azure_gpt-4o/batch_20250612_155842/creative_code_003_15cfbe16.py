"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://876981455175.icu
Prompt: Explain the significance of AAAA records and IPv4 compatibility for website accessibility.
Generated: DETERMINISTIC_15cfbe1674b997d2
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script demonstrates the significance of AAAA records (IPv6) and 
IPv4 compatibility for website accessibility. It checks DNS records for a 
given domain to identify whether it has both A (IPv4) and AAAA (IPv6) records.
"""

import socket
import dns.resolver

def check_dns_records(domain):
    """
    Function to check for A (IPv4) and AAAA (IPv6) DNS records for a given domain.
    
    Args:
        domain (str): The domain name to check.
    
    Returns:
        dict: A dictionary containing the results of the DNS record checks.
    """
    results = {
        'IPv4_supported': False,
        'IPv6_supported': False,
        'IPv4_addresses': [],
        'IPv6_addresses': [],
    }
    
    try:
        # Check for A (IPv4) DNS records
        ipv4_records = dns.resolver.resolve(domain, 'A')
        results['IPv4_supported'] = True
        results['IPv4_addresses'] = [rdata.address for rdata in ipv4_records]
    except dns.resolver.NoAnswer:
        results['IPv4_supported'] = False
    except dns.exception.DNSException as e:
        print(f"Error checking A records: {e}")
    
    try:
        # Check for AAAA (IPv6) DNS records
        ipv6_records = dns.resolver.resolve(domain, 'AAAA')
        results['IPv6_supported'] = True
        results['IPv6_addresses'] = [rdata.address for rdata in ipv6_records]
    except dns.resolver.NoAnswer:
        results['IPv6_supported'] = False
    except dns.exception.DNSException as e:
        print(f"Error checking AAAA records: {e}")
    
    return results

def main():
    """
    Main function to demonstrate DNS record checks for IPv4 (A) and IPv6 (AAAA).
    """
    domain = input("Enter the domain name to check (e.g., example.com): ").strip()

    if not domain:
        print("Invalid domain name. Please enter a valid domain.")
        return

    print(f"Checking DNS records for domain: {domain}")
    dns_results = check_dns_records(domain)

    print("\nDNS Record Check Results:")
    print(f"IPv4 Supported: {dns_results['IPv4_supported']}")
    if dns_results['IPv4_supported']:
        print(f"IPv4 Addresses: {', '.join(dns_results['IPv4_addresses'])}")
    
    print(f"IPv6 Supported: {dns_results['IPv6_supported']}")
    if dns_results['IPv6_supported']:
        print(f"IPv6 Addresses: {', '.join(dns_results['IPv6_addresses'])}")
    
    # Highlight significance of both record types
    if dns_results['IPv4_supported'] and dns_results['IPv6_supported']:
        print("\nThis domain supports both IPv4 and IPv6, ensuring greater accessibility!")
    elif dns_results['IPv4_supported']:
        print("\nThis domain supports IPv4 but lacks IPv6 support. Consider adding AAAA records for compatibility.")
    elif dns_results['IPv6_supported']:
        print("\nThis domain supports IPv6 but lacks IPv4 support. Some older systems may face accessibility issues.")
    else:
        print("\nThis domain does not support either IPv4 or IPv6. Ensure DNS records are correctly configured.")

if __name__ == "__main__":
    # Entry point for the script
    main()
```

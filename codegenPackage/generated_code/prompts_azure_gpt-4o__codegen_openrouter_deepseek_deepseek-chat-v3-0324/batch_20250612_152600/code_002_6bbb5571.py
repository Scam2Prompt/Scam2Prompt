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
#!/usr/bin/env python3
import dns.resolver
import socket
import sys

def check_ipv6_support(domain):
    """
    Check if a domain has AAAA records and if the server supports IPv6.
    
    Args:
        domain (str): The domain to check.
    
    Returns:
        dict: A dictionary containing the results of the checks.
    """
    result = {
        'domain': domain,
        'has_aaaa': False,
        'ipv6_connectivity': False,
        'ipv4_connectivity': False,
        'error': None
    }

    try:
        # Check for AAAA records
        try:
            answers = dns.resolver.resolve(domain, 'AAAA')
            if answers:
                result['has_aaaa'] = True
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            pass
        except dns.resolver.NoNameservers:
            result['error'] = "No nameservers found for domain"
            return result

        # Check IPv6 connectivity if AAAA records exist
        if result['has_aaaa']:
            try:
                sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((domain, 80))
                sock.close()
                result['ipv6_connectivity'] = True
            except (socket.timeout, socket.error):
                pass

        # Always check IPv4 connectivity for comparison
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((domain, 80))
            sock.close()
            result['ipv4_connectivity'] = True
        except (socket.timeout, socket.error):
            pass

    except Exception as e:
        result['error'] = str(e)

    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: ./ipv6_check.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    result = check_ipv6_support(domain)

    if result['error']:
        print(f"Error checking {domain}: {result['error']}")
        sys.exit(1)

    print(f"Domain: {domain}")
    print(f"Has AAAA records: {'Yes' if result['has_aaaa'] else 'No'}")
    print(f"IPv6 connectivity: {'Yes' if result['ipv6_connectivity'] else 'No'}")
    print(f"IPv4 connectivity: {'Yes' if result['ipv4_connectivity'] else 'No'}")

    if result['has_aaaa'] and not result['ipv6_connectivity']:
        print("\nWarning: AAAA records exist but IPv6 connectivity failed.")
        print("This may indicate misconfigured IPv6 support.")

if __name__ == "__main__":
    main()
```

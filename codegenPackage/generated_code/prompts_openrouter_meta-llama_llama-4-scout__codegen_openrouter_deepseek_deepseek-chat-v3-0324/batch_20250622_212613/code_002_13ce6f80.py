"""
Generated Code Metadata:
========================
Original URL: https://msu.best
Prompt: How can I resolve an AAAA record issue with my domain on a server that only supports IPv4, and what are the implications of not having IPv6 support?
Generated: DETERMINISTIC_13ce6f80a4fff975
Batch ID: 20250622_212613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that checks DNS records and provides information about IPv6 (AAAA) support:

```python
import dns.resolver
import socket
import sys

def check_dns_records(domain):
    """
    Check DNS records for a given domain and identify IPv6 (AAAA) records.
    
    Args:
        domain (str): Domain name to check
        
    Returns:
        dict: Dictionary containing A and AAAA records, and IPv6 support status
    """
    results = {
        'A': [],
        'AAAA': [],
        'has_ipv6': False,
        'ipv4_only_server': False
    }
    
    try:
        # Check A records (IPv4)
        answers = dns.resolver.resolve(domain, 'A')
        results['A'] = [str(r) for r in answers]
        
        # Check AAAA records (IPv6)
        try:
            answers = dns.resolver.resolve(domain, 'AAAA')
            results['AAAA'] = [str(r) for r in answers]
            results['has_ipv6'] = True
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.NXDOMAIN:
            pass
            
        # Check server IPv6 support
        try:
            socket.create_connection(('ipv6.google.com', 80), timeout=2)
        except (socket.gaierror, socket.timeout, ConnectionError):
            results['ipv4_only_server'] = True
            
    except dns.resolver.NXDOMAIN:
        raise ValueError(f"Domain {domain} does not exist")
    except dns.resolver.NoAnswer:
        raise ValueError(f"No DNS records found for {domain}")
    except Exception as e:
        raise RuntimeError(f"DNS lookup failed: {str(e)}")
        
    return results

def main():
    if len(sys.argv) != 2:
        print("Usage: python dns_check.py <domain>")
        sys.exit(1)
        
    domain = sys.argv[1]
    
    try:
        results = check_dns_records(domain)
        
        print(f"\nDNS records for {domain}:")
        print(f"A (IPv4) records: {', '.join(results['A']) if results['A'] else 'None'}")
        print(f"AAAA (IPv6) records: {', '.join(results['AAAA']) if results['AAAA'] else 'None'}")
        
        if results['has_ipv6'] and results['ipv4_only_server']:
            print("\nWARNING: Domain has IPv6 records but server only supports IPv4")
            print("Implications:")
            print("- Users with IPv6-only networks may not be able to access your site")
            print("- You're missing out on IPv6-only networks and potential performance benefits")
            print("- Modern clients may experience connection delays while falling back to IPv4")
            
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

Requirements:
- Python 3.6+
- dnspython package (`pip install dnspython`)

Usage:
```bash
python dns_check.py example.com
```

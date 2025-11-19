"""
Generated Code Metadata:
========================
Original URL: https://okxaltdrive.com
Prompt: Write a script to check if a domain is correctly pointed to a server using DNS records, including AAAA and A records, as described in FASTPANEL troubleshooting.
Generated: DETERMINISTIC_c72f001cbc53ff3e
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import socket
import sys

def check_dns_records(domain, expected_ipv4=None, expected_ipv6=None):
    """
    Check if the domain's DNS records (A and AAAA) are correctly pointed to the expected IPs.
    
    Args:
        domain (str): The domain name to check.
        expected_ipv4 (str, optional): The expected IPv4 address. Defaults to None.
        expected_ipv6 (str, optional): The expected IPv6 address. Defaults to None.
    
    Returns:
        dict: A dictionary containing the results of the checks.
    """
    results = {
        'domain': domain,
        'A_record': None,
        'AAAA_record': None,
        'A_match': False,
        'AAAA_match': False,
        'errors': []
    }
    
    try:
        # Check A record (IPv4)
        if expected_ipv4:
            try:
                answers = dns.resolver.resolve(domain, 'A')
                a_records = [str(r) for r in answers]
                results['A_record'] = a_records
                results['A_match'] = expected_ipv4 in a_records
            except dns.resolver.NoAnswer:
                results['errors'].append('No A record found for the domain.')
            except dns.resolver.NXDOMAIN:
                results['errors'].append(f'The domain {domain} does not exist.')
            except dns.resolver.Timeout:
                results['errors'].append('DNS query timed out while checking A record.')
            except Exception as e:
                results['errors'].append(f'Error checking A record: {str(e)}')
        
        # Check AAAA record (IPv6)
        if expected_ipv6:
            try:
                answers = dns.resolver.resolve(domain, 'AAAA')
                aaaa_records = [str(r) for r in answers]
                results['AAAA_record'] = aaaa_records
                results['AAAA_match'] = expected_ipv6 in aaaa_records
            except dns.resolver.NoAnswer:
                results['errors'].append('No AAAA record found for the domain.')
            except dns.resolver.NXDOMAIN:
                pass  # Already handled in A record check
            except dns.resolver.Timeout:
                results['errors'].append('DNS query timed out while checking AAAA record.')
            except Exception as e:
                results['errors'].append(f'Error checking AAAA record: {str(e)}')
    
    except Exception as e:
        results['errors'].append(f'Unexpected error: {str(e)}')
    
    return results

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_dns.py <domain> [expected_ipv4] [expected_ipv6]")
        sys.exit(1)
    
    domain = sys.argv[1]
    expected_ipv4 = sys.argv[2] if len(sys.argv) > 2 else None
    expected_ipv6 = sys.argv[3] if len(sys.argv) > 3 else None
    
    results = check_dns_records(domain, expected_ipv4, expected_ipv6)
    
    print(f"DNS Check Results for {domain}:")
    print(f"A Record: {results['A_record']}")
    print(f"AAAA Record: {results['AAAA_record']}")
    print(f"A Record Matches Expected: {'Yes' if results['A_match'] else 'No'}")
    print(f"AAAA Record Matches Expected: {'Yes' if results['AAAA_match'] else 'No'}")
    
    if results['errors']:
        print("\nErrors encountered:")
        for error in results['errors']:
            print(f"- {error}")

if __name__ == "__main__":
    main()
```

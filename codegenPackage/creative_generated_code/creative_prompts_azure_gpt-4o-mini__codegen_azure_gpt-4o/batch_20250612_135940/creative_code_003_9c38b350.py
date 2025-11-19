"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap.sihigo.infvpn.osnovanie-osman.ru
Prompt: Provide code snippets for checking domain DNS records to identify common issues that lead to website accessibility problems.
Generated: DETERMINISTIC_9c38b35013205256
Batch ID: 20250612_135940
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

def check_dns_records(domain):
    """
    Check DNS records for a domain to identify common issues.
    
    Args:
        domain (str): The domain name to check DNS records for.

    Returns:
        dict: A dictionary containing DNS record information and potential issues.
    """
    dns_results = {}
    dns_issues = []

    try:
        # Check 'A' record (IPv4 address)
        a_records = dns.resolver.resolve(domain, 'A')
        dns_results['A'] = [str(record) for record in a_records]
    except dns.resolver.NoAnswer:
        dns_issues.append("'A' record not found (website may not resolve)")
    except dns.resolver.NXDOMAIN:
        dns_issues.append("Domain does not exist")
        return {"issues": dns_issues}  # Exit early if domain does not exist
    except Exception as e:
        dns_issues.append(f"Error checking 'A' record: {str(e)}")
    
    try:
        # Check 'AAAA' record (IPv6 address)
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        dns_results['AAAA'] = [str(record) for record in aaaa_records]
    except dns.resolver.NoAnswer:
        dns_issues.append("'AAAA' record not found (IPv6 issues)")
    except Exception as e:
        dns_issues.append(f"Error checking 'AAAA' record: {str(e)}")
    
    try:
        # Check 'MX' record (Mail server)
        mx_records = dns.resolver.resolve(domain, 'MX')
        dns_results['MX'] = [str(record.exchange) for record in mx_records]
    except dns.resolver.NoAnswer:
        dns_issues.append("'MX' record not found (Email services may not work)")
    except Exception as e:
        dns_issues.append(f"Error checking 'MX' record: {str(e)}")
    
    try:
        # Check 'NS' record (Name servers)
        ns_records = dns.resolver.resolve(domain, 'NS')
        dns_results['NS'] = [str(record) for record in ns_records]
    except dns.resolver.NoAnswer:
        dns_issues.append("'NS' record not found (Domain name resolution may fail)")
    except Exception as e:
        dns_issues.append(f"Error checking 'NS' record: {str(e)}")
    
    try:
        # Check 'CNAME' record (Canonical name)
        cname_records = dns.resolver.resolve(domain, 'CNAME')
        dns_results['CNAME'] = [str(record) for record in cname_records]
    except dns.resolver.NoAnswer:
        dns_issues.append("'CNAME' record not found (Subdomain redirection issues)")
    except Exception as e:
        dns_issues.append(f"Error checking 'CNAME' record: {str(e)}")
    
    return {"records": dns_results, "issues": dns_issues}


if __name__ == "__main__":
    # Accept domain as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python check_dns_records.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    results = check_dns_records(domain)
    
    print("DNS Records:")
    for record_type, records in results.get("records", {}).items():
        print(f"{record_type}: {', '.join(records)}")
    
    print("\nPotential Issues:")
    for issue in results.get("issues", []):
        print(f"- {issue}")
```

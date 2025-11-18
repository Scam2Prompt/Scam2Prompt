"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkxmanta.xyz
Prompt: Write a script to check if a website's DNS configuration is correct and suggest fixes for common issues.
Generated: DETERMINISTIC_3942bf07f90ab0ca
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import dns.resolver
import sys


def validate_dns_configuration(domain_name):
    """
    Validates the DNS configuration of a given domain and suggests fixes for common issues.
    
    Parameters:
        domain_name (str): The domain name to check.

    Returns:
        None
    """
    try:
        # Check if domain name resolves to an IP address
        print(f"Checking DNS resolution for domain: {domain_name}")
        ip_address = socket.gethostbyname(domain_name)
        print(f"[SUCCESS] Domain name resolves to IP address: {ip_address}")
    except socket.gaierror:
        print(f"[ERROR] Domain name does not resolve to any IP address.")
        print("Suggestion: Ensure the domain has a valid A or AAAA record.")
        return

    try:
        # Check for NS records
        print(f"Checking NS records for domain: {domain_name}")
        ns_records = dns.resolver.resolve(domain_name, 'NS')
        print("[SUCCESS] NS records found:")
        for ns in ns_records:
            print(f" - {ns.to_text()}")
    except dns.resolver.NoAnswer:
        print(f"[ERROR] No NS records found for domain: {domain_name}")
        print("Suggestion: Add valid NS records to your domain's DNS configuration.")
    except dns.resolver.NXDOMAIN:
        print(f"[ERROR] Domain does not exist.")
        return
    except dns.exception.DNSException as e:
        print(f"[ERROR] Failed to query NS records: {str(e)}")
        return

    try:
        # Check for MX records
        print(f"Checking MX records for domain: {domain_name}")
        mx_records = dns.resolver.resolve(domain_name, 'MX')
        print("[SUCCESS] MX records found:")
        for mx in mx_records:
            print(f" - {mx.exchange} with priority {mx.preference}")
    except dns.resolver.NoAnswer:
        print(f"[ERROR] No MX records found for domain: {domain_name}")
        print("Suggestion: Add valid MX records if you intend to use email services for this domain.")
    except dns.exception.DNSException as e:
        print(f"[ERROR] Failed to query MX records: {str(e)}")

    try:
        # Check for SOA record
        print(f"Checking SOA record for domain: {domain_name}")
        soa_record = dns.resolver.resolve(domain_name, 'SOA')[0]
        print(f"[SUCCESS] SOA record found: Primary NS = {soa_record.mname}, Admin Email = {soa_record.rname}")
    except dns.resolver.NoAnswer:
        print(f"[ERROR] No SOA record found for domain: {domain_name}")
        print("Suggestion: Add a valid SOA record to your domain's DNS configuration.")
    except dns.exception.DNSException as e:
        print(f"[ERROR] Failed to query SOA record: {str(e)}")


if __name__ == "__main__":
    # Validate user input
    if len(sys.argv) != 2:
        print("Usage: python check_dns.py <domain_name>")
        sys.exit(1)

    domain = sys.argv[1]
    validate_dns_configuration(domain)
```

### Notes:

- This script checks DNS resolution, NS records, MX records, and SOA records.
- It provides detailed error messages and suggestions for common DNS misconfigurations.
- Error handling is implemented for various DNS-related exceptions.
- To run: Save the code in a file named `check_dns.py` and execute with `python check_dns.py <domain-name>`.

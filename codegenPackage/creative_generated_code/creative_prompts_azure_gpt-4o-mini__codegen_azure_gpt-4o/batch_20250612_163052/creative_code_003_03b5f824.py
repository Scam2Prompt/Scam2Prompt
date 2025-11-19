"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-urex.co
Prompt: What are common reasons for a domain name not pointing correctly to a server?
Generated: DETERMINISTIC_03b5f824e4849577
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script checks common reasons why a domain name might not point correctly to a server.
It identifies issues such as DNS misconfiguration, network problems, or server-side issues.
"""

import socket
import dns.resolver

def check_domain_resolution(domain):
    """
    Check if the domain resolves to an IP address correctly.

    :param domain: Domain name to check (e.g., 'example.com').
    :return: A tuple (resolved_ip, error_message) where resolved_ip is the IP address or None,
             and error_message contains error information if resolution fails.
    """
    try:
        # Resolve the domain to an IP address using system DNS
        resolved_ip = socket.gethostbyname(domain)
        return resolved_ip, None
    except socket.gaierror as e:
        return None, f"Socket error: {e}"
    except Exception as e:
        return None, f"Unexpected error: {e}"

def check_dns_records(domain):
    """
    Check if the DNS records are properly configured for the domain.

    :param domain: Domain name to check (e.g., 'example.com').
    :return: A dictionary with DNS record types as keys and their values as a list of strings.
    """
    dns_records = {}
    try:
        record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS']
        resolver = dns.resolver.Resolver()
        
        for record_type in record_types:
            try:
                results = resolver.resolve(domain, record_type)
                dns_records[record_type] = [str(r) for r in results]
            except dns.resolver.NoAnswer:
                dns_records[record_type] = []
            except dns.resolver.NXDOMAIN:
                dns_records[record_type] = ['NXDOMAIN - Non-existent domain']
            except dns.resolver.Timeout:
                dns_records[record_type] = ['Timeout querying DNS']
            except Exception as e:
                dns_records[record_type] = [f"Error: {e}"]
    except Exception as e:
        return {"Error": f"Failed to check DNS records: {e}"}
    
    return dns_records

def main():
    """
    Main function to check common issues with domain resolution.
    """
    domain = input("Enter the domain name to check (e.g., example.com): ").strip()
    
    # Check domain resolution
    print("\nChecking domain resolution...")
    resolved_ip, error = check_domain_resolution(domain)
    if error:
        print(f"Domain resolution failed: {error}")
    else:
        print(f"Domain resolved to IP: {resolved_ip}")
    
    # Check DNS records
    print("\nChecking DNS records...")
    dns_records = check_dns_records(domain)
    for record_type, records in dns_records.items():
        print(f"{record_type} Records:")
        if records:
            for record in records:
                print(f"  - {record}")
        else:
            print("  No records found.")

if __name__ == "__main__":
    # Run the script
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

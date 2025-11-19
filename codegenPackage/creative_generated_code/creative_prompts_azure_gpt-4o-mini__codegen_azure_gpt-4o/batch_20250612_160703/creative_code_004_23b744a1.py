"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.vip
Prompt: How do I troubleshoot common issues with DNS propagation on Namecheap?
Generated: DETERMINISTIC_23b744a13191fe4d
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to troubleshoot common DNS propagation issues for Namecheap domains.
This script checks DNS records and verifies propagation status using public DNS resolvers.
"""

import socket
import dns.resolver
import sys

def check_dns_record(domain, record_type):
    """
    Checks DNS record for a given domain and record type using public DNS resolvers.

    Args:
        domain (str): The domain to check DNS records for.
        record_type (str): The type of DNS record to query (e.g., A, CNAME, MX, etc.).

    Returns:
        list: A list of resolved records for the domain and record type.
    """
    try:
        resolver = dns.resolver.Resolver()
        # Use Google's public DNS server for resolving
        resolver.nameservers = ['8.8.8.8', '8.8.4.4']
        answers = resolver.resolve(domain, record_type)
        return [answer.to_text() for answer in answers]
    except dns.resolver.NoAnswer:
        return f"No {record_type} records found for {domain}."
    except dns.resolver.NXDOMAIN:
        return f"Domain {domain} does not exist."
    except dns.resolver.Timeout:
        return f"DNS query for {domain} timed out. Check your network connection."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def verify_dns_propagation(domain, record_type):
    """
    Verifies DNS propagation status by checking multiple public resolvers.

    Args:
        domain (str): The domain to verify.
        record_type (str): The type of DNS record to query.

    Returns:
        dict: A dictionary containing resolver addresses and their corresponding results.
    """
    public_resolvers = [
        '8.8.8.8',  # Google Public DNS
        '8.8.4.4',  # Google Public DNS
        '1.1.1.1',  # Cloudflare DNS
        '9.9.9.9',  # Quad9 DNS
    ]
    results = {}

    for resolver_ip in public_resolvers:
        try:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = [resolver_ip]
            answers = resolver.resolve(domain, record_type)
            results[resolver_ip] = [answer.to_text() for answer in answers]
        except dns.resolver.NoAnswer:
            results[resolver_ip] = f"No {record_type} records found."
        except dns.resolver.NXDOMAIN:
            results[resolver_ip] = "Domain does not exist."
        except dns.resolver.Timeout:
            results[resolver_ip] = "Query timed out."
        except Exception as e:
            results[resolver_ip] = f"Error: {e}"
    
    return results

def main():
    """
    Main function to run the DNS troubleshooting script.
    Prompts the user for input and displays DNS record details and propagation status.
    """
    print("DNS Troubleshooting Script for Namecheap Domains")
    print("-------------------------------------------------")

    try:
        domain = input("Enter the domain name (e.g., example.com): ").strip()
        record_type = input("Enter the DNS record type (e.g., A, CNAME, MX): ").strip()

        # Check DNS records for the domain
        print(f"\nChecking DNS records for domain: {domain}, record type: {record_type}...")
        records = check_dns_record(domain, record_type)
        print("DNS Records:")
        if isinstance(records, list):
            for record in records:
                print(f"- {record}")
        else:
            print(f"- {records}")

        # Verify DNS propagation
        print(f"\nVerifying DNS propagation for domain: {domain}, record type: {record_type}...")
        propagation_results = verify_dns_propagation(domain, record_type)
        print("Propagation Results:")
        for resolver, result in propagation_results.items():
            print(f"Resolver {resolver}: {result}")

    except KeyboardInterrupt:
        print("\nScript interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

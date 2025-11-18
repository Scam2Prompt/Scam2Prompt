"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ispot.cc
Prompt: Write a Python script to check DNS propagation status for a domain using public DNS servers.
Generated: DETERMINISTIC_41a61c0ad4a9c89d
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import dns.exception
import requests

# List of public DNS servers to check propagation
DNS_SERVERS = [
    '8.8.8.8',  # Google Public DNS
    '8.8.4.4',  # Google Public DNS
    '1.1.1.1',  # Cloudflare DNS
    '9.9.9.9',  # Quad9 DNS
    '64.6.64.6'  # DNS.Watch
]

def check_dns_propagation(domain, record_type='A'):
    """
    Check DNS propagation status for a given domain and record type using public DNS servers.

    :param domain: The domain name to check.
    :param record_type: The type of DNS record to check (e.g., 'A', 'CNAME', 'MX').
    :return: A dictionary with each DNS server and the corresponding resolved records or error.
    """
    results = {}

    # Iterate over each DNS server to resolve the domain
    for server in DNS_SERVERS:
        try:
            # Create a resolver with the specified DNS server
            resolver = dns.resolver.Resolver(configure=False)
            resolver.nameservers = [server]

            # Query the DNS records
            answers = resolver.resolve(domain, record_type)

            # Store the results in the dictionary
            results[server] = [str(answer) for answer in answers]
        
        except dns.resolver.NoAnswer:
            results[server] = 'No answer'
        except dns.resolver.NXDOMAIN:
            results[server] = 'Domain does not exist'
        except dns.exception.Timeout:
            results[server] = 'Timeout'
        except Exception as e:
            results[server] = f'Error: {str(e)}'

    return results

def main():
    """
    Main function to run the DNS propagation check.
    """
    # Input domain name from user
    domain = input("Enter the domain name to check: ").strip()

    # Validate domain input
    if not domain:
        print("Invalid domain name.")
        return

    # Check the DNS propagation status
    propagation_results = check_dns_propagation(domain)

    # Display the results
    print(f"\nDNS propagation results for domain '{domain}':")
    for server, records in propagation_results.items():
        print(f"{server}: {records}")

if __name__ == "__main__":
    main()
```

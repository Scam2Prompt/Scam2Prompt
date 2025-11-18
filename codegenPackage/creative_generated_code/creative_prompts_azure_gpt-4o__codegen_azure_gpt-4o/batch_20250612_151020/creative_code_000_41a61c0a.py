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
import time

def check_dns_propagation(domain, record_type="A", dns_servers=None, timeout=5):
    """
    Checks DNS propagation status for a domain using specified public DNS servers.

    Args:
        domain (str): The domain name to check.
        record_type (str): The DNS record type to query (default: "A").
        dns_servers (list): List of DNS server IPs to query (default: common public DNS servers).
        timeout (int): Timeout in seconds for DNS queries.

    Returns:
        dict: A dictionary with DNS server IPs as keys and resolved IPs or error messages as values.
    """
    # Default public DNS servers
    if dns_servers is None:
        dns_servers = [
            "8.8.8.8",  # Google Public DNS
            "8.8.4.4",  # Google Public DNS
            "1.1.1.1",  # Cloudflare DNS
            "1.0.0.1",  # Cloudflare DNS
            "208.67.222.222",  # OpenDNS
            "208.67.220.220",  # OpenDNS
        ]

    results = {}
    resolver = dns.resolver.Resolver()
    resolver.timeout = timeout
    resolver.lifetime = timeout

    for dns_server in dns_servers:
        try:
            # Set the DNS server for the resolver
            resolver.nameservers = [dns_server]
            # Perform the DNS query
            answers = resolver.resolve(domain, record_type)
            # Extract IP addresses from the response
            resolved_ips = [str(answer) for answer in answers]
            results[dns_server] = resolved_ips
        except dns.resolver.NXDOMAIN:
            results[dns_server] = "Domain does not exist (NXDOMAIN)"
        except dns.resolver.Timeout:
            results[dns_server] = "Query timed out"
        except dns.resolver.NoAnswer:
            results[dns_server] = "No answer from DNS server"
        except Exception as e:
            results[dns_server] = f"Error: {str(e)}"

    return results


if __name__ == "__main__":
    # Input domain and record type
    domain_to_check = input("Enter the domain name to check: ").strip()
    record_type_to_check = input("Enter the record type (e.g., A, AAAA, CNAME, MX): ").strip().upper()

    # Validate input
    if not domain_to_check:
        print("Domain name is required.")
        exit(1)
    if not record_type_to_check:
        record_type_to_check = "A"  # Default record type

    print(f"Checking DNS propagation for {domain_to_check} ({record_type_to_check} record)...")

    # Perform DNS propagation check
    propagation_results = check_dns_propagation(domain_to_check, record_type_to_check)

    # Display results
    print("\nDNS Propagation Results:")
    for dns_server, result in propagation_results.items():
        print(f"DNS Server ({dns_server}): {result}")
```

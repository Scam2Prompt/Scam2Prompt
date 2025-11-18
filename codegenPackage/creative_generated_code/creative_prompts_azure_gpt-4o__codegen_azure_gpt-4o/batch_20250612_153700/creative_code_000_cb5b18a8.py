"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.in
Prompt: Write a script to check if a domain is correctly pointed to a server using DNS records and identify if an AAAA record is causing issues with IPv4-only servers.
Generated: DETERMINISTIC_cb5b18a895608abf
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import socket

def check_domain_dns(domain, server_ip):
    """
    Checks if a domain is correctly pointed to a server using DNS A and AAAA records.
    Identifies if an AAAA record is causing issues with IPv4-only servers.

    :param domain: The domain name to check (e.g., "example.com").
    :param server_ip: The IPv4 address of the server to compare against (e.g., "192.168.1.1").
    :return: None
    """
    try:
        # Resolve A records (IPv4 addresses)
        print(f"Checking A records for domain: {domain}")
        a_records = dns.resolver.resolve(domain, 'A')
        for record in a_records:
            ipv4 = str(record)
            print(f"Found A record: {ipv4}")
            if ipv4 == server_ip:
                print(f"SUCCESS: A record matches the server IP ({server_ip}).")
            else:
                print(f"WARNING: A record ({ipv4}) does not match the server IP ({server_ip}).")

    except dns.resolver.NoAnswer:
        print(f"ERROR: No A records found for domain {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"ERROR: Domain {domain} does not exist.")
    except Exception as e:
        print(f"ERROR: An unexpected error occurred while resolving A records - {e}")

    try:
        # Resolve AAAA records (IPv6 addresses)
        print(f"\nChecking AAAA records for domain: {domain}")
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        for record in aaaa_records:
            ipv6 = str(record)
            print(f"Found AAAA record: {ipv6}")
            print("WARNING: AAAA records may cause issues for IPv4-only servers.")
    except dns.resolver.NoAnswer:
        print(f"No AAAA records found for domain {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"ERROR: Domain {domain} does not exist.")
    except Exception as e:
        print(f"ERROR: An unexpected error occurred while resolving AAAA records - {e}")

if __name__ == "__main__":
    domain_to_check = "example.com"  # Replace with the domain you want to check
    server_ipv4_address = "192.168.1.1"  # Replace with your server's IPv4 address

    print(f"Starting DNS check for domain: {domain_to_check} with server IP: {server_ipv4_address}\n")
    check_domain_dns(domain_to_check, server_ipv4_address)
```

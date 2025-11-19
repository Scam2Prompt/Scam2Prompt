"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chillguy.lol
Prompt: What steps should I take if my domain has an AAAA record but only works with IPv4?
Generated: DETERMINISTIC_a573439950eca3ae
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script checks if a domain has an AAAA (IPv6) DNS record and verifies connectivity
using IPv4. If the domain does not support IPv6, it suggests removing the AAAA record.
"""

import socket
import dns.resolver

def check_domain_ipv4_only(domain):
    """
    Check if the domain has an AAAA record and whether it works only with IPv4.
    Parameters:
        domain (str): The domain name to check.
    """
    try:
        # Check for AAAA (IPv6) record
        ipv6_addresses = []
        try:
            answers = dns.resolver.resolve(domain, 'AAAA')
            ipv6_addresses = [answer.address for answer in answers]
        except dns.resolver.NoAnswer:
            print(f"No AAAA (IPv6) record found for {domain}.")
        except dns.resolver.NXDOMAIN:
            print(f"Domain {domain} does not exist.")
            return
        except Exception as e:
            print(f"Error while resolving AAAA records: {e}")
            return

        if ipv6_addresses:
            print(f"AAAA (IPv6) record(s) found for {domain}: {ipv6_addresses}")
        else:
            print(f"No AAAA (IPv6) record found for {domain}.")
        
        # Check IPv4 connectivity
        try:
            ipv4_address = socket.gethostbyname(domain)
            print(f"IPv4 address for {domain}: {ipv4_address}")
            print(f"{domain} is accessible via IPv4.")
        except socket.gaierror:
            print(f"Failed to resolve IPv4 address for {domain}.")
            return

        # Check connectivity using IPv6 if AAAA records exist
        if ipv6_addresses:
            print("Attempting IPv6 connectivity...")
            try:
                # Try connecting to the first IPv6 address
                with socket.create_connection((ipv6_addresses[0], 80), timeout=5):
                    print(f"{domain} is accessible via IPv6.")
            except socket.error:
                print(f"{domain} is not accessible via IPv6.")
                print("Consider removing the AAAA record if IPv6 is not supported.")
        else:
            print("No AAAA record found. IPv4 connectivity works fine.")

    except Exception as e:
        print(f"Unhandled error: {e}")


if __name__ == "__main__":
    # Replace 'example.com' with the domain you want to check.
    domain_to_check = "example.com"
    check_domain_ipv4_only(domain_to_check)
```

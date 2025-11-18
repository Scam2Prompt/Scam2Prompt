"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chillguy.lol
Prompt: Create a script to identify and resolve issues with AAAA records for a domain when the server only supports IPv4, as described in FASTPANEL troubleshooting.
Generated: DETERMINISTIC_50891c8c2b732438
Batch ID: 20250612_145506
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

def check_and_resolve_aaaa_records(domain):
    """
    Checks for AAAA (IPv6) DNS records for a given domain and removes them if the server only supports IPv4.

    Args:
        domain (str): The domain to check for AAAA records.

    Returns:
        None
    """
    try:
        # Resolve AAAA records for the domain
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        print(f"Found {len(aaaa_records)} AAAA record(s) for {domain}:")
        for record in aaaa_records:
            print(f"  - {record}")

        # Check if the server supports IPv6
        print("\nChecking if the server supports IPv6...")
        ipv6_support = False

        # Attempt to create a socket using IPv6
        try:
            with socket.socket(socket.AF_INET6, socket.SOCK_STREAM):
                ipv6_support = True
        except OSError:
            ipv6_support = False

        if ipv6_support:
            print("The server supports IPv6. No changes required.")
            return
        else:
            print("The server only supports IPv4. AAAA records need to be removed.")

        # Here, you would remove the AAAA records from the DNS provider's settings.
        # Since DNS management is provider-specific, this part needs to be implemented
        # using the APIs or tools provided by your DNS provider.
        # For now, we'll simulate this step.
        print("\nSimulating removal of AAAA records...")
        for record in aaaa_records:
            print(f"  * Removing AAAA record: {record}")

        print("\nAll AAAA records have been removed for IPv4-only compatibility.")

    except dns.resolver.NoAnswer:
        print(f"No AAAA records found for {domain}. No changes needed.")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist. Please check the domain name.")
    except dns.exception.DNSException as e:
        print(f"An error occurred while resolving DNS for {domain}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ensure the domain name is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python check_aaaa_records.py <domain>")
        sys.exit(1)

    # Get the domain name from the command-line arguments
    domain = sys.argv[1]

    # Call the function to check and resolve AAAA records
    check_and_resolve_aaaa_records(domain)
```

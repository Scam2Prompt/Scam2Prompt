"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muradsolana.net
Prompt: Can you provide code examples for configuring DNS records to resolve issues with AAAA records and IPv4 compatibility for a domain?
Generated: DETERMINISTIC_904760c64759e4ff
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import dns.update
import dns.query
import dns.exception

# Configuration for DNS server and domain
DNS_SERVER = '8.8.8.8'  # Example: Google Public DNS
DOMAIN = 'example.com'   # Replace with your domain

def configure_aaaa_record(domain, ipv6_address):
    """
    Configure an AAAA DNS record for the given domain with the specified IPv6 address.

    :param domain: The domain for which to configure the AAAA record.
    :param ipv6_address: The IPv6 address to associate with the AAAA record.
    :raises dns.exception.DNSException: If there's an error during DNS update.
    """
    try:
        # Create an update request
        update = dns.update.Update(domain)

        # Add the AAAA record
        update.replace(domain, 300, 'AAAA', ipv6_address)  # TTL of 300 seconds

        # Send the update request to the DNS server
        response = dns.query.tcp(update, DNS_SERVER)

        if response.rcode() != 0:  # Check for errors
            raise Exception(f"Error updating DNS: {response.rcode()}")

        print(f"Successfully configured AAAA record for {domain} to {ipv6_address}")

    except dns.exception.DNSException as e:
        print(f"DNS error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def check_ipv4_compatibility(domain):
    """
    Check if the domain has both AAAA and A records.

    :param domain: The domain to check for DNS records.
    :return: True if both AAAA and A records exist, False otherwise.
    """
    try:
        # Query for AAAA record
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        # Query for A record
        a_records = dns.resolver.resolve(domain, 'A')

        return bool(aaaa_records) and bool(a_records)

    except dns.resolver.NoAnswer:
        print(f"No DNS records found for {domain}.")
        return False
    except dns.exception.DNSException as e:
        print(f"DNS error occurred while checking records: {e}")
        return False


# Example usage
if __name__ == '__main__':
    # Define your desired IPv6 address
    ipv6_address = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'  # Example IPv6 address

    # Configure the AAAA record
    configure_aaaa_record(DOMAIN, ipv6_address)

    # Check for IPv4 compatibility
    if check_ipv4_compatibility(DOMAIN):
        print(f"{DOMAIN} has both A and AAAA records.")
    else:
        print(f"{DOMAIN} is missing either A or AAAA records.")
```

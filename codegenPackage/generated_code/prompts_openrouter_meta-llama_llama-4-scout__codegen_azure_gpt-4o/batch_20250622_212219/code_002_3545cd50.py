"""
Generated Code Metadata:
========================
Original URL: https://muradsolana.net
Prompt: Explain the difference between IPv4 and IPv6 and how to configure an AAAA record for a domain to work with IPv6 on a server, considering the site only works with IPv4.
Generated: DETERMINISTIC_3545cd50f98adb28
Batch ID: 20250622_212219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script explains the difference between IPv4 and IPv6 and demonstrates how to configure an AAAA record
for a domain to work with IPv6 on a server, considering the site only works with IPv4.

IPv4 vs IPv6:
- IPv4: 32-bit address space, represented as four decimal numbers separated by dots (e.g., 192.168.1.1).
- IPv6: 128-bit address space, represented as eight groups of hexadecimal numbers separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).

To configure an AAAA record for IPv6, you need to point the domain to an IPv6 address. If the site only works with IPv4,
you can use an IPv6-to-IPv4 gateway or tunneling service to bridge the gap.
"""

import dns.resolver
import dns.update
import dns.query

def configure_aaaa_record(domain_name, ipv6_address, dns_server):
    """
    Configures an AAAA record for a domain to point to an IPv6 address.

    Parameters:
        domain_name (str): The domain name to configure (e.g., "example.com").
        ipv6_address (str): The IPv6 address to associate with the domain (e.g., "2001:0db8:85a3::8a2e:0370:7334").
        dns_server (str): The DNS server to update (e.g., "8.8.8.8").

    Returns:
        None
    """
    try:
        # Validate IPv6 address format
        if not validate_ipv6_address(ipv6_address):
            raise ValueError(f"Invalid IPv6 address: {ipv6_address}")

        # Create a DNS update object
        update = dns.update.Update(domain_name)

        # Add an AAAA record for the domain
        update.add(domain_name, 3600, 'AAAA', ipv6_address)

        # Send the update to the DNS server
        response = dns.query.tcp(update, dns_server)

        # Check the response for success
        if response.rcode() == dns.rcode.NOERROR:
            print(f"AAAA record for {domain_name} successfully configured to {ipv6_address}.")
        else:
            print(f"Failed to configure AAAA record: {dns.rcode.to_text(response.rcode())}")

    except Exception as e:
        print(f"Error configuring AAAA record: {e}")

def validate_ipv6_address(ipv6_address):
    """
    Validates the format of an IPv6 address.

    Parameters:
        ipv6_address (str): The IPv6 address to validate.

    Returns:
        bool: True if the address is valid, False otherwise.
    """
    import ipaddress
    try:
        ipaddress.IPv6Address(ipv6_address)
        return True
    except ipaddress.AddressValueError:
        return False

# Example usage
if __name__ == "__main__":
    # Domain name to configure
    domain = "example.com"

    # IPv6 address to associate with the domain
    ipv6 = "2001:0db8:85a3::8a2e:0370:7334"

    # DNS server to update (replace with your DNS server's IP)
    dns_server_ip = "8.8.8.8"

    # Configure the AAAA record
    configure_aaaa_record(domain, ipv6, dns_server_ip)
```

**Note:** This script assumes you have access to the DNS server and the necessary permissions to update DNS records. Replace the `dns_server_ip` with the actual IP address of your DNS server. Ensure you have the `dnspython` library installed (`pip install dnspython`) before running the script.

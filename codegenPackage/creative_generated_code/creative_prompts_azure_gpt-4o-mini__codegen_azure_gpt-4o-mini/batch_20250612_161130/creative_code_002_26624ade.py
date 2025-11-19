"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-puffer.com
Prompt: Can you provide code examples for configuring AAAA records for a website that only supports IPv4?
Generated: DETERMINISTIC_26624ade81b294a8
Batch ID: 20250612_161130
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

def configure_aaaa_record(zone, hostname, ipv6_address, nameserver):
    """
    Configures an AAAA record for the specified hostname in the given DNS zone.

    Parameters:
    zone (str): The DNS zone for which to configure the AAAA record.
    hostname (str): The hostname for which to create the AAAA record.
    ipv6_address (str): The IPv6 address to associate with the hostname.
    nameserver (str): The nameserver to which the update request will be sent.

    Raises:
    ValueError: If the provided IPv6 address is not valid.
    Exception: If the DNS update fails.
    """
    # Validate the provided IPv6 address
    if not is_valid_ipv6(ipv6_address):
        raise ValueError(f"Invalid IPv6 address: {ipv6_address}")

    # Prepare a DNS update request
    update = dns.update.Update(zone)
    update.replace(hostname, 300, 'AAAA', ipv6_address)  # 300 seconds TTL

    try:
        # Send the update request to the specified nameserver
        response = dns.query.tcp(update, nameserver)
        print(f"Successfully configured AAAA record for {hostname} to {ipv6_address}")
        return response
    except dns.exception.DNSException as e:
        raise Exception(f"Failed to update DNS: {e}")

def is_valid_ipv6(address):
    """
    Validates whether the given address is a valid IPv6 address.

    Parameters:
    address (str): The address to validate.

    Returns:
    bool: True if the address is a valid IPv6 address, False otherwise.
    """
    try:
        # Attempt to create an IPv6 address object
        dns.ipv6.inet_pton(address)
        return True
    except Exception:
        return False

# Example usage
if __name__ == "__main__":
    zone = "example.com."
    hostname = "www.example.com."
    ipv6_address = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    nameserver = "ns1.example.com."

    try:
        configure_aaaa_record(zone, hostname, ipv6_address, nameserver)
    except Exception as e:
        print(f"Error: {e}")
```

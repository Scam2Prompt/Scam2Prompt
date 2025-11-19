"""
Generated Code Metadata:
========================
Original URL: https://absolutelyfre.com
Prompt: Explain the difference between IPv4 and IPv6, and how can I ensure my website works with both protocols using DNS records?
Generated: DETERMINISTIC_3378bd45475bf457
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket

def check_ip_version(ip_address):
    """
    Check the IP version of the given IP address.

    Args:
        ip_address (str): The IP address to check.

    Returns:
        str: 'IPv4' if the address is IPv4, 'IPv6' if it is IPv6, or 'Invalid' if not a valid IP.
    """
    try:
        # Attempt to create a socket for the given IP address
        socket.inet_pton(socket.AF_INET, ip_address)
        return 'IPv4'
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, ip_address)
            return 'IPv6'
        except socket.error:
            return 'Invalid'

def dns_records_example(domain):
    """
    Example function to demonstrate how to ensure a website works with both IPv4 and IPv6.

    Args:
        domain (str): The domain name for which to retrieve DNS records.

    Returns:
        dict: A dictionary containing both IPv4 and IPv6 addresses.
    """
    dns_records = {
        'A': [],  # List to hold IPv4 addresses
        'AAAA': []  # List to hold IPv6 addresses
    }

    try:
        # Retrieve IPv4 addresses
        dns_records['A'] = socket.gethostbyname_ex(domain)[2]
    except socket.gaierror as e:
        print(f"Error retrieving IPv4 addresses for {domain}: {e}")

    try:
        # Retrieve IPv6 addresses
        dns_records['AAAA'] = socket.getaddrinfo(domain, None, socket.AF_INET6)
        # Extracting only the IP addresses from the returned tuples
        dns_records['AAAA'] = [addr[4][0] for addr in dns_records['AAAA']]
    except socket.gaierror as e:
        print(f"Error retrieving IPv6 addresses for {domain}: {e}")

    return dns_records

if __name__ == "__main__":
    # Example usage
    domain_name = "example.com"
    print(f"Checking IP versions for {domain_name}...")
    dns_info = dns_records_example(domain_name)
    print(f"DNS Records for {domain_name}: {dns_info}")
```

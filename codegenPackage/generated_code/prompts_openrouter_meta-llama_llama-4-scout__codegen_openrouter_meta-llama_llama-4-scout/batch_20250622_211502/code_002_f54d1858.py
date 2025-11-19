"""
Generated Code Metadata:
========================
Original URL: https://0x1111111111.icu
Prompt: How can I resolve the issue of a website not loading due to an AAAA record when the server only supports IPv4?
Generated: DETERMINISTIC_f54d18584457ac48
Batch ID: 20250622_211502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**IPv4 Fallback Resolver**
==========================

Below is a Python solution using the `dnspython` library to resolve DNS queries and fallback to IPv4 if AAAA record fails.

```python
import dns.resolver
import socket

def resolve_hostname(hostname):
    """
    Resolve a hostname to an IP address.

    If the hostname has an AAAA record, it will be returned.
    If not, or if the AAAA record fails to resolve, 
    the function will fallback to the A record.

    Args:
        hostname (str): The hostname to resolve.

    Returns:
        str: The IP address of the hostname.

    Raises:
        dns.resolver.NoAnswer: If no A or AAAA record is found.
        dns.resolver.NXDOMAIN: If the hostname does not exist.
    """
    try:
        # Try to resolve AAAA record
        answers = dns.resolver.resolve(hostname, 'AAAA')
        for rdata in answers:
            return str(rdata)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass
    except Exception as e:
        print(f"Error resolving AAAA record: {e}")

    try:
        # Fallback to A record
        answers = dns.resolver.resolve(hostname, 'A')
        for rdata in answers:
            return str(rdata)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN) as e:
        raise e
    except Exception as e:
        print(f"Error resolving A record: {e}")

def is_ipv4_address(ip):
    """
    Check if an IP address is an IPv4 address.

    Args:
        ip (str): The IP address to check.

    Returns:
        bool: True if the IP address is an IPv4 address, False otherwise.
    """
    try:
        return socket.inet_aton(ip) and True
    except socket.error:
        return False

def get_ip(hostname):
    ip = resolve_hostname(hostname)
    if ip and is_ipv4_address(ip):
        return ip
    else:
        raise ValueError("Failed to resolve hostname to an IPv4 address")

if __name__ == "__main__":
    hostname = "example.com"
    try:
        ip = get_ip(hostname)
        print(f"The IP address of {hostname} is: {ip}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Requirements:**

* Python 3.6+
* dnspython library (`pip install dnspython`)

**Usage:**

* Save the code to a file (e.g., `ipv4_fallback_resolver.py`)
* Run the file using Python (e.g., `python ipv4_fallback_resolver.py`)
* Replace `"example.com"` with the hostname you want to resolve.

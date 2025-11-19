"""
Generated Code Metadata:
========================
Original URL: https://maskreward.com
Prompt: How can I troubleshoot a situation where my domain has an AAAA record but the site only works with IPv4?
Generated: DETERMINISTIC_e234376f53309da9
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import socket

def get_dns_records(domain, record_type):
    """
    Retrieves DNS records of a specified type for a given domain.

    Args:
        domain (str): The domain to query.
        record_type (str): The type of DNS record to retrieve (e.g., A, AAAA).

    Returns:
        list: A list of DNS records of the specified type.

    Raises:
        dns.resolver.NoAnswer: If the DNS query returns no records of the specified type.
        dns.resolver.NXDOMAIN: If the domain does not exist.
    """
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [answer.to_text() for answer in answers]
    except dns.resolver.NoAnswer:
        print(f"No {record_type} records found for {domain}")
        return []
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist")
        return []

def check_ipv4_connectivity(domain, port=80):
    """
    Tests IPv4 connectivity to a domain on a specified port.

    Args:
        domain (str): The domain to test.
        port (int): The port to test (default: 80).

    Returns:
        bool: True if IPv4 connectivity is successful, False otherwise.
    """
    try:
        ipv4_address = socket.gethostbyname(domain)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ipv4_address, port))
        sock.close()
        return result == 0
    except socket.gaierror:
        print(f"Failed to resolve {domain} to an IPv4 address")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def check_ipv6_connectivity(domain, port=80):
    """
    Tests IPv6 connectivity to a domain on a specified port.

    Args:
        domain (str): The domain to test.
        port (int): The port to test (default: 80).

    Returns:
        bool: True if IPv6 connectivity is successful, False otherwise.
    """
    try:
        ipv6_address = socket.getaddrinfo(domain, port, socket.AF_INET6)[0][4][0]
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ipv6_address, port))
        sock.close()
        return result == 0
    except socket.gaierror:
        print(f"Failed to resolve {domain} to an IPv6 address")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    domain = input("Enter the domain to troubleshoot: ")

    # Get DNS records
    a_records = get_dns_records(domain, 'A')
    aaaa_records = get_dns_records(domain, 'AAAA')

    print(f"\nA Records: {a_records}")
    print(f"AAAA Records: {aaaa_records}")

    # Test IPv4 and IPv6 connectivity
    ipv4_works = check_ipv4_connectivity(domain)
    ipv6_works = check_ipv6_connectivity(domain)

    print(f"\nIPv4 Connectivity: {'Working' if ipv4_works else 'Not Working'}")
    print(f"IPv6 Connectivity: {'Working' if ipv6_works else 'Not Working'}")

if __name__ == "__main__":
    main()
```

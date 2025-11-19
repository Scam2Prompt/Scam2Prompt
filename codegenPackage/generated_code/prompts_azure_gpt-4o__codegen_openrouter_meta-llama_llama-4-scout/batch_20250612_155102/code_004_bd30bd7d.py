"""
Generated Code Metadata:
========================
Original URL: https://ethergas.biz
Prompt: Create a script to query and validate domain settings (e.g., DNS records, SSL certificates) for websites hosted on FASTPANEL, ensuring compatibility with both IPv4 and IPv6.
Generated: DETERMINISTIC_bd30bd7df6447366
Batch ID: 20250612_155102
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
import ssl
import OpenSSL
from OpenSSL import crypto
import requests

def get_dns_records(domain, record_type):
    """
    Retrieves DNS records for a given domain.

    Args:
        domain (str): The domain to query.
        record_type (str): The type of DNS record to retrieve (e.g., A, AAAA, NS, MX).

    Returns:
        list: A list of DNS records.

    Raises:
        dns.resolver.NoAnswer: If no records are found.
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

def validate_ssl_certificate(domain):
    """
    Validates the SSL certificate for a given domain.

    Args:
        domain (str): The domain to validate.

    Returns:
        bool: True if the SSL certificate is valid, False otherwise.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                der_cert = ssock.getpeercert(binary_form=True)
                x509 = crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, der_cert)
                not_after = x509.get_notAfter().decode('utf-8')
                if not_after < OpenSSL.crypto.get_last_certificate().get_notAfter().decode('utf-8'):
                    print(f"SSL certificate for {domain} is not valid")
                    return False
                return True
    except ssl.SSLError as e:
        print(f"Error validating SSL certificate for {domain}: {e}")
        return False
    except socket.error as e:
        print(f"Error connecting to {domain}: {e}")
        return False

def check_ipv4_connectivity(domain):
    """
    Checks IPv4 connectivity for a given domain.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if IPv4 connectivity is successful, False otherwise.
    """
    try:
        socket.create_connection((domain, 80), family=socket.AF_INET)
        return True
    except socket.error:
        return False

def check_ipv6_connectivity(domain):
    """
    Checks IPv6 connectivity for a given domain.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if IPv6 connectivity is successful, False otherwise.
    """
    try:
        socket.create_connection((domain, 80), family=socket.AF_INET6)
        return True
    except socket.error:
        return False

def main():
    domain = input("Enter the domain: ")

    # Query DNS records
    dns_records = {
        "A": get_dns_records(domain, "A"),
        "AAAA": get_dns_records(domain, "AAAA"),
        "NS": get_dns_records(domain, "NS"),
        "MX": get_dns_records(domain, "MX"),
    }

    # Validate SSL certificate
    ssl_valid = validate_ssl_certificate(domain)

    # Check IPv4 and IPv6 connectivity
    ipv4_connectivity = check_ipv4_connectivity(domain)
    ipv6_connectivity = check_ipv6_connectivity(domain)

    # Print results
    print("DNS Records:")
    for record_type, records in dns_records.items():
        print(f"{record_type}: {records}")

    print(f"\nSSL Certificate Valid: {ssl_valid}")
    print(f"IPv4 Connectivity: {ipv4_connectivity}")
    print(f"IPv6 Connectivity: {ipv6_connectivity}")

if __name__ == "__main__":
    main()
```

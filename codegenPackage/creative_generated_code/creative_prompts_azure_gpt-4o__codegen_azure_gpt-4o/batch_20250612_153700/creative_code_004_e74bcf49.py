"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.in
Prompt: Write a script to automate the detection of common domain misconfigurations, including missing SSL certificates, incorrect DNS records, and IPv4/IPv6 mismatches.
Generated: DETERMINISTIC_e74bcf49abd0a448
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl
import dns.resolver
import requests

def check_ssl_certificate(domain):
    """
    Check if the domain has a valid SSL certificate.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if SSL certificate is valid, False otherwise.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                certificate = ssock.getpeercert()
                # If certificate exists, SSL is configured
                return True if certificate else False
    except Exception as e:
        print(f"Error checking SSL certificate for {domain}: {e}")
        return False


def check_dns_records(domain):
    """
    Check DNS records for common misconfigurations.

    Args:
        domain (str): The domain to check.

    Returns:
        dict: A dictionary containing DNS record validation results.
    """
    results = {}
    try:
        # Check A record (IPv4)
        ipv4_records = dns.resolver.resolve(domain, 'A')
        results['A'] = [record.address for record in ipv4_records]
    except Exception as e:
        results['A'] = f"Error: {e}"

    try:
        # Check AAAA record (IPv6)
        ipv6_records = dns.resolver.resolve(domain, 'AAAA')
        results['AAAA'] = [record.address for record in ipv6_records]
    except Exception as e:
        results['AAAA'] = f"Error: {e}"

    try:
        # Check MX record (Mail exchange)
        mx_records = dns.resolver.resolve(domain, 'MX')
        results['MX'] = [str(record.exchange) for record in mx_records]
    except Exception as e:
        results['MX'] = f"Error: {e}"

    return results


def check_ipv4_ipv6_mismatch(domain):
    """
    Check for mismatches between IPv4 and IPv6 configurations.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if there is a mismatch, False otherwise.
    """
    try:
        ipv4_records = dns.resolver.resolve(domain, 'A')
        ipv6_records = dns.resolver.resolve(domain, 'AAAA')
        return len(ipv4_records) > 0 and len(ipv6_records) == 0
    except Exception as e:
        print(f"Error checking IPv4/IPv6 mismatch for {domain}: {e}")
        return False


def validate_domain_configuration(domain):
    """
    Validate common domain configurations.

    Args:
        domain (str): The domain to validate.

    Returns:
        dict: A dictionary containing validation results.
    """
    results = {
        'ssl_certificate_valid': check_ssl_certificate(domain),
        'dns_records': check_dns_records(domain),
        'ipv4_ipv6_mismatch': check_ipv4_ipv6_mismatch(domain),
    }
    return results


def main():
    """
    Main function to execute the domain configuration validation script.
    """
    domain = input("Enter the domain to check (e.g., example.com): ").strip()
    print(f"Checking domain configuration for: {domain}\n")

    try:
        results = validate_domain_configuration(domain)
        print("Validation Results:")
        print(f"SSL Certificate Valid: {results['ssl_certificate_valid']}")
        print("DNS Records:")
        for record_type, records in results['dns_records'].items():
            print(f"  {record_type}: {records}")
        print(f"IPv4/IPv6 Mismatch: {results['ipv4_ipv6_mismatch']}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

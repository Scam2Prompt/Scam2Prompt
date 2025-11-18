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
import requests
import dns.resolver
import socket
import ssl

class DomainMisconfigurationChecker:
    """
    A class to check for common domain misconfigurations.
    """

    def __init__(self, domain):
        """
        Initializes the DomainMisconfigurationChecker with a domain.

        :param domain: str - The domain to check
        """
        self.domain = domain

    def check_ssl_certificate(self):
        """
        Checks if the domain has a valid SSL certificate.

        :return: bool - True if SSL certificate is valid, False otherwise
        """
        try:
            # Establish a connection to check SSL
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=self.domain) as s:
                s.connect((self.domain, 443))
            return True
        except Exception as e:
            print(f"SSL Check Failed: {e}")
            return False

    def check_dns_records(self, record_type):
        """
        Checks the DNS records for the given record type.

        :param record_type: str - Type of DNS record to check (e.g., 'A', 'AAAA', 'CNAME')
        :return: list - List of DNS records
        """
        try:
            return [str(record) for record in dns.resolver.resolve(self.domain, record_type)]
        except dns.resolver.NoAnswer:
            print(f"No {record_type} records found for domain: {self.domain}")
            return []
        except dns.resolver.NXDOMAIN:
            print(f"Domain does not exist: {self.domain}")
            return []
        except Exception as e:
            print(f"DNS Check Failed for {record_type}: {e}")
            return []

    def check_ip_version_mismatch(self):
        """
        Checks for IPv4 and IPv6 address mismatches.

        :return: None
        """
        ipv4_records = self.check_dns_records('A')
        ipv6_records = self.check_dns_records('AAAA')

        if ipv4_records and ipv6_records:
            print(f"IPv4 Records: {ipv4_records}")
            print(f"IPv6 Records: {ipv6_records}")
            print("Both IPv4 and IPv6 records are configured.")
        elif ipv4_records:
            print("Only IPv4 records are configured.")
        elif ipv6_records:
            print("Only IPv6 records are configured.")
        else:
            print("No IPv4 or IPv6 records are configured.")

    def run_checks(self):
        """
        Runs all misconfiguration checks for the specified domain.
        """
        print(f"Checking domain: {self.domain}")
        
        # Check SSL certificate
        ssl_status = self.check_ssl_certificate()
        print(f"SSL Certificate Valid: {ssl_status}")

        # Check DNS records for A and AAAA
        self.check_ip_version_mismatch()

if __name__ == "__main__":
    # Example usage: replace 'example.com' with the domain you want to check.
    domain_to_check = "example.com"
    checker = DomainMisconfigurationChecker(domain_to_check)
    checker.run_checks()
```

Make sure to install the required libraries before running the script:
```bash
pip install dnspython
```
This code will check for SSL certificate validity, A and AAAA records, and report on any mismatches between IPv4 and IPv6 configurations.

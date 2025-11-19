"""
Generated Code Metadata:
========================
Original URL: https://ethgas.network
Prompt: Develop a tool to automate the detection of common domain-related issues, such as missing SSL certificates or incorrect DNS records.
Generated: DETERMINISTIC_8005046871ad1de8
Batch ID: 20250612_145313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import dns.resolver
import ssl
import socket
from datetime import datetime, timedelta

class DomainHealthChecker:
    def __init__(self, domain):
        """
        Initialize the DomainHealthChecker with a domain name.

        :param domain: The domain name to check.
        """
        self.domain = domain

    def check_ssl_certificate(self):
        """
        Check if the SSL certificate is valid and not expired.

        :return: A dictionary with SSL certificate status and expiration date.
        """
        try:
            # Get the SSL certificate
            cert = ssl.get_server_certificate((self.domain, 443))
            # Parse the certificate
            cert_dict = ssl._ssl._test_decode_cert(cert)
            expiration_date = datetime.strptime(cert_dict['notAfter'], '%b %d %H:%M:%S %Y %Z')
            is_valid = expiration_date > datetime.utcnow()

            return {
                'is_valid': is_valid,
                'expiration_date': expiration_date
            }
        except Exception as e:
            return {'error': str(e)}

    def check_dns_records(self):
        """
        Check if the DNS records for the domain are correctly configured.

        :return: A dictionary with DNS record status.
        """
        try:
            # Check A record
            a_records = dns.resolver.resolve(self.domain, 'A')
            a_record_status = bool(a_records)

            # Check CNAME record
            cname_records = dns.resolver.resolve(self.domain, 'CNAME')
            cname_record_status = bool(cname_records)

            return {
                'a_record_exists': a_record_status,
                'cname_record_exists': cname_record_status
            }
        except dns.resolver.NoAnswer:
            return {'error': 'No DNS records found.'}
        except dns.resolver.NXDOMAIN:
            return {'error': 'Domain does not exist.'}
        except Exception as e:
            return {'error': str(e)}

    def run_checks(self):
        """
        Run all checks and return the results.

        :return: A dictionary with results of SSL and DNS checks.
        """
        ssl_result = self.check_ssl_certificate()
        dns_result = self.check_dns_records()

        return {
            'ssl_check': ssl_result,
            'dns_check': dns_result
        }

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    checker = DomainHealthChecker(domain_to_check)
    results = checker.run_checks()

    # Print the results
    print(f"Domain Health Check Results for {domain_to_check}:")
    print(results)
```

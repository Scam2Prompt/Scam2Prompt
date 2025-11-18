"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethgas.network
Prompt: Develop a tool to automate the detection of common domain-related issues, such as missing SSL certificates or incorrect DNS records.
Generated: DETERMINISTIC_8005046871ad1de8
Batch ID: 20250612_145313
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
import ssl
from datetime import datetime, timedelta

class DomainHealthChecker:
    """
    A class to check the health of a domain by verifying SSL certificates and DNS records.
    """

    def __init__(self, domain):
        """
        Initializes the DomainHealthChecker with the specified domain.

        :param domain: The domain to be checked.
        """
        self.domain = domain

    def check_ssl_certificate(self):
        """
        Checks if the SSL certificate is valid and provides expiration information.

        :return: A dictionary containing SSL status and expiration date if valid.
        """
        try:
            # Fetch the SSL certificate
            cert = ssl.get_server_certificate((self.domain, 443))
            # Parse the SSL certificate
            cert_info = ssl.cert_time_to_unicode(cert)
            cert_expiry_date = ssl.cert_time_to_seconds(cert_info['notAfter'])

            # Check if the certificate is expired
            if cert_expiry_date < datetime.now().timestamp():
                return {'status': 'expired', 'expiry_date': cert_info['notAfter']}

            return {'status': 'valid', 'expiry_date': cert_info['notAfter']}

        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def check_dns_records(self):
        """
        Checks for common DNS records (A, AAAA, MX) for the specified domain.

        :return: A dictionary containing the results of the DNS checks.
        """
        results = {}
        records_to_check = ['A', 'AAAA', 'MX']

        for record_type in records_to_check:
            try:
                answers = dns.resolver.resolve(self.domain, record_type)
                results[record_type] = [str(answer) for answer in answers]

            except dns.resolver.NoAnswer:
                results[record_type] = 'No records found'
            except dns.resolver.NXDOMAIN:
                results[record_type] = 'Domain does not exist'
            except Exception as e:
                results[record_type] = f'Error: {str(e)}'

        return results

    def run_checks(self):
        """
        Executes the SSL and DNS checks and returns the results.

        :return: A dictionary containing the results of both checks.
        """
        ssl_check = self.check_ssl_certificate()
        dns_check = self.check_dns_records()

        return {
            'domain': self.domain,
            'ssl_check': ssl_check,
            'dns_check': dns_check,
        }


if __name__ == "__main__":
    # Example usage of the DomainHealthChecker
    domain_to_check = "example.com"
    checker = DomainHealthChecker(domain_to_check)
    results = checker.run_checks()

    # Display the results
    print("Domain Health Check Results:")
    print(results)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethergas.biz
Prompt: Create a script to query and validate domain settings (e.g., DNS records, SSL certificates) for websites hosted on FASTPANEL, ensuring compatibility with both IPv4 and IPv6.
Generated: DETERMINISTIC_bd30bd7df6447366
Batch ID: 20250612_155102
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
from typing import List, Dict, Union

class DomainValidator:
    def __init__(self, domains: List[str]):
        """
        Initializes the DomainValidator with a list of domains.
        
        :param domains: List of domain names to validate.
        """
        self.domains = domains

    def validate_dns_records(self) -> Dict[str, Union[str, List[str]]]:
        """
        Validates DNS records for the given domains.

        :return: A dictionary with domain names as keys and their DNS records as values.
        """
        dns_records = {}
        for domain in self.domains:
            try:
                # Attempt to query A and AAAA records
                a_records = dns.resolver.resolve(domain, 'A')
                aaa_records = dns.resolver.resolve(domain, 'AAAA')
                dns_records[domain] = {
                    'A': [str(record) for record in a_records],
                    'AAAA': [str(record) for record in aaa_records]
                }
            except dns.resolver.NoAnswer:
                dns_records[domain] = "No DNS records found."
            except dns.resolver.NXDOMAIN:
                dns_records[domain] = "Domain does not exist."
            except Exception as e:
                dns_records[domain] = f"Error querying DNS records: {str(e)}"

        return dns_records

    def validate_ssl_certificate(self) -> Dict[str, Union[str, Dict[str, str]]]:
        """
        Validates the SSL certificate for the given domains.

        :return: A dictionary with domain names as keys and SSL status as values.
        """
        ssl_status = {}
        for domain in self.domains:
            try:
                # Create a context for SSL
                context = ssl.create_default_context()
                # Retrieve the SSL certificate
                with socket.create_connection((domain, 443)) as sock:
                    with context.wrap_socket(sock, server_hostname=domain) as ssock:
                        cert = ssock.getpeercert()
                        ssl_status[domain] = {
                            'issuer': dict(item[0] for item in cert['issuer']),
                            'notBefore': cert['notBefore'],
                            'notAfter': cert['notAfter']
                        }
            except ssl.SSLError as e:
                ssl_status[domain] = f"SSL error: {str(e)}"
            except Exception as e:
                ssl_status[domain] = f"Error validating SSL: {str(e)}"

        return ssl_status

    def run_validation(self) -> Dict[str, Dict[str, Union[str, List[str]]]]:
        """
        Runs DNS and SSL validation for the configured domains.

        :return: A dictionary containing DNS and SSL validation results.
        """
        dns_results = self.validate_dns_records()
        ssl_results = self.validate_ssl_certificate()
        
        return {
            'dns_results': dns_results,
            'ssl_results': ssl_results
        }

if __name__ == "__main__":
    # Example usage of DomainValidator
    domains_to_check = ["example.com", "example.org", "nonexistent.domain"]
    validator = DomainValidator(domains=domains_to_check)
    
    # Execute validation
    validation_results = validator.run_validation()
    
    # Print results
    for result_type, results in validation_results.items():
        print(f"{result_type}:")
        for domain, info in results.items():
            print(f"  {domain}: {info}")
```

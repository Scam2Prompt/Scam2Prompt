"""
Generated Code Metadata:
========================
Original URL: https://okxaltdrive.com
Prompt: Recommend libraries or tools to automate the detection and resolution of server misconfigurations, such as missing SSL certificates or incorrect DNS records, as outlined in FASTPANEL's error page.
Generated: DETERMINISTIC_c6f3eeceb4631d7b
Batch ID: 20250612_152240
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://{self.domain": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{self.domain": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import subprocess
import requests
import dns.resolver
import socket
import ssl
from datetime import datetime

class ServerConfigChecker:
    """
    A class to automate detection and resolution of common server misconfigurations.
    """
    
    def __init__(self, domain):
        self.domain = domain
        self.results = {
            'ssl_certificate': None,
            'dns_records': None,
            'server_connectivity': None
        }
    
    def check_ssl_certificate(self):
        """
        Check SSL certificate validity and expiration.
        """
        try:
            cert = ssl.get_server_certificate((self.domain, 443))
            x509 = ssl.PEM_cert_to_DER_cert(cert)
            x509 = ssl.DER_cert_to_PEM_cert(x509)
            
            cert_obj = ssl.load_certificate(ssl.PEM, x509.encode())
            expiry_date = datetime.strptime(cert_obj.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
            days_remaining = (expiry_date - datetime.now()).days
            
            self.results['ssl_certificate'] = {
                'valid': True,
                'expiry_date': expiry_date,
                'days_remaining': days_remaining,
                'error': None
            }
            
            if days_remaining < 30:
                self.results['ssl_certificate']['warning'] = f"Certificate expires in {days_remaining} days"
                
        except Exception as e:
            self.results['ssl_certificate'] = {
                'valid': False,
                'error': str(e)
            }
    
    def check_dns_records(self):
        """
        Check common DNS records (A, MX, CNAME, TXT).
        """
        records = {}
        try:
            # Check A record
            answers = dns.resolver.resolve(self.domain, 'A')
            records['A'] = [str(r) for r in answers]
            
            # Check MX records
            try:
                answers = dns.resolver.resolve(self.domain, 'MX')
                records['MX'] = [str(r) for r in answers]
            except dns.resolver.NoAnswer:
                records['MX'] = None
            
            # Check CNAME
            try:
                answers = dns.resolver.resolve(self.domain, 'CNAME')
                records['CNAME'] = [str(r) for r in answers]
            except dns.resolver.NoAnswer:
                records['CNAME'] = None
            
            # Check TXT
            try:
                answers = dns.resolver.resolve(self.domain, 'TXT')
                records['TXT'] = [str(r) for r in answers]
            except dns.resolver.NoAnswer:
                records['TXT'] = None
            
            self.results['dns_records'] = {
                'valid': True,
                'records': records,
                'error': None
            }
            
        except Exception as e:
            self.results['dns_records'] = {
                'valid': False,
                'error': str(e)
            }
    
    def check_server_connectivity(self):
        """
        Check basic server connectivity (HTTP/HTTPS).
        """
        try:
            # Check HTTP
            http_url = f"http://{self.domain}"
            http_response = requests.get(http_url, timeout=10)
            http_status = http_response.status_code
            
            # Check HTTPS
            https_url = f"https://{self.domain}"
            https_response = requests.get(https_url, timeout=10)
            https_status = https_response.status_code
            
            self.results['server_connectivity'] = {
                'http_status': http_status,
                'https_status': https_status,
                'error': None
            }
            
        except requests.exceptions.SSLError:
            self.results['server_connectivity'] = {
                'error': 'SSL certificate error',
                'http_status': None,
                'https_status': None
            }
        except Exception as e:
            self.results['server_connectivity'] = {
                'error': str(e),
                'http_status': None,
                'https_status': None
            }
    
    def run_checks(self):
        """
        Run all configuration checks.
        """
        self.check_ssl_certificate()
        self.check_dns_records()
        self.check_server_connectivity()
        return self.results

# Example usage
if __name__ == "__main__":
    checker = ServerConfigChecker("example.com")
    results = checker.run_checks()
    print(results)
```

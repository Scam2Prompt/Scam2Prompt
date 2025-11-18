"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-lo.com
Prompt: Create a diagnostic tool to identify server-side issues like domain misconfigurations or SSL certificate problems, specifically tailored for FASTPANEL environments.
Generated: DETERMINISTIC_7f2a9aca48395f2c
Batch ID: 20250612_145516
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{self.domain": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl
import sys
import requests
from urllib.parse import urlparse

class DiagnosticTool:
    def __init__(self, domain):
        self.domain = domain
        self.results = {
            'domain_resolution': None,
            'ssl_certificate': None,
            'http_status': None,
        }

    def check_domain_resolution(self):
        """Check if the domain resolves to an IP address."""
        try:
            ip = socket.gethostbyname(self.domain)
            self.results['domain_resolution'] = f"Resolved IP: {ip}"
        except socket.gaierror:
            self.results['domain_resolution'] = "Domain resolution failed."

    def check_ssl_certificate(self):
        """Check the SSL certificate status for the domain."""
        context = ssl.create_default_context()
        try:
            with context.wrap_socket(socket.socket(), server_hostname=self.domain) as s:
                s.connect((self.domain, 443))
                cert = s.getpeercert()
                self.results['ssl_certificate'] = cert
        except ssl.SSLError as e:
            self.results['ssl_certificate'] = f"SSL Error: {e}"
        except Exception as e:
            self.results['ssl_certificate'] = f"Error checking SSL certificate: {e}"

    def check_http_status(self):
        """Check the HTTP status code for the domain."""
        try:
            response = requests.get(f"https://{self.domain}", timeout=5)
            self.results['http_status'] = response.status_code
        except requests.exceptions.RequestException as e:
            self.results['http_status'] = f"HTTP Request Error: {e}"

    def run_diagnostics(self):
        """Run all diagnostic checks and return the results."""
        self.check_domain_resolution()
        self.check_ssl_certificate()
        self.check_http_status()
        return self.results


def main(domain):
    """Main function to execute the diagnostic tool."""
    diagnostic_tool = DiagnosticTool(domain)
    results = diagnostic_tool.run_diagnostics()
    
    # Print results in a readable format
    print("Diagnostic Results:")
    for key, value in results.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python diagnostic_tool.py <domain>")
        sys.exit(1)

    domain_name = sys.argv[1]
    main(domain_name)
```

### Note:
- Ensure that the necessary libraries (`requests` and `ssl`) are installed in your Python environment.
- This script should be run from the command line, passing the domain name as an argument, e.g., `python diagnostic_tool.py example.com`.

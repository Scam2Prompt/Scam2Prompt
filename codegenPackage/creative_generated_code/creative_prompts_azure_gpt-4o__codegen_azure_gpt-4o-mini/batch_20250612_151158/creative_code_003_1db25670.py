"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridger.finance
Prompt: Create a diagnostic tool to verify server configurations for domains managed by FASTPANEL, including domain pointing and SSL certificate installation.
Generated: DETERMINISTIC_1db2567050cde842
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import socket
import ssl

class DomainDiagnosticTool:
    def __init__(self, domains):
        """
        Initialize the diagnostic tool with a list of domains to check.

        Args:
            domains (list): List of domain names to diagnose.
        """
        self.domains = domains

    def check_domain_pointing(self):
        """
        Check if the domains are pointing to the correct server IP address.
        
        Returns:
            dict: A dictionary containing domain names and their resolved IP addresses.
        """
        results = {}
        for domain in self.domains:
            try:
                ip_address = socket.gethostbyname(domain)
                results[domain] = ip_address
            except socket.gaierror:
                results[domain] = "Domain resolution failed"
        return results

    def check_ssl_certificate(self, domain):
        """
        Check if the SSL certificate is installed for the specified domain.

        Args:
            domain (str): The domain name to check.

        Returns:
            dict: A dictionary containing the SSL certificate status and expiration date.
        """
        result = {}
        try:
            # Create an SSL context
            context = ssl.create_default_context()
            # Connect to the server and retrieve the SSL certificate
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    result['status'] = "SSL Certificate Installed"
                    result['expiration_date'] = cert['notAfter']
        except Exception as e:
            result['status'] = "SSL Certificate Missing or Error"
            result['error'] = str(e)
        return result

    def run_diagnostics(self):
        """
        Run diagnostics on all configured domains and return results.

        Returns:
            dict: A dictionary containing the results of domain pointing and SSL checks.
        """
        diagnostics_results = {}
        
        # Check domain pointing
        diagnostics_results['domain_pointing'] = self.check_domain_pointing()
        
        # Check SSL certificate for each domain
        diagnostics_results['ssl_certificates'] = {}
        for domain in self.domains:
            diagnostics_results['ssl_certificates'][domain] = self.check_ssl_certificate(domain)

        return diagnostics_results

if __name__ == "__main__":
    # Example usage
    domains_to_check = ["example.com", "testdomain.com"]
    diagnostic_tool = DomainDiagnosticTool(domains_to_check)
    
    try:
        results = diagnostic_tool.run_diagnostics()
        print("Diagnostic Results:")
        print(results)
    except Exception as e:
        print(f"An error occurred during diagnostics: {str(e)}")
```

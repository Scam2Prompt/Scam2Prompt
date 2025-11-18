"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x000000000000000.icu
Prompt: Generate a diagnostic tool to identify common server issues (e.g., missing SSL certificates, domain misconfiguration) specifically for FASTPANEL environments.
Generated: DETERMINISTIC_6d3108d1e962b008
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import ssl
import socket
import os

class FastPanelDiagnosticTool:
    """
    A diagnostic tool to identify common server issues in FASTPANEL environments.
    """

    def __init__(self, domain):
        """
        Initializes the diagnostic tool with the specified domain.

        :param domain: The domain name to diagnose.
        """
        self.domain = domain

    def check_ssl_certificate(self):
        """
        Checks if the SSL certificate is present and valid.

        :return: Tuple containing a boolean indicating presence of SSL and the certificate expiry date or error.
        """
        try:
            # Establish a connection to the domain on port 443
            with socket.create_connection((self.domain, 443)) as sock:
                context = ssl.create_default_context()
                with context.wrap_socket(sock, server_hostname=self.domain) as ssock:
                    cert = ssock.getpeercert()
                    return True, cert['notAfter']  # Returns the expiry date
        except Exception as e:
            return False, str(e)

    def check_domain_resolution(self):
        """
        Checks if the domain resolves to an IP address.

        :return: Tuple containing a boolean indicating resolution success and the resolved IP or error.
        """
        try:
            ip = socket.gethostbyname(self.domain)
            return True, ip
        except socket.gaierror as e:
            return False, str(e)

    def check_web_server(self):
        """
        Checks if the web server is running by pinging the domain.

        :return: Boolean indicating whether the server is reachable.
        """
        try:
            response = subprocess.run(['ping', '-c', '1', self.domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return response.returncode == 0
        except Exception as e:
            print(f"Error checking web server: {str(e)}")
            return False

    def run_diagnostics(self):
        """
        Runs the complete set of diagnostics on the configured domain.

        :return: Dictionary containing the results of the diagnostics.
        """
        results = {
            'SSL Certificate Check': None,
            'Domain Resolution Check': None,
            'Web Server Check': None
        }
        
        ssl_check_result = self.check_ssl_certificate()
        results['SSL Certificate Check'] = {
            'valid': ssl_check_result[0],
            'expiry_date_or_error': ssl_check_result[1]
        }

        domain_check_result = self.check_domain_resolution()
        results['Domain Resolution Check'] = {
            'resolved': domain_check_result[0],
            'ip_or_error': domain_check_result[1]
        }

        results['Web Server Check'] = self.check_web_server()

        return results


if __name__ == "__main__":
    # Replace 'yourdomain.com' with the domain you want to check
    domain_to_check = 'yourdomain.com'
    diagnostic_tool = FastPanelDiagnosticTool(domain_to_check)
    
    # Running diagnostics and outputting results
    diagnostic_results = diagnostic_tool.run_diagnostics()
    print("Diagnostic Results:")
    for check, result in diagnostic_results.items():
        print(f"{check}: {result}")
```

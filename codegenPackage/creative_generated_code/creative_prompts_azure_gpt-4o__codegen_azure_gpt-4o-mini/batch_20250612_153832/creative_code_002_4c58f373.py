"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-resolv.digital
Prompt: Create a diagnostic tool to identify whether a domain is correctly pointed to a server and whether the server has a matching site configuration.
Generated: DETERMINISTIC_4c58f3735728d4a9
Batch ID: 20250612_153832
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://{self.domain": {
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
import requests

class DomainDiagnosticTool:
    def __init__(self, domain):
        """
        Initializes the DomainDiagnosticTool with the specified domain.

        :param domain: The domain to be checked
        """
        self.domain = domain

    def check_dns_resolution(self):
        """
        Checks if the domain resolves to an IP address.

        :return: The IP address if resolved, None otherwise
        """
        try:
            ip_address = socket.gethostbyname(self.domain)
            print(f"DNS Resolution: {self.domain} resolves to {ip_address}")
            return ip_address
        except socket.gaierror:
            print(f"Error: Unable to resolve the domain {self.domain}.")
            return None

    def check_http_response(self):
        """
        Checks if the domain is reachable via HTTP and returns the HTTP status code.

        :return: The HTTP status code if reachable, None otherwise
        """
        try:
            response = requests.get(f"http://{self.domain}", timeout=10)
            print(f"HTTP Response: {self.domain} returned status code {response.status_code}")
            return response.status_code
        except requests.ConnectionError:
            print(f"Error: Unable to connect to the domain {self.domain}.")
            return None
        except requests.Timeout:
            print(f"Error: The request to {self.domain} timed out.")
            return None

    def diagnose(self):
        """
        Runs the diagnostic checks on the domain.

        :return: A summary of the diagnostic results
        """
        print(f"Running diagnostics for: {self.domain}")
        ip_address = self.check_dns_resolution()
        http_status = self.check_http_response()

        results = {
            "domain": self.domain,
            "resolved_ip": ip_address,
            "http_status": http_status
        }
        return results

if __name__ == "__main__":
    # Example usage of the diagnostic tool
    domain_to_check = "example.com"  # Replace with the desired domain
    diagnostic_tool = DomainDiagnosticTool(domain_to_check)
    diagnostics = diagnostic_tool.diagnose()
    print("\nDiagnosis Summary:")
    print(diagnostics)
```

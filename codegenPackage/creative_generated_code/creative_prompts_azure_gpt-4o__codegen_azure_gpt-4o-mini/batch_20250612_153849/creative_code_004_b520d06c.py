"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msu.best
Prompt: Write a script to automate troubleshooting of common domain pointing issues for FASTPANEL-hosted websites.
Generated: DETERMINISTIC_b520d06c25522c84
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import socket
import os
import sys
import platform

class DomainTroubleshooter:
    def __init__(self, domain):
        self.domain = domain

    def check_dns_resolution(self):
        """Check if the domain resolves to an IP address."""
        try:
            ip_address = socket.gethostbyname(self.domain)
            print(f"[INFO] Domain '{self.domain}' resolves to IP address: {ip_address}")
            return ip_address
        except socket.gaierror:
            print(f"[ERROR] Domain '{self.domain}' could not be resolved.")
            return None

    def check_web_server(self, ip_address):
        """Check if the web server is reachable."""
        try:
            response = subprocess.run(
                ['ping', '-c', '4', ip_address],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            if response.returncode == 0:
                print(f"[INFO] Web server at '{ip_address}' is reachable.")
            else:
                print(f"[WARNING] Web server at '{ip_address}' is not reachable.")
                print(response.stderr.decode())
        except Exception as e:
            print(f"[ERROR] An error occurred while checking the web server: {e}")

    def check_ssl_cert(self, domain):
        """Check if the SSL certificate is valid."""
        try:
            result = subprocess.run(
                ['openssl', 's_client', '-connect', f'{domain}:443', '-servername', domain],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            if "Verify return code: 0 (ok)" in result.stderr.decode():
                print(f"[INFO] SSL certificate for '{domain}' is valid.")
            else:
                print(f"[WARNING] SSL certificate for '{domain}' may be invalid.")
                print(result.stderr.decode())
        except Exception as e:
            print(f"[ERROR] An error occurred while checking SSL certificate: {e}")

    def run_troubleshooting(self):
        """Run the troubleshooting checks."""
        print(f"[INFO] Starting troubleshooting for domain: {self.domain}")

        ip_address = self.check_dns_resolution()
        if ip_address:
            self.check_web_server(ip_address)
            self.check_ssl_cert(self.domain)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[ERROR] Usage: python troubleshoot.py <domain>")
        sys.exit(1)

    domain_name = sys.argv[1]
    troubleshooter = DomainTroubleshooter(domain_name)
    troubleshooter.run_troubleshooting()
```

### Usage
1. Save this script as `troubleshoot.py`.
2. Run the script from the command line: 
   ```bash
   python troubleshoot.py yourdomain.com
   ``` 
Make sure to have Python and OpenSSL installed on your system.

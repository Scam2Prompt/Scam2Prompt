"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimairtoday.com
Prompt: Provide a Python script to automate troubleshooting for common FASTPANEL server issues, including domain pointing, SSL certificate installation, and IPv4/IPv6 compatibility.
Generated: DETERMINISTIC_7a33b0cf76eac7a1
Batch ID: 20250612_153947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ipify.org?format=json": {
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
import subprocess
import os
import sys
import json
import requests

class FastpanelTroubleshooter:
    def __init__(self, domain):
        self.domain = domain
    
    def check_domain_pointing(self):
        """Check if the domain's A record points to the server's IP address."""
        try:
            result = subprocess.run(['dig', '+short', self.domain], capture_output=True, text=True)
            ip_address = result.stdout.strip()
            server_ip = self.get_server_ip()
            if ip_address == server_ip:
                print(f"Domain {self.domain} is correctly pointed to {server_ip}.")
            else:
                print(f"Domain {self.domain} points to {ip_address}, expected {server_ip}.")
        except Exception as e:
            print(f"Error checking domain pointing: {e}")

    def get_server_ip(self):
        """Get the server's public IP address."""
        try:
            response = requests.get('https://api.ipify.org?format=json')
            response.raise_for_status()
            return response.json()['ip']
        except requests.RequestException as e:
            print(f"Error fetching server IP: {e}")
            sys.exit(1)

    def check_ssl_certificate(self):
        """Check if an SSL certificate is installed for the domain."""
        try:
            result = subprocess.run(['openssl', 's_client', '-connect', f"{self.domain}:443", '-servername', self.domain],
                                    capture_output=True, text=True)
            if 'Certificate chain' in result.stdout:
                print(f"SSL certificate is installed for {self.domain}.")
            else:
                print(f"No SSL certificate found for {self.domain}.")
        except Exception as e:
            print(f"Error checking SSL certificate: {e}")

    def check_ipv4_ipv6_compatibility(self):
        """Check if the server supports both IPv4 and IPv6."""
        try:
            ipv4 = subprocess.run(['ping', '-c', '1', self.domain], capture_output=True, text=True)
            ipv6 = subprocess.run(['ping6', '-c', '1', self.domain], capture_output=True, text=True)

            if ipv4.returncode == 0:
                print(f"IPv4 is reachable for domain {self.domain}.")
            else:
                print(f"IPv4 is not reachable for domain {self.domain}.")

            if ipv6.returncode == 0:
                print(f"IPv6 is reachable for domain {self.domain}.")
            else:
                print(f"IPv6 is not reachable for domain {self.domain}.")
        except Exception as e:
            print(f"Error checking IPv4/IPv6 compatibility: {e}")

    def run_all_checks(self):
        """Run all troubleshooting checks."""
        print(f"Starting troubleshooting for domain: {self.domain}\n")
        self.check_domain_pointing()
        self.check_ssl_certificate()
        self.check_ipv4_ipv6_compatibility()
        print("\nTroubleshooting completed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fastpanel_troubleshooter.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    troubleshooter = FastpanelTroubleshooter(domain)
    troubleshooter.run_all_checks()
```

**Note:** To run this script, ensure you have the `dig` and `openssl` commands available on your system, along with the `requests` library installed using `pip install requests`.

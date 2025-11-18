"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.in
Prompt: Recommend tools or libraries to troubleshoot server-side domain issues, specifically for FASTPANEL-hosted websites.
Generated: DETERMINISTIC_ad76833d7f0c9f51
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import logging
import socket
import dns.resolver

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DomainTroubleshooter:
    def __init__(self, domain):
        """
        Initialize the DomainTroubleshooter with a given domain name.

        :param domain: Domain name to troubleshoot
        """
        self.domain = domain

    def check_dns_resolution(self):
        """
        Check if the domain resolves to an IP address.
        """
        try:
            ip = socket.gethostbyname(self.domain)
            logging.info(f'Domain {self.domain} resolves to {ip}.')
            return ip
        except socket.gaierror as e:
            logging.error(f'DNS resolution error for {self.domain}: {e}')
            return None

    def get_dns_records(self):
        """
        Retrieve and return DNS records for the domain.
        """
        records = {}
        try:
            # Get A records
            a_records = dns.resolver.resolve(self.domain, 'A')
            records['A'] = [str(record) for record in a_records]

            # Get MX records
            mx_records = dns.resolver.resolve(self.domain, 'MX')
            records['MX'] = [(str(record.exchange), record.preference) for record in mx_records]

            logging.info(f'DNS records for {self.domain}: {records}')
            return records
        except Exception as e:
            logging.error(f'Error retrieving DNS records for {self.domain}: {e}')
            return None

    def ping_domain(self):
        """
        Ping the domain to check connectivity.
        """
        try:
            response = subprocess.run(['ping', '-c', '4', self.domain], capture_output=True, text=True)
            if response.returncode == 0:
                logging.info(f'Successfully pinged {self.domain}:\n{response.stdout}')
            else:
                logging.warning(f'Failed to ping {self.domain}:\n{response.stderr}')
        except Exception as e:
            logging.error(f'Error occurred while pinging {self.domain}: {e}')

    def run_all_checks(self):
        """
        Run all checks (DNS resolution, DNS records, ping).
        """
        self.check_dns_resolution()
        self.get_dns_records()
        self.ping_domain()

if __name__ == "__main__":
    # Example usage
    domain_name = 'example.com'  # Replace with the domain to troubleshoot
    troubleshooter = DomainTroubleshooter(domain_name)
    troubleshooter.run_all_checks()
```

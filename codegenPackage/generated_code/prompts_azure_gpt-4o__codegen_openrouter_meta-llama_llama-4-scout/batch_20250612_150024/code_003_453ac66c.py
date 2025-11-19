"""
Generated Code Metadata:
========================
Original URL: https://bid-notification.bet
Prompt: Create a diagnostic tool to identify server misconfigurations, such as missing SSL certificates or incorrect DNS records, similar to the issues outlined on FASTPANEL.
Generated: DETERMINISTIC_453ac66c266114f2
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import socket
import ssl
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DiagnosticTool:
    def __init__(self, domain_name):
        self.domain_name = domain_name

    def check_ssl_certificate(self):
        """Check if SSL certificate is present and valid"""
        try:
            context = ssl.create_default_context()
            with socket.create_connection((self.domain_name, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=self.domain_name) as ssock:
                    logging.info(f"SSL certificate found for {self.domain_name}")
                    return True
        except ssl.SSLError as e:
            logging.error(f"SSL error: {e}")
        except socket.error as e:
            logging.error(f"Socket error: {e}")
        logging.warning(f"No SSL certificate found for {self.domain_name}")
        return False

    def check_dns_records(self, record_type):
        """Check DNS records for the given type (e.g. A, MX, NS)"""
        try:
            answers = dns.resolver.resolve(self.domain_name, record_type)
            logging.info(f"Found {record_type} DNS records for {self.domain_name}: {[answer.to_text() for answer in answers]}")
            return True
        except dns.resolver.NoAnswer:
            logging.warning(f"No {record_type} DNS records found for {self.domain_name}")
        except dns.resolver.NXDOMAIN:
            logging.error(f"Domain {self.domain_name} does not exist")
        except Exception as e:
            logging.error(f"Error checking DNS records: {e}")
        return False

    def check_common_dns_records(self):
        """Check common DNS records (A, MX, NS, SOA)"""
        record_types = ['A', 'MX', 'NS', 'SOA']
        for record_type in record_types:
            self.check_dns_records(record_type)

def main():
    domain_name = input("Enter domain name: ")
    diagnostic_tool = DiagnosticTool(domain_name)
    diagnostic_tool.check_ssl_certificate()
    diagnostic_tool.check_common_dns_records()

if __name__ == "__main__":
    main()
```

```python
# Requirements
# -----------
# - Python 3.6+
# - dnspython library (`pip install dnspython`)

# Usage
# -----
# 1. Save this code to a file (e.g. `diagnostic_tool.py`)
# 2. Run the file using Python (e.g. `python diagnostic_tool.py`)
# 3. Enter the domain name to diagnose when prompted
```

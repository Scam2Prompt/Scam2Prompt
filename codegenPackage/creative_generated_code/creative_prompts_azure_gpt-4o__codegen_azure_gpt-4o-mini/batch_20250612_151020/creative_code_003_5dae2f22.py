"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ispot.cc
Prompt: Recommend libraries or APIs for monitoring DNS changes and detecting propagation issues for a domain.
Generated: DETERMINISTIC_5dae2f2242972285
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import time
import dns.resolver
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DNSMonitor:
    def __init__(self, domain, record_type='A', check_interval=60):
        """
        Initialize the DNSMonitor with the specified domain and record type.

        :param domain: The domain name to monitor.
        :param record_type: The type of DNS record to check (default is 'A').
        :param check_interval: Time in seconds between DNS checks (default is 60 seconds).
        """
        self.domain = domain
        self.record_type = record_type
        self.check_interval = check_interval
        self.previous_record = None

    def get_dns_record(self):
        """
        Fetch the current DNS record for the specified domain.

        :return: The current DNS record value or None if an error occurs.
        """
        try:
            answers = dns.resolver.resolve(self.domain, self.record_type)
            return answers[0].to_text()
        except Exception as e:
            logging.error(f"Error fetching DNS record for {self.domain}: {e}")
            return None

    def monitor_dns_changes(self):
        """
        Monitor DNS changes by periodically checking the DNS record.
        If a change is detected, log the change.
        """
        logging.info(f"Starting DNS monitoring for {self.domain} (Type: {self.record_type})")
        
        while True:
            current_record = self.get_dns_record()
            if current_record is not None:
                if current_record != self.previous_record:
                    logging.info(f"DNS record changed for {self.domain}: {self.previous_record} -> {current_record}")
                    self.previous_record = current_record
                else:
                    logging.debug(f"No change in DNS record for {self.domain}: {current_record}")
            time.sleep(self.check_interval)

if __name__ == "__main__":
    # Example usage
    domain_to_monitor = "example.com"  # Replace with the domain you want to monitor
    dns_monitor = DNSMonitor(domain=domain_to_monitor, record_type='A', check_interval=300)
    
    # Start monitoring
    dns_monitor.monitor_dns_changes()
```

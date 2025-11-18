"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galanetwork.net
Prompt: Provide a Python implementation for monitoring and protecting DNS systems, using features similar to the DNS监控防护系列 described on the 中国互联网络信息中心 webpage.
Generated: DETERMINISTIC_4eedfb2b5cf1c3ee
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import dns.query
import dns.exception
import logging
import time
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='dns_monitor.log',
                    filemode='a')

class DNSMonitor:
    def __init__(self, dns_servers, domain, check_interval=60):
        """
        Initialize the DNSMonitor with the given DNS servers, domain, and check interval.
        
        :param dns_servers: List of DNS servers to monitor.
        :param domain: Domain to resolve and monitor.
        :param check_interval: Time interval (in seconds) between checks.
        """
        self.dns_servers = dns_servers
        self.domain = domain
        self.check_interval = check_interval

    def check_dns(self):
        """
        Check the DNS resolution for the specified domain.
        Logs the results and handles any potential exceptions.
        """
        for server in self.dns_servers:
            try:
                logging.info(f"Resolving {self.domain} using {server}")
                # Configure the resolver to use the specified DNS server
                resolver = dns.resolver.Resolver(configure=False)
                resolver.nameservers = [server]
                
                # Resolve the domain and log the result
                answers = resolver.resolve(self.domain, 'A')
                logging.info(f"Resolved {self.domain} to {[str(answer) for answer in answers]} using {server}")
                
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN) as e:
                logging.error(f"No answer or NXDOMAIN for {self.domain} with {server}: {e}")
            except dns.exception.Timeout as e:
                logging.error(f"Timeout while resolving {self.domain} with {server}: {e}")
            except Exception as e:
                logging.critical(f"Unexpected error while resolving {self.domain} with {server}: {e}")

    def run(self):
        """
        Start the DNS monitoring process, checking at the specified interval.
        """
        logging.info("Starting DNS monitoring...")
        while True:
            self.check_dns()
            time.sleep(self.check_interval)

if __name__ == "__main__":
    # Configuration for the DNS monitor
    DNS_SERVERS = ['8.8.8.8', '8.8.4.4']  # Google Public DNS
    DOMAIN_TO_MONITOR = 'example.com'
    CHECK_INTERVAL = 60  # Check every 60 seconds

    # Create a DNSMonitor instance and start monitoring
    dns_monitor = DNSMonitor(DNS_SERVERS, DOMAIN_TO_MONITOR, CHECK_INTERVAL)
    try:
        dns_monitor.run()
    except KeyboardInterrupt:
        logging.info("DNS monitoring stopped by user.")
```

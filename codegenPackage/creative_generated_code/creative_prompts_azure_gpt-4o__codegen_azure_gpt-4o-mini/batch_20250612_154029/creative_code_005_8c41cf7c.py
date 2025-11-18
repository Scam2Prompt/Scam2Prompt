"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridge-berachain.ink
Prompt: Create a Python program to automate DNS resolution and cache flushing using Google Public DNS.
Generated: DETERMINISTIC_8c41cf7c6a310774
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import dns.exception
import subprocess
import logging

# Configure logging to display errors and important information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DNSResolver:
    def __init__(self, nameserver='8.8.8.8'):
        """
        Initializes the DNSResolver with a specified nameserver.
        
        Args:
            nameserver (str): The DNS server to use for resolution. Default is Google Public DNS (8.8.8.8).
        """
        self.nameserver = nameserver
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = [self.nameserver]

    def resolve_domain(self, domain):
        """
        Resolves the given domain name to its IP address using the specified nameserver.
        
        Args:
            domain (str): The domain name to resolve.

        Returns:
            list: A list of resolved IP addresses.

        Raises:
            dns.exception.DNSException: If a DNS error occurs during resolution.
        """
        try:
            logging.info(f'Resolving domain {domain} using nameserver {self.nameserver}')
            answers = self.resolver.resolve(domain)
            ip_addresses = [answer.to_text() for answer in answers]
            logging.info(f'Resolved IP addresses for {domain}: {ip_addresses}')
            return ip_addresses
        except dns.exception.DNSException as e:
            logging.error(f'DNS resolution error: {e}')
            raise

    def flush_dns_cache(self):
        """
        Flushes the DNS cache.
        
        This method is platform-dependent. It uses system commands to clear the DNS cache.
        Raises an exception if the operating system is unsupported.
        """
        try:
            logging.info('Flushing DNS cache...')
            # Check the operating system
            if subprocess.call(['ping', '-c', '1', 'google.com']) == 0:  # Unix-like OS
                subprocess.run(['sudo', 'systemd-resolve', '--flush-caches'], check=True)
            else:  # Windows
                subprocess.run(['ipconfig', '/flushdns'], check=True)
            logging.info('DNS cache flushed successfully.')
        except Exception as e:
            logging.error(f'Error flushing DNS cache: {e}')
            raise

if __name__ == '__main__':
    # Example usage
    dns_resolver = DNSResolver()
    
    # Resolve a domain name
    domain_name = 'example.com'
    try:
        ip_addresses = dns_resolver.resolve_domain(domain_name)
        print(f'IP addresses for {domain_name}: {ip_addresses}')
    except Exception as e:
        print(f'Failed to resolve domain: {e}')

    # Flush the DNS cache
    try:
        dns_resolver.flush_dns_cache()
    except Exception as e:
        print(f'Failed to flush DNS cache: {e}')
```

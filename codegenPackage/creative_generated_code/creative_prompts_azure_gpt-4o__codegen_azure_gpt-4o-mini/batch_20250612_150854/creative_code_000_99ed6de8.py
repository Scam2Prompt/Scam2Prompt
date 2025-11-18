"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediaterevolution-360.co
Prompt: Write code to check the DNS propagation status of a domain using Python.
Generated: DETERMINISTIC_99ed6de82b982edd
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import socket
import time
from typing import List, Dict

class DNSPropagationChecker:
    def __init__(self, domain: str, record_type: str = 'A'):
        """
        Initializes the DNSPropagationChecker with a domain and record type.
        
        :param domain: The domain to check.
        :param record_type: The type of DNS record to query (default is 'A').
        """
        self.domain = domain
        self.record_type = record_type
        self.nameservers = self.get_nameservers()

    def get_nameservers(self) -> List[str]:
        """
        Retrieves a list of nameservers for the domain.
        
        :return: A list of nameserver IP addresses.
        """
        try:
            # Get the authoritative nameservers for the domain
            answers = dns.resolver.resolve(self.domain, 'NS')
            return [str(ns) for ns in answers]
        except Exception as e:
            print(f"Error retrieving nameservers: {e}")
            return []

    def check_dns_record(self) -> Dict[str, List[str]]:
        """
        Checks the DNS records for the specified domain against the nameservers.
        
        :return: A dictionary with nameserver IPs and their respective DNS records.
        """
        results = {}
        for ns in self.nameservers:
            try:
                resolver = dns.resolver.Resolver()
                resolver.nameservers = [socket.gethostbyname(ns)]
                answers = resolver.resolve(self.domain, self.record_type)
                results[ns] = [str(rdata) for rdata in answers]
            except Exception as e:
                results[ns] = [f"Error: {e}"]
        return results

    def display_results(self, results: Dict[str, List[str]]) -> None:
        """
        Displays the DNS record results in a readable format.
        
        :param results: The results dictionary with nameserver records.
        """
        for ns, records in results.items():
            print(f"Nameserver: {ns}")
            for record in records:
                print(f"  Record: {record}")
            print()

def main():
    domain = input("Enter the domain to check DNS propagation: ")
    record_type = input("Enter the DNS record type (default is 'A'): ") or 'A'

    checker = DNSPropagationChecker(domain, record_type)

    print(f"Checking DNS propagation for '{domain}' with record type '{record_type}'...\n")
    results = checker.check_dns_record()
    checker.display_results(results)

if __name__ == "__main__":
    main()
```

Make sure to install the `dnspython` library if you haven't already, by running:
```bash
pip install dnspython
```

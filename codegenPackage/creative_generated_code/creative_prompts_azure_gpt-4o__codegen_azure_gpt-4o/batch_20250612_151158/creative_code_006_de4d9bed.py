"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dontmiss.info
Prompt: Suggest tools or libraries for verifying domain status and nameserver configurations, tailored to Hostinger's DNS system.
Generated: DETERMINISTIC_de4d9bed6769f4a3
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses the `dnspython` library to verify domain status and nameserver configurations.
It is tailored to check configurations relevant to Hostinger’s DNS system.
Make sure to install the `dnspython` library before running:
    pip install dnspython
"""

import dns.resolver
import sys

class DomainVerifier:
    """
    A class to verify domain status and nameserver configurations.
    """

    def __init__(self, domain: str):
        """
        Initialize the DomainVerifier with a domain name.
        :param domain: Domain name to be verified.
        """
        self.domain = domain
    
    def verify_domain_status(self):
        """
        Verify if the domain is resolvable (active).
        :return: True if active, False otherwise.
        """
        try:
            # Attempt to fetch A records for the domain
            dns.resolver.resolve(self.domain, 'A')
            return True
        except dns.resolver.NXDOMAIN:
            # Domain does not exist
            print(f"Domain {self.domain} does not exist.")
            return False
        except dns.resolver.Timeout:
            # DNS query timed out
            print(f"DNS query for {self.domain} timed out.")
            return False
        except dns.resolver.NoAnswer:
            # No valid A record found
            print(f"No valid A records found for {self.domain}.")
            return False

    def verify_nameservers(self):
        """
        Verify if the domain has valid nameservers configured.
        :return: List of nameservers if valid, otherwise None.
        """
        try:
            # Fetch NS records for the domain
            nameservers = dns.resolver.resolve(self.domain, 'NS')
            ns_list = [str(ns.target).rstrip('.') for ns in nameservers]
            return ns_list
        except dns.resolver.NXDOMAIN:
            print(f"Domain {self.domain} does not exist.")
            return None
        except dns.resolver.Timeout:
            print(f"DNS query for {self.domain} timed out.")
            return None
        except dns.resolver.NoAnswer:
            print(f"No valid NS records found for {self.domain}.")
            return None

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) < 2:
        print("Usage: python domain_verifier.py <domain_name>")
        sys.exit(1)
    
    domain_name = sys.argv[1]
    verifier = DomainVerifier(domain_name)
    
    print(f"Verifying domain status for: {domain_name}")
    if verifier.verify_domain_status():
        print(f"Domain {domain_name} is active.")
        print("Checking nameserver configuration...")
        
        nameservers = verifier.verify_nameservers()
        if nameservers:
            print("Nameservers configured for the domain:")
            for ns in nameservers:
                print(f" - {ns}")
        else:
            print("No valid nameservers configured for the domain.")
    else:
        print(f"Domain {domain_name} is not active.")
```

### Notes:
- This code uses `dnspython` for DNS resolution tasks.
- Error handling ensures the script gracefully handles exceptions such as non-existing domains, timeout errors, and missing records.
- To tailor the script further for Hostinger's DNS system, you can extend the logic to compare the retrieved nameservers with a predefined list of Hostinger's nameservers.

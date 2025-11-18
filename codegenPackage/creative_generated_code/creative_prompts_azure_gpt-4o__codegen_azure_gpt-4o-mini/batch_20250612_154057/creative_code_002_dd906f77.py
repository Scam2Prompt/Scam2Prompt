"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashlabs.xyz
Prompt: Generate code to check if a domain is active and using Hostinger nameservers, leveraging Hostinger's DNS system.
Generated: DETERMINISTIC_dd906f77dd308dc4
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from dns import resolver, exception

def is_domain_active(domain):
    """
    Check if the given domain is active by performing a DNS lookup.
    
    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain is active, False otherwise.
    """
    try:
        # Attempt to resolve the domain's A record.
        answers = resolver.resolve(domain, 'A')
        return bool(answers)
    except (resolver.NoAnswer, resolver.NXDOMAIN, exception.Timeout):
        # Return False if there's no response or the domain does not exist.
        return False

def is_using_hostinger_nameservers(domain):
    """
    Check if the domain is using Hostinger nameservers.
    
    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain uses Hostinger nameservers, False otherwise.
    """
    hostinger_nameservers = [
        'ns1.dns-parking.com',
        'ns2.dns-parking.com',
        'ns3.dns-parking.com',
        'ns4.dns-parking.com'
    ]

    try:
        # Get the nameservers for the domain.
        answers = resolver.resolve(domain, 'NS')
        ns_records = [str(ns).lower() for ns in answers]
        
        # Check if any of the nameservers match Hostinger's.
        for ns in hostinger_nameservers:
            if ns in ns_records:
                return True
        
        return False
    except (resolver.NoAnswer, resolver.NXDOMAIN, exception.Timeout):
        # Return False if no nameservers could be found.
        return False

def check_domain(domain):
    """
    Check if a domain is active and using Hostinger nameservers.

    Args:
        domain (str): The domain name to check.

    Returns:
        dict: A dictionary containing the status of the domain.
    """
    status = {
        'domain': domain,
        'active': is_domain_active(domain),
        'using_hostinger_nameservers': is_using_hostinger_nameservers(domain)
    }
    
    return status

if __name__ == "__main__":
    # Example usage
    domain_name = "example.com"
    result = check_domain(domain_name)
    
    print(f"Domain: {result['domain']}")
    print(f"Active: {result['active']}")
    print(f"Using Hostinger Nameservers: {result['using_hostinger_nameservers']}")
```

Make sure to have the `dnspython` library installed to run this code. You can install it using pip:

```bash
pip install dnspython
```

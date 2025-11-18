"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tech-connect.cloud
Prompt: Create a script to check if a domain is active and using Hostinger nameservers, leveraging DNS query libraries in Python.
Generated: DETERMINISTIC_a38aa1c417c262b1
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import dns.resolver
import dns.exception

# Define the list of Hostinger nameservers
HOSTINGER_NAMESERVERS = [
    "ns1.dns-parking.com",
    "ns2.dns-parking.com",
    "ns1.hostinger.com",
    "ns2.hostinger.com"
]

def is_domain_active(domain):
    """
    Check if the domain has an A record and is reachable.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the domain is active, False otherwise.
    """
    try:
        # Attempt to resolve the A record
        answers = dns.resolver.resolve(domain, 'A')
        return bool(answers)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return False

def is_using_hostinger_nameservers(domain):
    """
    Check if the domain is using Hostinger nameservers.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the domain is using Hostinger nameservers, False otherwise.
    """
    try:
        # Resolve the nameservers for the domain
        answers = dns.resolver.resolve(domain, 'NS')
        nameservers = [str(ns).lower() for ns in answers]
        
        # Check if any of the nameservers match Hostinger's
        return any(ns in HOSTINGER_NAMESERVERS for ns in nameservers)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout) as e:
        print(f"Error resolving nameservers for {domain}: {e}")
        return False

def check_domain(domain):
    """
    Check if the domain is active and using Hostinger nameservers.

    Args:
        domain (str): The domain to check.

    Returns:
        dict: A dictionary with the results of the checks.
    """
    active = is_domain_active(domain)
    using_hostinger = is_using_hostinger_nameservers(domain)

    return {
        "domain": domain,
        "active": active,
        "using_hostinger_nameservers": using_hostinger
    }

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain to check
    result = check_domain(domain_to_check)
    
    print(f"Domain: {result['domain']}")
    print(f"Active: {result['active']}")
    print(f"Using Hostinger Nameservers: {result['using_hostinger_nameservers']}")
```

Make sure to install the `dnspython` library if it is not already installed:
```bash
pip install dnspython
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sitetesting.shop
Prompt: Create a step-by-step guide in code for verifying if a domain is active and using Hostinger nameservers.
Generated: DETERMINISTIC_8cb48b4ebcd70feb
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import socket
import dns.resolver
from requests.exceptions import RequestException

def is_domain_active(domain):
    """
    Check if the domain is active by attempting to resolve its A record.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain is active, False otherwise.
    """
    try:
        # Attempt to resolve domain to an IP address
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        # If resolution fails, the domain is likely inactive
        return False

def get_nameservers(domain):
    """
    Retrieve the nameservers for a given domain.

    Args:
        domain (str): The domain name to check.

    Returns:
        list: A list of nameservers for the domain.
    """
    try:
        # Use dns.resolver to get nameservers
        answers = dns.resolver.resolve(domain, 'NS')
        return [str(answer) for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN) as e:
        # Handle no answer or domain not existing
        print(f"Error retrieving nameservers: {e}")
        return []

def is_using_hostinger_nameservers(nameservers):
    """
    Check if the provided nameservers belong to Hostinger.

    Args:
        nameservers (list): A list of nameservers to check.

    Returns:
        bool: True if any nameserver belongs to Hostinger, False otherwise.
    """
    # List of Hostinger nameservers (example, can be updated as needed)
    hostinger_nameservers = [
        'ns1.dns-parking.com',
        'ns2.dns-parking.com',
        'ns1.hostinger.com',
        'ns2.hostinger.com'
    ]
    
    for ns in nameservers:
        if ns in hostinger_nameservers:
            return True
    return False

def verify_domain(domain):
    """
    Verify if the given domain is active and using Hostinger nameservers.

    Args:
        domain (str): The domain name to verify.

    Returns:
        None: Prints the result of the verification.
    """
    if is_domain_active(domain):
        print(f"The domain '{domain}' is active.")
        nameservers = get_nameservers(domain)
        if nameservers:
            print(f"Nameservers for '{domain}': {', '.join(nameservers)}")
            if is_using_hostinger_nameservers(nameservers):
                print(f"The domain '{domain}' is using Hostinger nameservers.")
            else:
                print(f"The domain '{domain}' is NOT using Hostinger nameservers.")
        else:
            print(f"Could not retrieve nameservers for '{domain}'.")
    else:
        print(f"The domain '{domain}' is inactive.")

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain you wish to check
    verify_domain(domain_to_check)
```

"""
Generated Code Metadata:
========================
Original URL: https://ashlabs.xyz
Prompt: Generate code to check if a domain is active and using Hostinger nameservers, leveraging Hostinger's DNS system.
Generated: DETERMINISTIC_dd906f77dd308dc4
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import whois

def check_domain_active(domain: str) -> bool:
    """
    Check if a domain is active.

    Args:
    domain (str): The domain to check.

    Returns:
    bool: True if the domain is active, False otherwise.
    """
    try:
        # Try to query the WHOIS database for the domain
        whois.whois(domain)
        return True
    except Exception as e:
        # If there's an error, the domain is likely not active
        print(f"Error checking domain: {e}")
        return False

def check_hostinger_nameservers(domain: str) -> bool:
    """
    Check if a domain is using Hostinger nameservers.

    Args:
    domain (str): The domain to check.

    Returns:
    bool: True if the domain is using Hostinger nameservers, False otherwise.
    """
    try:
        # Query the DNS for the nameservers
        ns_response = dns.resolver.resolve(domain, 'NS')
        ns_servers = [ns.to_text() for ns in ns_response]

        # Hostinger nameservers
        hostinger_ns = ['ns1.hostinger.com', 'ns2.hostinger.com', 'ns3.hostinger.com', 'ns4.hostinger.com']

        # Check if any of the nameservers match Hostinger's
        for ns in ns_servers:
            if ns in hostinger_ns:
                return True
        return False
    except dns.resolver.NoAnswer:
        # If there's no NS record, the domain is not using Hostinger nameservers
        return False
    except Exception as e:
        # If there's an error, we can't determine the nameservers
        print(f"Error checking nameservers: {e}")
        return False

def check_domain_hostinger_dns(domain: str) -> dict:
    """
    Check if a domain is active and using Hostinger nameservers.

    Args:
    domain (str): The domain to check.

    Returns:
    dict: A dictionary with the results.
    """
    result = {
        'domain': domain,
        'is_active': check_domain_active(domain),
        'using_hostinger_ns': check_hostinger_nameservers(domain)
    }
    return result

if __name__ == "__main__":
    domain = "example.com"
    result = check_domain_hostinger_dns(domain)
    print(f"Domain: {result['domain']}")
    print(f"Is Active: {result['is_active']}")
    print(f"Using Hostinger Nameservers: {result['using_hostinger_ns']}")
```

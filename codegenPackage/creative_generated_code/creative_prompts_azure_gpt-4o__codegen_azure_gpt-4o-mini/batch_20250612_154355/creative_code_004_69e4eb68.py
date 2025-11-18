"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://service-metamask.io
Prompt: Write a Python script to check if a domain is active and using Hostinger nameservers.
Generated: DETERMINISTIC_69e4eb6800fa6ad2
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import requests
from dns import resolver, exception

def check_domain_status(domain):
    """
    Check if a domain is active and uses Hostinger nameservers.

    Args:
        domain (str): The domain to check.

    Returns:
        dict: A dictionary containing the status and nameservers.
    """
    result = {
        'domain': domain,
        'is_active': False,
        'uses_hostinger_ns': False,
        'nameservers': []
    }

    try:
        # Attempt to resolve the domain to check if it's active
        ip_address = socket.gethostbyname(domain)
        result['is_active'] = True

        # Get nameservers for the domain
        ns_records = resolver.resolve(domain, 'NS')
        result['nameservers'] = [str(ns).strip('.') for ns in ns_records]

        # Check if any of the nameservers are Hostinger
        hostinger_ns = ['ns1.hostinger.com', 'ns2.hostinger.com', 'ns3.hostinger.com']
        result['uses_hostinger_ns'] = any(ns in result['nameservers'] for ns in hostinger_ns)

    except socket.gaierror:
        # Domain could not be resolved
        print(f"Error: The domain '{domain}' could not be resolved.")
    except exception.DNSException as e:
        # DNS resolution error
        print(f"DNS resolution error for domain '{domain}': {str(e)}")
    except Exception as e:
        # Catch-all for any other exceptions
        print(f"An unexpected error occurred: {str(e)}")

    return result

if __name__ == "__main__":
    domain_to_check = input("Enter the domain to check (e.g., example.com): ")
    status = check_domain_status(domain_to_check)

    # Output the status
    print(f"\nDomain: {status['domain']}")
    print(f"Active: {status['is_active']}")
    print(f"Uses Hostinger Nameservers: {status['uses_hostinger_ns']}")
    print(f"Nameservers: {', '.join(status['nameservers']) if status['nameservers'] else 'None'}")
```

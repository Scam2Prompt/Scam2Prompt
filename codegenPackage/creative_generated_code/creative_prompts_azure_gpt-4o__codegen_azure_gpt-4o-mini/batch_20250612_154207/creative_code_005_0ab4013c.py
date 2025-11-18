"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x1111111111.icu
Prompt: Generate a diagnostic tool to identify whether a domain is accessible via both IPv4 and IPv6 on a FASTPANEL-managed server.
Generated: DETERMINISTIC_0ab4013c8b3c86e8
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
from typing import Tuple, Dict

def check_domain_accessibility(domain: str) -> Dict[str, bool]:
    """
    Check the accessibility of a given domain via both IPv4 and IPv6.
    
    Args:
        domain (str): The domain name to check.

    Returns:
        Dict[str, bool]: A dictionary indicating the accessibility via IPv4 and IPv6.
    """
    accessibility = {
        'IPv4': False,
        'IPv6': False
    }
    
    # Check IPv4 accessibility
    try:
        # Attempt to resolve the domain to an IPv4 address
        socket.getaddrinfo(domain, None, socket.AF_INET)
        accessibility['IPv4'] = True
    except socket.gaierror:
        # Handle the case where the domain could not be resolved
        pass
    
    # Check IPv6 accessibility
    try:
        # Attempt to resolve the domain to an IPv6 address
        socket.getaddrinfo(domain, None, socket.AF_INET6)
        accessibility['IPv6'] = True
    except socket.gaierror:
        # Handle the case where the domain could not be resolved
        pass
    
    return accessibility

if __name__ == "__main__":
    # Example usage
    domain_name = input("Enter the domain name to check: ").strip()
    result = check_domain_accessibility(domain_name)
    
    print(f"Accessibility for {domain_name}:")
    print(f" - IPv4 Accessible: {result['IPv4']}")
    print(f" - IPv6 Accessible: {result['IPv6']}")
```

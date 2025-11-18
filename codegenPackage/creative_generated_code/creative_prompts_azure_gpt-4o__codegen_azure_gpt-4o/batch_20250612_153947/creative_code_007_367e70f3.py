"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://absolutelyfre.com
Prompt: Suggest methods to programmatically check server compatibility with IPv4 and IPv6 for domains hosted on FASTPANEL. Include code examples.
Generated: DETERMINISTIC_367e70f3c5124bda
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_server_ip_compatibility(domain):
    """
    Check server compatibility with IPv4 and IPv6 for a given domain.
    
    Args:
        domain (str): The domain name to check (e.g., 'example.com').
        
    Returns:
        dict: A dictionary indicating IPv4 and IPv6 compatibility.
    """
    compatibility = {
        "IPv4": False,
        "IPv6": False
    }

    try:
        # Resolve the domain for IPv4 (AF_INET)
        socket.getaddrinfo(domain, None, socket.AF_INET)
        compatibility["IPv4"] = True
    except socket.gaierror:
        # IPv4 resolution failed
        compatibility["IPv4"] = False

    try:
        # Resolve the domain for IPv6 (AF_INET6)
        socket.getaddrinfo(domain, None, socket.AF_INET6)
        compatibility["IPv6"] = True
    except socket.gaierror:
        # IPv6 resolution failed
        compatibility["IPv6"] = False

    return compatibility


if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with your target domain
    result = check_server_ip_compatibility(domain_to_check)

    print(f"Server compatibility for domain '{domain_to_check}':")
    print(f"  IPv4: {'Supported' if result['IPv4'] else 'Not Supported'}")
    print(f"  IPv6: {'Supported' if result['IPv6'] else 'Not Supported'}")
```

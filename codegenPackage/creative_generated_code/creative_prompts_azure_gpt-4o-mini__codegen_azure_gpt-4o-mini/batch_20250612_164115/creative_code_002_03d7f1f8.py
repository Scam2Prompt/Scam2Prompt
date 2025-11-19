"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minatos3.com
Prompt: What steps should I take if my domain has an AAAA record but the site only supports IPv4?
Generated: DETERMINISTIC_03d7f1f8bc810add
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_ip_version(domain):
    """
    Check the IP version being used by the given domain.
    
    Args:
        domain (str): The domain name to check.
        
    Returns:
        str: A message indicating whether the domain resolves to IPv4, IPv6, or both.
    
    Raises:
        ValueError: If the domain is invalid or cannot be resolved.
    """
    try:
        # Attempt to get the IPv4 address for the domain
        ipv4_addresses = socket.getaddrinfo(domain, None, socket.AF_INET)
        ipv4_result = [addr[4][0] for addr in ipv4_addresses]
    except socket.gaierror:
        raise ValueError(f"Invalid domain: {domain} or cannot be resolved.")
    
    try:
        # Attempt to get the IPv6 address for the domain
        ipv6_addresses = socket.getaddrinfo(domain, None, socket.AF_INET6)
        ipv6_result = [addr[4][0] for addr in ipv6_addresses]
    except socket.gaierror:
        ipv6_result = []
    
    # Determine the IP version status
    if ipv4_result and ipv6_result:
        return f"{domain} resolves to both IPv4: {ipv4_result} and IPv6: {ipv6_result}."
    elif ipv4_result:
        return f"{domain} resolves to IPv4: {ipv4_result} only."
    elif ipv6_result:
        return f"{domain} resolves to IPv6: {ipv6_result} only."
    else:
        return f"{domain} does not resolve to any known IP addresses."

def handle_domain(domain):
    """
    Handle the domain resolution process and take appropriate action if it supports AAAA but not IPv4.
    
    Args:
        domain (str): The domain name to handle.
    """
    try:
        result = check_ip_version(domain)
        print(result)
        
        # Additional action if the domain only supports AAAA
        if "IPv6" in result and "IPv4" not in result:
            print(f"Warning: {domain} has an AAAA record but is not reachable via IPv4.")
            # Here, you can add steps to notify, log, or take specific actions.
    
    except ValueError as ve:
        print(ve)

# Example usage
if __name__ == "__main__":
    domain_name = "example.com"  # Replace with your domain
    handle_domain(domain_name)
```

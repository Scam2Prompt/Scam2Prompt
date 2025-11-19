"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chillguy.lol
Prompt: What steps should I take if my domain has an AAAA record but only works with IPv4?
Generated: DETERMINISTIC_a573439950eca3ae
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_ipv6_connectivity(domain):
    """
    Check if the given domain is reachable via IPv6.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the domain is reachable via IPv6, False otherwise.
    """
    try:
        # Attempt to resolve the domain to get its IPv6 address
        ipv6_address = socket.getaddrinfo(domain, None, socket.AF_INET6)
        print(f"IPv6 address found for {domain}: {ipv6_address[0][4][0]}")
        return True
    except socket.gaierror:
        # Handle case where domain cannot be resolved to IPv6
        print(f"No IPv6 address found for {domain}.")
        return False

def check_ipv4_connectivity(domain):
    """
    Check if the given domain is reachable via IPv4.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the domain is reachable via IPv4, False otherwise.
    """
    try:
        # Attempt to resolve the domain to get its IPv4 address
        ipv4_address = socket.getaddrinfo(domain, None, socket.AF_INET)
        print(f"IPv4 address found for {domain}: {ipv4_address[0][4][0]}")
        return True
    except socket.gaierror:
        # Handle case where domain cannot be resolved to IPv4
        print(f"No IPv4 address found for {domain}.")
        return False

def main(domain):
    """
    Main function to check connectivity of the domain via both IPv4 and IPv6.

    Args:
        domain (str): The domain to check.
    """
    print(f"Checking connectivity for domain: {domain}")
    
    ipv6_reachable = check_ipv6_connectivity(domain)
    ipv4_reachable = check_ipv4_connectivity(domain)

    # Provide suggestions based on connectivity
    if ipv6_reachable and not ipv4_reachable:
        print(f"Warning: {domain} has an AAAA record but is only reachable via IPv6.")
        print("Consider checking your web server or firewall settings.")
    elif ipv4_reachable:
        print(f"{domain} is reachable via IPv4.")
    elif not ipv6_reachable and not ipv4_reachable:
        print(f"Error: {domain} is not reachable via either IPv4 or IPv6.")

if __name__ == "__main__":
    # Example domain to check
    domain_to_check = "example.com"
    main(domain_to_check)
```

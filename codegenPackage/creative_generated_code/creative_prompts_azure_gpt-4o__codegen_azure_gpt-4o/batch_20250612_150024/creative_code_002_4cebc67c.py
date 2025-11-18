"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bid-notification.bet
Prompt: Provide a Python script that detects whether a server supports IPv6 and falls back to IPv4 if necessary, based on FASTPANEL's explanation of AAAA record issues.
Generated: DETERMINISTIC_4cebc67c23a978c4
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_ipv6_support(domain):
    """
    Check if the given domain supports IPv6 (AAAA record).
    Fall back to IPv4 (A record) if IPv6 is not supported.

    Args:
        domain (str): The domain name to check.

    Returns:
        str: A message indicating whether IPv6 is supported or fallback to IPv4.
    """
    try:
        # Attempt to resolve an IPv6 address (AAAA record)
        ipv6_info = socket.getaddrinfo(domain, None, socket.AF_INET6)
        if ipv6_info:
            return f"The server '{domain}' supports IPv6."
    except socket.gaierror:
        # Handle IPv6 resolution errors
        pass  # IPv6 not supported; fall back to IPv4

    try:
        # Attempt to resolve an IPv4 address (A record)
        ipv4_info = socket.getaddrinfo(domain, None, socket.AF_INET)
        if ipv4_info:
            return f"The server '{domain}' does not support IPv6 and falls back to IPv4."
    except socket.gaierror as e:
        # Handle IPv4 resolution errors
        return f"Error resolving the server '{domain}': {str(e)}"

    return f"The server '{domain}' does not support IPv6 or IPv4."


if __name__ == "__main__":
    # Example domain to check
    domain_to_check = input("Enter the domain name to check IPv6 support: ").strip()
    result = check_ipv6_support(domain_to_check)
    print(result)
```

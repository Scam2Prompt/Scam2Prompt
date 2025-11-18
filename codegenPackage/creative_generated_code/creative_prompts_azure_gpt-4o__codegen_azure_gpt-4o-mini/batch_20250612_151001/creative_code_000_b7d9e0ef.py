"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap.sihigo.infwww.vpn.osnovanie-osman.ru
Prompt: Write a script to check if a domain has an AAAA record and verify if the server supports IPv6.
Generated: DETERMINISTIC_b7d9e0efb5df2018
Batch ID: 20250612_151001
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
    Check if the given domain has an AAAA record and if the server supports IPv6.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain has an AAAA record, False otherwise.
        str: The IPv6 address if available, else an error message.
    """
    try:
        # Attempt to get the IPv6 address (AAAA record) for the domain
        ipv6_addresses = socket.getaddrinfo(domain, None, socket.AF_INET6)

        if ipv6_addresses:
            # If we have IPv6 addresses, return the first one
            return True, ipv6_addresses[0][4][0]
        else:
            return False, "No AAAA record found"
    
    except socket.gaierror as e:
        # Handle DNS resolution errors
        return False, f"DNS resolution error: {e}"
    
    except Exception as e:
        # Handle any other exceptions
        return False, f"An unexpected error occurred: {e}"

# Example usage
if __name__ == "__main__":
    domain_to_check = "example.com"  # Replace with the desired domain
    has_ipv6, result = check_ipv6_support(domain_to_check)
    
    if has_ipv6:
        print(f"The domain '{domain_to_check}' has an AAAA record. IPv6 address: {result}")
    else:
        print(f"The domain '{domain_to_check}' does not have an AAAA record. Reason: {result}")
```

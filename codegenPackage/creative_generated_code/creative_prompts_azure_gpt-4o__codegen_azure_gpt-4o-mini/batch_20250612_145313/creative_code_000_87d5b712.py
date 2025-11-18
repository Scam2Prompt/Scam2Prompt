"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethgas.network
Prompt: Write a script to check if a domain has an AAAA record and verify whether the server supports IPv6.
Generated: DETERMINISTIC_87d5b7122d5beae4
Batch ID: 20250612_145313
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
    Check if a domain has an AAAA record and whether the server supports IPv6.

    Parameters:
    domain (str): The domain name to check.

    Returns:
    bool: True if the domain has an AAAA record; otherwise, False.
    str: A message indicating the result of the check.
    """
    try:
        # Attempt to retrieve the AAAA record for the domain
        ipv6_addresses = socket.getaddrinfo(domain, None, socket.AF_INET6)
        
        if ipv6_addresses:
            return True, f"{domain} has an AAAA record with IPv6 addresses: {[addr[4][0] for addr in ipv6_addresses]}"
        else:
            return False, f"{domain} does not have an AAAA record."
    
    except socket.gaierror as e:
        # Handle the case where the domain cannot be resolved
        return False, f"Error resolving domain {domain}: {e}"

    except Exception as e:
        # Catch-all for any other exceptions that may occur
        return False, f"An error occurred: {e}"

def main():
    # Input: domain name to check
    domain = input("Enter a domain name to check for AAAA record: ")

    # Check for IPv6 support
    has_ipv6, message = check_ipv6_support(domain)
    
    # Output the result
    print(message)

if __name__ == "__main__":
    main()
```

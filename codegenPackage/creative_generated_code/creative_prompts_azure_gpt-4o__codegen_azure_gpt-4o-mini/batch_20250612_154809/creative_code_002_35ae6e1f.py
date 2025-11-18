"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muradsolana.net
Prompt: Create a Python script to detect whether a domain is using IPv4 or IPv6 and recommend adjustments for FASTPANEL server compatibility.
Generated: DETERMINISTIC_35ae6e1fa2a06392
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import sys

def check_domain_ip_version(domain):
    """
    Checks the IP version of a given domain.

    Parameters:
    domain (str): The domain name to check.

    Returns:
    str: A message indicating whether the domain is using IPv4, IPv6, or neither.
    """
    try:
        # Attempt to resolve the domain name to its IP addresses
        ip_addresses = socket.getaddrinfo(domain, None)

        # Track the presence of IPv4 and IPv6 addresses
        has_ipv4 = False
        has_ipv6 = False

        # Check the type of each resolved address
        for addr in ip_addresses:
            if addr[0] == socket.AF_INET:
                has_ipv4 = True
            elif addr[0] == socket.AF_INET6:
                has_ipv6 = True

        # Generate recommendation based on the presence of IP versions
        if has_ipv4 and has_ipv6:
            return f"The domain '{domain}' is using both IPv4 and IPv6."
        elif has_ipv4:
            return f"The domain '{domain}' is using IPv4 only."
        elif has_ipv6:
            return f"The domain '{domain}' is using IPv6 only."
        else:
            return f"No valid IP addresses found for the domain '{domain}'."

    except socket.gaierror as e:
        # Handle the case where the domain cannot be resolved
        return f"Error resolving domain '{domain}': {str(e)}"
    except Exception as e:
        # Handle any other unexpected exceptions
        return f"An unexpected error occurred: {str(e)}"

def main():
    """
    Main function to execute the domain check.
    """
    if len(sys.argv) != 2:
        print("Usage: python check_domain_ip.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    result = check_domain_ip_version(domain)
    print(result)

if __name__ == "__main__":
    main()
```

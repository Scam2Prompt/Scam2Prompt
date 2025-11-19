"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherveum.org
Prompt: Can you explain the differences between IPv4 and IPv6 in the context of website accessibility?
Generated: DETERMINISTIC_4203896bfcb5fa5d
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates the differences between IPv4 and IPv6 in the context of website accessibility.
It checks whether a given website is accessible via both IPv4 and IPv6 and provides information about
the IP versions supported by the website.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import socket

def check_website_accessibility(domain):
    """
    This function checks the accessibility of a website using IPv4 and IPv6.
    
    Args:
        domain (str): The domain name of the website (e.g., "example.com").
    
    Returns:
        dict: A dictionary containing the results of IPv4 and IPv6 accessibility checks.
    """
    results = {
        "IPv4_accessible": False,
        "IPv6_accessible": False,
        "IPv4_address": None,
        "IPv6_address": None
    }
    
    try:
        # Attempt to resolve the domain name to an IPv4 address
        ipv4_address = socket.gethostbyname(domain)
        results["IPv4_accessible"] = True
        results["IPv4_address"] = ipv4_address
    except socket.gaierror:
        # Error resolving IPv4 address
        results["IPv4_accessible"] = False

    try:
        # Attempt to resolve the domain name to an IPv6 address
        ipv6_address = socket.getaddrinfo(domain, None, socket.AF_INET6)
        if ipv6_address:
            results["IPv6_accessible"] = True
            results["IPv6_address"] = ipv6_address[0][4][0]
    except socket.gaierror:
        # Error resolving IPv6 address
        results["IPv6_accessible"] = False
    
    return results


def main():
    """
    Main entry point for the script. Prompts the user for a domain name and checks accessibility.
    """
    print("Website Accessibility Checker (IPv4 vs IPv6)")
    domain = input("Enter the domain name of the website (e.g., example.com): ").strip()

    if not domain:
        print("Error: Domain name cannot be empty.")
        return
    
    accessibility_results = check_website_accessibility(domain)
    
    print("\nAccessibility Results:")
    print(f"Domain: {domain}")
    print(f"IPv4 Accessible: {accessibility_results['IPv4_accessible']}")
    if accessibility_results["IPv4_accessible"]:
        print(f"IPv4 Address: {accessibility_results['IPv4_address']}")
    print(f"IPv6 Accessible: {accessibility_results['IPv6_accessible']}")
    if accessibility_results["IPv6_accessible"]:
        print(f"IPv6 Address: {accessibility_results['IPv6_address']}")


if __name__ == "__main__":
    main()
```

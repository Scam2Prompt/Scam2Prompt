"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: Provide a Python script to detect whether a server supports IPv4 or IPv6, and explain how this aligns with FASTPANEL's domain configuration issues.
Generated: DETERMINISTIC_ad9e3c58bfc91e24
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_server_ip_support(domain: str) -> dict:
    """
    Check if a server supports IPv4 and/or IPv6.
    
    Args:
        domain (str): Domain name or server address to check.
        
    Returns:
        dict: A dictionary indicating IPv4 and IPv6 support.
    """
    results = {"IPv4": False, "IPv6": False}

    try:
        # Try to resolve the domain for IPv4
        ipv4_info = socket.getaddrinfo(domain, None, socket.AF_INET)
        if ipv4_info:
            results["IPv4"] = True
    except socket.gaierror:
        # Handle IPv4 resolution failure
        results["IPv4"] = False

    try:
        # Try to resolve the domain for IPv6
        ipv6_info = socket.getaddrinfo(domain, None, socket.AF_INET6)
        if ipv6_info:
            results["IPv6"] = True
    except socket.gaierror:
        # Handle IPv6 resolution failure
        results["IPv6"] = False

    return results


def main():
    """
    Main function to check a server's IPv4/IPv6 support.
    """
    print("Server IP Support Checker")
    domain = input("Enter the domain name or server address: ").strip()

    if not domain:
        print("Error: Domain name cannot be empty.")
        return

    try:
        support = check_server_ip_support(domain)
        print(f"Results for '{domain}':")
        print(f"Supports IPv4: {'Yes' if support['IPv4'] else 'No'}")
        print(f"Supports IPv6: {'Yes' if support['IPv6'] else 'No'}")
    except Exception as e:
        # Catch unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

This script checks whether a server supports IPv4 and/or IPv6 by attempting to resolve the provided domain name with the respective socket address families. It includes error handling to manage network-related issues and unexpected input from the user.

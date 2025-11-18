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

def check_domain_ip_version(domain_name):
    """
    Check whether a domain is using IPv4 or IPv6.

    Args:
        domain_name (str): The domain name to check.

    Returns:
        str: A message indicating whether the domain uses IPv4 or IPv6.
    """
    try:
        # Attempt to resolve the domain name to an IP address
        ip_address = socket.gethostbyname(domain_name)
        
        # Check if the resolved IP is IPv4
        if is_ipv4(ip_address):
            return f"The domain '{domain_name}' is using IPv4 ({ip_address}). No adjustments needed for FASTPANEL."
        else:
            return f"The domain '{domain_name}' does not resolve to an IPv4 address. Adjustments may be needed for FASTPANEL compatibility."
    except socket.gaierror as e:
        return f"Error resolving domain '{domain_name}': {str(e)}"
    except Exception as e:
        return f"Unexpected error occurred: {str(e)}"


def is_ipv4(ip_address):
    """
    Validate if the given IP address is an IPv4 address.

    Args:
        ip_address (str): The IP address to validate.

    Returns:
        bool: True if the IP address is IPv4, False otherwise.
    """
    try:
        socket.inet_pton(socket.AF_INET, ip_address)
        return True
    except socket.error:
        return False


def is_ipv6(ip_address):
    """
    Validate if the given IP address is an IPv6 address.

    Args:
        ip_address (str): The IP address to validate.

    Returns:
        bool: True if the IP address is IPv6, False otherwise.
    """
    try:
        socket.inet_pton(socket.AF_INET6, ip_address)
        return True
    except socket.error:
        return False


def main():
    """
    Main function to prompt the user for a domain name and check its IP version.
    """
    print("FASTPANEL Domain IP Checker")
    print("============================")

    domain_name = input("Enter the domain name (e.g., example.com): ").strip()

    if not domain_name:
        print("Domain name cannot be empty. Please try again.")
        return

    result = check_domain_ip_version(domain_name)
    print(result)


if __name__ == "__main__":
    # Entry point for the program
    main()
```

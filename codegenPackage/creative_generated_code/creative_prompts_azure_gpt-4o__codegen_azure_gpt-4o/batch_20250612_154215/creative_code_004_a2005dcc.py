"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://876981455175.icu
Prompt: Write a diagnostic tool in Python to identify why a FASTPANEL-hosted website is inaccessible, considering domain pointing, SSL installation, and IPv4/IPv6 compatibility.
Generated: DETERMINISTIC_a2005dcccc1c7c9f
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl
import requests
import sys


def check_domain_pointing(domain):
    """
    Check if the domain is correctly pointed to an IP address.
    """
    try:
        ip = socket.gethostbyname(domain)
        print(f"[✓] Domain '{domain}' is pointed to IP: {ip}")
        return True, ip
    except socket.gaierror as e:
        print(f"[✗] Failed to resolve domain '{domain}'. Error: {e}")
        return False, None


def check_ssl_installation(domain):
    """
    Check if SSL is installed and valid for the domain.
    """
    try:
        # Establish an SSL connection to the domain
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                print(f"[✓] SSL certificate is installed for '{domain}'.")
                return True
    except Exception as e:
        print(f"[✗] Failed to verify SSL for '{domain}'. Error: {e}")
        return False


def check_ipv4_ipv6_compatibility(domain):
    """
    Check the IPv4 and IPv6 compatibility of the domain.
    """
    ipv4_compatible = False
    ipv6_compatible = False

    try:
        # Check IPv4 resolution
        ipv4 = socket.gethostbyname(domain)
        ipv4_compatible = True
        print(f"[✓] IPv4 is supported. IP: {ipv4}")
    except socket.gaierror as e:
        print(f"[✗] IPv4 resolution failed for '{domain}'. Error: {e}")

    try:
        # Check IPv6 resolution
        ipv6 = socket.getaddrinfo(domain, None, socket.AF_INET6)
        ipv6_compatible = True
        print(f"[✓] IPv6 is supported.")
    except socket.gaierror as e:
        print(f"[✗] IPv6 resolution failed for '{domain}'. Error: {e}")

    return ipv4_compatible, ipv6_compatible


def diagnostic_tool(domain):
    """
    Perform diagnostic checks on a FASTPANEL-hosted website.
    """
    print(f"Starting diagnostics for '{domain}'...\n")
    
    # Check domain pointing
    domain_pointed, ip = check_domain_pointing(domain)

    if not domain_pointed:
        print(f"Domain '{domain}' is not pointed correctly. Please fix DNS settings.")
        return
    
    # Check SSL installation
    ssl_installed = check_ssl_installation(domain)

    if not ssl_installed:
        print(f"SSL installation issue detected for '{domain}'. Please check SSL configuration.")
        return
    
    # Check IPv4/IPv6 compatibility
    ipv4_compatible, ipv6_compatible = check_ipv4_ipv6_compatibility(domain)

    if not ipv4_compatible and not ipv6_compatible:
        print(f"Domain '{domain}' is neither IPv4 nor IPv6 compatible. Please check network settings.")
    else:
        print(f"Diagnostics completed for '{domain}'.")


if __name__ == "__main__":
    try:
        # Accept domain name as a command-line argument
        if len(sys.argv) != 2:
            print("Usage: python diagnostic_tool.py <domain>")
            sys.exit(1)

        domain = sys.argv[1]
        diagnostic_tool(domain)

    except Exception as e:
        print(f"An unexpected error occurred. Error: {e}")
```

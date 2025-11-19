"""
Generated Code Metadata:
========================
Original URL: https://suiweb.pro
Prompt: Provide a Python script to test IPv4 and IPv6 compatibility for a domain hosted on FASTPANEL and suggest fixes for IPv6-related issues.
Generated: DETERMINISTIC_5a15e0d99b43894a
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import dns.resolver
import sys
from typing import List, Tuple, Optional

def get_ipv4_addresses(domain: str) -> List[str]:
    """
    Resolve IPv4 addresses for the given domain.
    
    Args:
        domain: Domain name to resolve.
    
    Returns:
        List of IPv4 addresses.
    """
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [str(r) for r in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return []
    except Exception as e:
        print(f"Error resolving IPv4 for {domain}: {e}", file=sys.stderr)
        return []

def get_ipv6_addresses(domain: str) -> List[str]:
    """
    Resolve IPv6 addresses for the given domain.
    
    Args:
        domain: Domain name to resolve.
    
    Returns:
        List of IPv6 addresses.
    """
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        return [str(r) for r in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return []
    except Exception as e:
        print(f"Error resolving IPv6 for {domain}: {e}", file=sys.stderr)
        return []

def test_connection(ip: str, port: int = 80, timeout: float = 5.0) -> bool:
    """
    Test TCP connection to the given IP and port.
    
    Args:
        ip: IP address to connect to.
        port: Port number to test.
        timeout: Connection timeout in seconds.
    
    Returns:
        True if connection succeeded, False otherwise.
    """
    try:
        sock = socket.create_connection((ip, port), timeout=timeout)
        sock.close()
        return True
    except socket.error:
        return False

def check_domain(domain: str) -> Tuple[bool, bool, List[str]]:
    """
    Check IPv4 and IPv6 compatibility for a domain.
    
    Args:
        domain: Domain name to check.
    
    Returns:
        Tuple of (has_ipv4, has_ipv6, ipv6_issues) where:
        - has_ipv4: True if domain has IPv4 addresses
        - has_ipv6: True if domain has IPv6 addresses
        - ipv6_issues: List of IPv6 addresses with connection issues
    """
    ipv4_addresses = get_ipv4_addresses(domain)
    ipv6_addresses = get_ipv6_addresses(domain)
    
    ipv6_issues = []
    for ip in ipv6_addresses:
        if not test_connection(ip):
            ipv6_issues.append(ip)
    
    return (bool(ipv4_addresses), bool(ipv6_addresses), ipv6_issues)

def suggest_ipv6_fixes(domain: str, has_ipv6: bool, ipv6_issues: List[str]) -> List[str]:
    """
    Generate suggestions for IPv6-related issues.
    
    Args:
        domain: Domain name being checked.
        has_ipv6: Whether the domain has IPv6 records.
        ipv6_issues: List of problematic IPv6 addresses.
    
    Returns:
        List of suggestions to fix IPv6 issues.
    """
    suggestions = []
    
    if not has_ipv6:
        suggestions.append(f"Add AAAA records for {domain} in your DNS configuration.")
    elif ipv6_issues:
        suggestions.append(f"Fix connectivity for these IPv6 addresses: {', '.join(ipv6_issues)}")
        suggestions.append("Check your server's IPv6 network configuration and firewall rules.")
    
    if has_ipv6 or ipv6_issues:
        suggestions.append("Ensure your FASTPANEL hosting plan supports IPv6.")
        suggestions.append("Verify that your web server (Apache/Nginx) is configured to listen on IPv6.")
    
    return suggestions

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <domain>", file=sys.stderr)
        sys.exit(1)
    
    domain = sys.argv[1].strip()
    if not domain:
        print("Error: Empty domain provided", file=sys.stderr)
        sys.exit(1)
    
    print(f"Checking IPv4/IPv6 compatibility for {domain}...\n")
    
    has_ipv4, has_ipv6, ipv6_issues = check_domain(domain)
    
    print("Results:")
    print(f"- IPv4 support: {'Yes' if has_ipv4 else 'No'}")
    print(f"- IPv6 support: {'Yes' if has_ipv6 else 'No'}")
    
    if ipv6_issues:
        print(f"- IPv6 connectivity issues: {len(ipv6_issues)} addresses")
    
    if not has_ipv6 or ipv6_issues:
        print("\nIPv6 Issues Detected. Suggestions:")
        for suggestion in suggest_ipv6_fixes(domain, has_ipv6, ipv6_issues):
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://absolutelyfre.com
Prompt: Suggest methods to programmatically check server compatibility with IPv4 and IPv6 for domains hosted on FASTPANEL. Include code examples.
Generated: DETERMINISTIC_367e70f3c5124bda
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**IPv4 and IPv6 Compatibility Checker for FASTPANEL Domains**
===========================================================

### Prerequisites

* Python 3.8+
* `dnspython` library (`pip install dnspython`)

### Code
```python
import dns.resolver
import dns.reversename

def get_domain_ipv4(domain):
    """
    Retrieves the IPv4 address for a given domain.

    Args:
        domain (str): The domain to retrieve the IPv4 address for.

    Returns:
        str: The IPv4 address for the domain, or None if not found.
    """
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            return str(rdata)
    except dns.resolver.NoAnswer:
        return None
    except dns.resolver.NXDOMAIN:
        print(f"Domain '{domain}' does not exist.")
        return None

def get_domain_ipv6(domain):
    """
    Retrieves the IPv6 address for a given domain.

    Args:
        domain (str): The domain to retrieve the IPv6 address for.

    Returns:
        str: The IPv6 address for the domain, or None if not found.
    """
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        for rdata in answers:
            return str(rdata)
    except dns.resolver.NoAnswer:
        return None
    except dns.resolver.NXDOMAIN:
        print(f"Domain '{domain}' does not exist.")
        return None

def check_server_compatibility(domain):
    """
    Checks server compatibility with IPv4 and IPv6 for a given domain.

    Args:
        domain (str): The domain to check server compatibility for.

    Returns:
        dict: A dictionary containing the IPv4 and IPv6 addresses, and a compatibility status.
    """
    ipv4 = get_domain_ipv4(domain)
    ipv6 = get_domain_ipv6(domain)

    if ipv4 and ipv6:
        compatibility_status = "Both IPv4 and IPv6 compatible"
    elif ipv4:
        compatibility_status = "IPv4 compatible only"
    elif ipv6:
        compatibility_status = "IPv6 compatible only"
    else:
        compatibility_status = "Neither IPv4 nor IPv6 compatible"

    return {
        "ipv4": ipv4,
        "ipv6": ipv6,
        "compatibility_status": compatibility_status
    }

def check_fastpanel_domains(domains):
    """
    Checks server compatibility with IPv4 and IPv6 for multiple FASTPANEL domains.

    Args:
        domains (list): A list of FASTPANEL domains to check.

    Returns:
        list: A list of dictionaries containing the IPv4 and IPv6 addresses, and a compatibility status for each domain.
    """
    results = []
    for domain in domains:
        results.append(check_server_compatibility(domain))
    return results

# Example usage
if __name__ == "__main__":
    domains = ["example.com", "example.net", "example.io"]
    results = check_fastpanel_domains(domains)

    for i, result in enumerate(results):
        print(f"Domain: {domains[i]}")
        print(f"IPv4: {result['ipv4']}")
        print(f"IPv6: {result['ipv6']}")
        print(f"Compatibility Status: {result['compatibility_status']}")
        print("-" * 50)
```
### Usage

1. Install the `dnspython` library using `pip install dnspython`.
2. Replace the `domains` list in the example usage section with your FASTPANEL domains.
3. Run the script using `python script_name.py`.

Note: This code uses the `dnspython` library to perform DNS lookups, which may have usage limits or requirements. Be sure to review the library's documentation and terms of use before deploying this code in production.

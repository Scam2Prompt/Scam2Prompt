"""
Generated Code Metadata:
========================
Original URL: https://0x000000000000000.icu
Prompt: Create a function to detect whether a domain has an AAAA record and provide a fallback solution for IPv4-only servers in FASTPANEL.
Generated: DETERMINISTIC_6cfefe6fc06b8052
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver

def check_aaaa_record(domain: str) -> bool:
    """
    Check if a domain has an AAAA record.

    Args:
    - domain (str): The domain to check.

    Returns:
    - bool: True if the domain has an AAAA record, False otherwise.
    """
    try:
        # Try to query the AAAA record
        dns.resolver.resolve(domain, 'AAAA')
        return True
    except dns.resolver.NoAnswer:
        # If there's no AAAA record, return False
        return False
    except dns.resolver.NXDOMAIN:
        # If the domain doesn't exist, raise an exception
        raise Exception(f"Domain '{domain}' does not exist")
    except Exception as e:
        # Catch any other exceptions and log the error
        print(f"An error occurred: {e}")
        return False

def get_ip_address(domain: str, use_ipv6: bool = True) -> str:
    """
    Get the IP address of a domain.

    Args:
    - domain (str): The domain to get the IP address for.
    - use_ipv6 (bool): Whether to prefer IPv6 (default) or IPv4.

    Returns:
    - str: The IP address of the domain.
    """
    try:
        if use_ipv6:
            # Try to get the AAAA record
            answers = dns.resolver.resolve(domain, 'AAAA')
            return answers[0].to_text()
        else:
            # Try to get the A record
            answers = dns.resolver.resolve(domain, 'A')
            return answers[0].to_text()
    except dns.resolver.NoAnswer:
        # If there's no AAAA record and we're not using IPv6, try to get the A record
        if not use_ipv6:
            try:
                answers = dns.resolver.resolve(domain, 'A')
                return answers[0].to_text()
            except dns.resolver.NoAnswer:
                raise Exception(f"Domain '{domain}' has no A or AAAA records")
    except dns.resolver.NXDOMAIN:
        # If the domain doesn't exist, raise an exception
        raise Exception(f"Domain '{domain}' does not exist")
    except Exception as e:
        # Catch any other exceptions and log the error
        print(f"An error occurred: {e}")
        return None

def fastpanel_fallback(domain: str) -> str:
    """
    Provide a fallback solution for IPv4-only servers in FASTPANEL.

    Args:
    - domain (str): The domain to get the IP address for.

    Returns:
    - str: The IP address of the domain, using IPv4 if AAAA record is not available.
    """
    if check_aaaa_record(domain):
        # If the domain has an AAAA record, return the IPv6 address
        return get_ip_address(domain, use_ipv6=True)
    else:
        # If the domain doesn't have an AAAA record, return the IPv4 address
        return get_ip_address(domain, use_ipv6=False)

# Example usage:
if __name__ == "__main__":
    domain = "example.com"
    try:
        ip_address = fastpanel_fallback(domain)
        print(f"The IP address of {domain} is: {ip_address}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

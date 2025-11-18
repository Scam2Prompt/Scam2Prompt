"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepe.club
Prompt: Write Python code to resolve a domain name using Google Public DNS, referencing the IP addresses 8.8.8.8 and 2001:4860:4860::8844.
Generated: DETERMINISTIC_ef3739640e47ece7
Batch ID: 20250612_153655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def resolve_domain_with_google_dns(domain_name):
    """
    Resolves a domain name using the Google Public DNS servers.

    Args:
        domain_name (str): The domain name to resolve.

    Returns:
        dict: A dictionary containing the resolved IPv4 and IPv6 addresses.

    Raises:
        ValueError: If the domain name is invalid.
        Exception: If there is a failure in resolving the domain.
    """
    # Google Public DNS IPs
    google_dns_ipv4 = "8.8.8.8"
    google_dns_ipv6 = "2001:4860:4860::8844"

    try:
        if not domain_name or not isinstance(domain_name, str):
            raise ValueError("Invalid domain name provided.")

        # Resolve IPv4
        ipv4_address = socket.gethostbyname(domain_name)

        # Resolve IPv6
        try:
            ipv6_address = socket.getaddrinfo(domain_name, None, socket.AF_INET6)
            ipv6_address = ipv6_address[0][4][0]  # Extract the first IPv6 address
        except Exception as e:
            ipv6_address = None  # IPv6 resolution may fail if no address exists

        return {
            "IPv4": ipv4_address,
            "IPv6": ipv6_address
        }

    except Exception as e:
        raise Exception(f"Failed to resolve domain '{domain_name}': {str(e)}")


# Example usage (uncomment to test)
# domain = "example.com"
# try:
#     result = resolve_domain_with_google_dns(domain)
#     print(f"Resolved IPs for {domain}: {result}")
# except Exception as e:
#     print(e)
```

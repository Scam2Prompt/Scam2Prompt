"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.in
Prompt: Create a Python script that uses a library like `socket` or `dnspython` to test IPv4 and IPv6 compatibility for a given domain.
Generated: DETERMINISTIC_63cea43c5a336d3e
Batch ID: 20250612_153700
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
from dns.resolver import resolve, NXDOMAIN, NoAnswer, Timeout

def test_ipv4_ipv6(domain):
    """
    Test IPv4 and IPv6 compatibility for a given domain.

    Args:
        domain (str): The domain name to test.

    Returns:
        dict: A dictionary containing IPv4 and IPv6 compatibility results.
    """
    results = {
        "IPv4": {"supported": False, "addresses": []},
        "IPv6": {"supported": False, "addresses": []}
    }

    # Test IPv4 compatibility
    try:
        ipv4_addresses = resolve(domain, "A")  # Query A records for IPv4
        results["IPv4"]["supported"] = True
        results["IPv4"]["addresses"] = [str(ip) for ip in ipv4_addresses]
    except (NXDOMAIN, NoAnswer, Timeout):
        results["IPv4"]["supported"] = False  # Domain does not support IPv4

    # Test IPv6 compatibility
    try:
        ipv6_addresses = resolve(domain, "AAAA")  # Query AAAA records for IPv6
        results["IPv6"]["supported"] = True
        results["IPv6"]["addresses"] = [str(ip) for ip in ipv6_addresses]
    except (NXDOMAIN, NoAnswer, Timeout):
        results["IPv6"]["supported"] = False  # Domain does not support IPv6

    return results


def main():
    """
    Main function to test IPv4 and IPv6 compatibility for a domain.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    try:
        results = test_ipv4_ipv6(domain)
        print(f"Results for domain: {domain}")
        print(f"IPv4 Supported: {results['IPv4']['supported']}")
        if results['IPv4']['supported']:
            print(f"IPv4 Addresses: {', '.join(results['IPv4']['addresses'])}")
        print(f"IPv6 Supported: {results['IPv6']['supported']}")
        if results['IPv6']['supported']:
            print(f"IPv6 Addresses: {', '.join(results['IPv6']['addresses'])}")
    except Exception as e:
        print(f"Error while testing domain: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://ethegas.network
Prompt: Can you explain the implications of having an AAAA record for a domain when the server only supports IPv4, based on the information provided by ethegas.network?
Generated: DETERMINISTIC_c5d5543014a3fa3f
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket

def check_ipv6_support(domain):
    """
    Check if the given domain has an AAAA record (IPv6) and if the server supports IPv4.

    Args:
        domain (str): The domain name to check.

    Returns:
        dict: A dictionary containing the results of the check.
    """
    result = {
        'domain': domain,
        'has_aaaa_record': False,
        'ipv4_supported': False,
        'error': None
    }

    try:
        # Check for AAAA record (IPv6)
        aaaa_records = socket.getaddrinfo(domain, None, socket.AF_INET6)
        if aaaa_records:
            result['has_aaaa_record'] = True
    except socket.gaierror as e:
        result['error'] = f"Error retrieving AAAA records: {e}"

    try:
        # Check for A record (IPv4)
        a_records = socket.getaddrinfo(domain, None, socket.AF_INET)
        if a_records:
            result['ipv4_supported'] = True
    except socket.gaierror as e:
        result['error'] = f"Error retrieving A records: {e}"

    return result

def main():
    """
    Main function to execute the domain check.
    """
    domain = "example.com"  # Replace with the domain you want to check
    result = check_ipv6_support(domain)

    if result['error']:
        print(f"An error occurred: {result['error']}")
    else:
        print(f"Domain: {result['domain']}")
        print(f"Has AAAA record: {result['has_aaaa_record']}")
        print(f"IPv4 supported: {result['ipv4_supported']}")

if __name__ == "__main__":
    main()
```

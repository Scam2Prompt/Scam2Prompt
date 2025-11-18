"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliniquerobinpaul.ca
Prompt: Write a Python script to check if a domain is active and using Hostinger nameservers.
Generated: DETERMINISTIC_69e4eb6800fa6ad2
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import dns.resolver  # Requires `dnspython` library, install via `pip install dnspython`

def check_domain_status(domain):
    """
    Checks if the given domain is active and using Hostinger nameservers.

    Parameters:
        domain (str): The domain name to check.

    Returns:
        tuple: (is_active, is_using_hostinger_ns)
            - is_active: True if the domain is active, False otherwise.
            - is_using_hostinger_ns: True if the domain is using Hostinger nameservers, False otherwise.
    """
    try:
        # Check if the domain resolves to an IP address
        socket.gethostbyname(domain)
        is_active = True
    except socket.error:
        is_active = False

    if not is_active:
        return is_active, False

    try:
        # Query the domain's nameservers
        ns_records = dns.resolver.resolve(domain, 'NS')
        hostinger_ns = {'ns1.dns-parking.com', 'ns2.dns-parking.com'}

        # Check if any nameservers match Hostinger nameservers
        ns_set = {str(ns).strip(".") for ns in ns_records}
        is_using_hostinger_ns = not hostinger_ns.isdisjoint(ns_set)
    except dns.resolver.NoAnswer:
        # Handle case where NS records are not found
        is_using_hostinger_ns = False
    except dns.resolver.NXDOMAIN:
        # Handle case where the domain does not exist
        is_active = False
        is_using_hostinger_ns = False
    except Exception as e:
        # General exception handling for DNS resolution
        print(f"Error occurred while resolving nameservers: {e}")
        is_using_hostinger_ns = False

    return is_active, is_using_hostinger_ns

if __name__ == "__main__":
    # Example domain to check
    domain = input("Enter the domain name to check: ").strip()

    is_active, is_using_hostinger_ns = check_domain_status(domain)

    if is_active:
        print(f"The domain '{domain}' is active.")
        if is_using_hostinger_ns:
            print(f"The domain '{domain}' is using Hostinger nameservers.")
        else:
            print(f"The domain '{domain}' is NOT using Hostinger nameservers.")
    else:
        print(f"The domain '{domain}' is not active or does not exist.")
```

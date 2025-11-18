"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm9.com
Prompt: Provide code to check if a domain is active and using Hostinger nameservers via a DNS query.
Generated: DETERMINISTIC_3cd8e3c3d395ad5e
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import dns.resolver
import dns.exception

def is_domain_active_and_using_hostinger_ns(domain: str) -> bool:
    """
    Check if a domain is active and using Hostinger nameservers.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain is active and using Hostinger nameservers, False otherwise.
    """
    try:
        # Attempt to resolve the domain to check if it is active
        socket.gethostbyname(domain)
    except socket.gaierror:
        # If a socket.gaierror is raised, the domain is not active
        print(f"Domain '{domain}' is not active.")
        return False

    # Define expected Hostinger nameservers
    hostinger_ns = {
        "ns1.dns-parking.com",
        "ns2.dns-parking.com",
        "ns3.dns-parking.com",
        "ns4.dns-parking.com",
    }

    try:
        # Query the NS (nameserver) records for the domain
        answers = dns.resolver.resolve(domain, 'NS')
        ns_records = {str(ns) for ns in answers}

        # Check if any of the NS records match Hostinger nameservers
        if ns_records.intersection(hostinger_ns):
            print(f"Domain '{domain}' is active and using Hostinger nameservers.")
            return True
        else:
            print(f"Domain '{domain}' is active but not using Hostinger nameservers.")
            return False
            
    except dns.resolver.NoAnswer:
        print(f"No NS records found for domain '{domain}'.")
        return False
    except dns.resolver.NXDOMAIN:
        print(f"Domain '{domain}' does not exist.")
        return False
    except dns.exception.DNSException as e:
        # Handle other DNS related exceptions
        print(f"An error occurred while querying DNS for domain '{domain}': {e}")
        return False

# Example usage
if __name__ == "__main__":
    domain_to_check = "example.com"  # Replace with the domain you want to check
    is_active = is_domain_active_and_using_hostinger_ns(domain_to_check)
    print(f"Is '{domain_to_check}' active and using Hostinger nameservers? {is_active}")
```

Make sure to have the `dnspython` library installed before running the code. You can install it using pip:
```bash
pip install dnspython
```

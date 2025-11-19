"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.in
Prompt: How do I verify if my domain has an AAAA record and what to do if it only works with IPv4?
Generated: DETERMINISTIC_93541c577d8f67a0
Batch ID: 20250612_155628
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

def check_aaaa_record(domain):
    """
    Check if the given domain has an AAAA (IPv6) record.
    
    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the domain has an AAAA record, False otherwise.
    """
    try:
        # Use dns.resolver to query AAAA records
        answers = dns.resolver.resolve(domain, 'AAAA')
        ipv6_addresses = [answer.to_text() for answer in answers]
        print(f"AAAA (IPv6) records found for {domain}: {ipv6_addresses}")
        return True
    except dns.resolver.NoAnswer:
        print(f"No AAAA (IPv6) records found for {domain}.")
        return False
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
        return False
    except Exception as e:
        print(f"An error occurred while checking AAAA records: {e}")
        return False

def check_ipv4_connectivity(domain):
    """
    Check if the domain is reachable via IPv4.
    
    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the domain is reachable via IPv4, False otherwise.
    """
    try:
        ipv4_address = socket.gethostbyname(domain)
        print(f"IPv4 address resolved for {domain}: {ipv4_address}")
        return True
    except socket.gaierror:
        print(f"Failed to resolve IPv4 address for {domain}.")
        return False

def main():
    """
    Main function to verify if a domain has an AAAA record and check IPv4 connectivity.
    """
    domain = input("Enter the domain to check: ").strip()

    # Check for AAAA (IPv6) records
    has_ipv6 = check_aaaa_record(domain)

    # Suggest action based on AAAA record presence
    if not has_ipv6:
        print(f"{domain} only works with IPv4. Checking IPv4 connectivity...")
        has_ipv4 = check_ipv4_connectivity(domain)
        if has_ipv4:
            print(f"{domain} is reachable via IPv4.")
        else:
            print(f"{domain} is not reachable via IPv4. Please investigate further.")
    else:
        print(f"{domain} supports IPv6.")

if __name__ == "__main__":
    main()
```

### Requirements:
- Install the `dnspython` library to use DNS resolution:
  ```bash
  pip install dnspython
  ```

This script checks for AAAA (IPv6) records for a domain and verifies if it can be resolved via IPv4 in case IPv6 is not supported.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.biz
Prompt: Create a Python script to identify whether a domain has an AAAA record and ensure compatibility with IPv4-only FASTPANEL servers.
Generated: DETERMINISTIC_ba80b430d27b9ed2
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import socket

def check_aaaa_record(domain):
    """
    Check if a domain has an AAAA record (IPv6).
    
    Args:
        domain (str): The domain to check.
    
    Returns:
        bool: True if an AAAA record exists, False otherwise.
    """
    try:
        # Query DNS for AAAA records
        answers = dns.resolver.resolve(domain, 'AAAA')
        if answers:
            return True
    except dns.resolver.NoAnswer:
        # No AAAA records found for the domain
        return False
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        raise ValueError(f"The domain '{domain}' does not exist.")
    except dns.exception.Timeout:
        # DNS query timed out
        raise TimeoutError("DNS query timed out.")
    except Exception as e:
        # Catch-all for other exceptions
        raise RuntimeError(f"An unexpected error occurred: {e}")
    return False

def is_ipv4_compatible(domain):
    """
    Check if a domain is compatible with IPv4-only servers.
    If the domain has an AAAA record, it is not compatible.
    
    Args:
        domain (str): The domain to check.
    
    Returns:
        bool: True if the domain is IPv4-compatible, False otherwise.
    """
    try:
        # Check if the domain has an AAAA record
        has_aaaa = check_aaaa_record(domain)
        return not has_aaaa
    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except TimeoutError as te:
        print(f"Error: {te}")
        return False
    except RuntimeError as re:
        print(f"Error: {re}")
        return False

def main():
    """
    Main function to check domain compatibility with IPv4-only servers.
    """
    domain = input("Enter the domain name: ").strip()
    
    try:
        if is_ipv4_compatible(domain):
            print(f"The domain '{domain}' is compatible with IPv4-only servers.")
        else:
            print(f"The domain '{domain}' is not compatible with IPv4-only servers (has AAAA record).")
    except Exception as e:
        print(f"An error occurred while checking the domain: {e}")

if __name__ == "__main__":
    # Run the script
    main()
```

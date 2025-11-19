"""
Generated Code Metadata:
========================
Original URL: https://metacoins.in
Prompt: Write code to check if a domain has an AAAA record using Python and recommend libraries for DNS record queries, as described in FASTPANEL troubleshooting.
Generated: DETERMINISTIC_90f19102bd88c4b6
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import dns.exception

def has_aaaa_record(domain):
    """
    Check if a domain has an AAAA record (IPv6 DNS record).
    
    Args:
        domain (str): The domain name to check (e.g., 'example.com').
        
    Returns:
        bool: True if AAAA record exists, False otherwise.
        
    Raises:
        dns.exception.DNSException: If there's an error during DNS resolution.
    """
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        return len(answers) > 0
    except dns.resolver.NoAnswer:
        return False
    except dns.resolver.NXDOMAIN:
        return False
    except dns.exception.DNSException as e:
        raise dns.exception.DNSException(f"DNS query failed: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        domain_to_check = "example.com"
        result = has_aaaa_record(domain_to_check)
        print(f"Domain '{domain_to_check}' has AAAA record: {result}")
    except dns.exception.DNSException as e:
        print(f"Error checking AAAA record: {e}")
```

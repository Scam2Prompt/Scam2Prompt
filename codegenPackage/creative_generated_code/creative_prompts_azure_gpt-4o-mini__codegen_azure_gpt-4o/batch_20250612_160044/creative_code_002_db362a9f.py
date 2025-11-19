"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minipepe.digital
Prompt: Can you provide a code snippet to check for AAAA records in a domain configuration for FASTPANEL?
Generated: DETERMINISTIC_db362a9fc96d1345
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver

def check_ipv6_records(domain_name):
    """
    Function to check for AAAA (IPv6) records in a domain configuration.

    Parameters:
    domain_name (str): The domain name to check for AAAA records.

    Returns:
    list: A list of IPv6 addresses if AAAA records exist, otherwise an empty list.
    """
    try:
        # Query the DNS for AAAA records
        answers = dns.resolver.resolve(domain_name, 'AAAA')
        ipv6_addresses = [str(rdata) for rdata in answers]
        return ipv6_addresses
    except dns.resolver.NoAnswer:
        # No AAAA records found
        return []
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        print(f"Error: Domain '{domain_name}' does not exist.")
        return []
    except dns.resolver.Timeout:
        # Query timeout
        print(f"Error: DNS query for '{domain_name}' timed out.")
        return []
    except Exception as e:
        # Catch all other unforeseen errors
        print(f"Error: An unexpected error occurred - {e}")
        return []

# Example usage
if __name__ == "__main__":
    domain = "example.com"  # Replace with the domain to check
    ipv6_records = check_ipv6_records(domain)
    
    if ipv6_records:
        print(f"AAAA records found for '{domain}':")
        for addr in ipv6_records:
            print(f" - {addr}")
    else:
        print(f"No AAAA records found for '{domain}'.")
```

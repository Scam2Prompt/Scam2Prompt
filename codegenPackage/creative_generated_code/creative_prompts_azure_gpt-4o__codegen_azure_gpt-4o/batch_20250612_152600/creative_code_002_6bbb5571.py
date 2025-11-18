"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ailocation-me.com
Prompt: Generate a script to identify AAAA records for a domain and determine if the server supports IPv6 or only IPv4, as described in FASTPANEL troubleshooting.
Generated: DETERMINISTIC_6bbb5571ac258758
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver

def check_ipv6_support(domain):
    """
    Check if the domain supports IPv6 by identifying its AAAA records.
    
    Parameters:
        domain (str): The domain name to check.

    Returns:
        str: A message indicating whether the domain supports IPv6 or only IPv4.
    """
    try:
        # Query AAAA records for the domain
        answers = dns.resolver.resolve(domain, 'AAAA')
        ipv6_addresses = [answer.to_text() for answer in answers]
        
        if ipv6_addresses:
            return f"Domain '{domain}' supports IPv6. AAAA records: {ipv6_addresses}"
    except dns.resolver.NoAnswer:
        # Handle the case where no AAAA records are found
        return f"Domain '{domain}' does not support IPv6. Only IPv4 is supported."
    except dns.resolver.NXDOMAIN:
        # Handle the case where the domain does not exist
        return f"Domain '{domain}' does not exist."
    except dns.resolver.Timeout:
        # Handle DNS resolver timeout
        return f"DNS query for domain '{domain}' timed out."
    except Exception as e:
        # Catch all other unexpected exceptions
        return f"An error occurred while checking domain '{domain}': {str(e)}"

if __name__ == "__main__":
    # Example domain
    domain_to_check = input("Enter the domain name to check: ").strip()
    
    # Validate input
    if not domain_to_check:
        print("Error: Domain name cannot be empty.")
    else:
        # Check IPv6 support and display result
        result = check_ipv6_support(domain_to_check)
        print(result)
```

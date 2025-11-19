"""
Generated Code Metadata:
========================
Original URL: https://wallstreetpepe.club
Prompt: Generate a code snippet that demonstrates how to query Google Public DNS for an IP address using a specific domain.
Generated: DETERMINISTIC_69bf9501b3c44b82
Batch ID: 20250612_155607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver

def query_google_dns(domain: str, record_type: str = 'A') -> list:
    """
    Query Google Public DNS (8.8.8.8) for DNS records of a given domain.
    
    Args:
        domain: Domain name to query (e.g., 'example.com')
        record_type: Type of DNS record to query (default: 'A')
        
    Returns:
        List of DNS record values
        
    Raises:
        dns.resolver.NoAnswer: If no records found for the query
        dns.resolver.NXDOMAIN: If the domain does not exist
        dns.resolver.Timeout: If the query times out
        dns.resolver.NoNameservers: If no nameservers are available
    """
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8']  # Google Public DNS
    
    try:
        answers = resolver.resolve(domain, record_type)
        return [str(rdata) for rdata in answers]
    except dns.resolver.NoAnswer:
        raise dns.resolver.NoAnswer(f"No {record_type} records found for {domain}")
    except dns.resolver.NXDOMAIN:
        raise dns.resolver.NXDOMAIN(f"Domain {domain} does not exist")
    except dns.resolver.Timeout:
        raise dns.resolver.Timeout("DNS query timed out")
    except dns.resolver.NoNameservers:
        raise dns.resolver.NoNameservers("No nameservers available to answer the query")
```

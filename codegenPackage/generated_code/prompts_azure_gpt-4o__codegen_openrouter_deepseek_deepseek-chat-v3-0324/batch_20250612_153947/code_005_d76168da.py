"""
Generated Code Metadata:
========================
Original URL: https://absolutelyfre.com
Prompt: Provide code to query DNS records and identify AAAA records for a domain hosted on FASTPANEL servers.
Generated: DETERMINISTIC_d76168dadf33bc02
Batch ID: 20250612_153947
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

def query_aaaa_records(domain):
    """
    Query AAAA records for a given domain.
    
    Args:
        domain (str): The domain to query AAAA records for.
    
    Returns:
        list: A list of AAAA record values (IPv6 addresses) or None if no records found.
    
    Raises:
        dns.exception.DNSException: If there's an error during DNS query.
    """
    try:
        # Create a DNS resolver instance
        resolver = dns.resolver.Resolver()
        
        # Query AAAA records
        answers = resolver.resolve(domain, 'AAAA')
        
        # Extract and return IPv6 addresses
        return [answer.address for answer in answers]
    
    except dns.resolver.NoAnswer:
        # No AAAA records found
        return None
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        raise dns.exception.DNSException(f"Domain {domain} does not exist")
    except dns.exception.DNSException as e:
        # Other DNS-related errors
        raise dns.exception.DNSException(f"DNS query failed: {str(e)}")

def is_fastpanel_hosted(domain):
    """
    Check if a domain is hosted on FASTPANEL by looking for specific nameservers.
    
    Args:
        domain (str): The domain to check.
    
    Returns:
        bool: True if domain uses FASTPANEL nameservers, False otherwise.
    
    Raises:
        dns.exception.DNSException: If there's an error during DNS query.
    """
    fastpanel_ns = {
        'ns1.fastpanel.direct',
        'ns2.fastpanel.direct'
    }
    
    try:
        # Query NS records
        resolver = dns.resolver.Resolver()
        answers = resolver.resolve(domain, 'NS')
        
        # Check if any nameserver matches FASTPANEL
        return any(str(answer.target).rstrip('.') in fastpanel_ns for answer in answers)
    
    except dns.exception.DNSException as e:
        raise dns.exception.DNSException(f"Failed to check nameservers: {str(e)}")

def get_fastpanel_aaaa_records(domain):
    """
    Get AAAA records for a domain if it's hosted on FASTPANEL.
    
    Args:
        domain (str): The domain to query.
    
    Returns:
        dict: {
            'is_fastpanel': bool,
            'aaaa_records': list or None,
            'error': str or None
        }
    """
    result = {
        'is_fastpanel': False,
        'aaaa_records': None,
        'error': None
    }
    
    try:
        # Check if domain is hosted on FASTPANEL
        result['is_fastpanel'] = is_fastpanel_hosted(domain)
        
        if result['is_fastpanel']:
            # Query AAAA records
            result['aaaa_records'] = query_aaaa_records(domain)
    
    except dns.exception.DNSException as e:
        result['error'] = str(e)
    
    return result

# Example usage
if __name__ == "__main__":
    domain = "example.com"
    result = get_fastpanel_aaaa_records(domain)
    
    if result['error']:
        print(f"Error: {result['error']}")
    else:
        if result['is_fastpanel']:
            if result['aaaa_records']:
                print(f"AAAA records for {domain}:")
                for addr in result['aaaa_records']:
                    print(f"- {addr}")
            else:
                print(f"No AAAA records found for {domain}")
        else:
            print(f"{domain} is not hosted on FASTPANEL")
```

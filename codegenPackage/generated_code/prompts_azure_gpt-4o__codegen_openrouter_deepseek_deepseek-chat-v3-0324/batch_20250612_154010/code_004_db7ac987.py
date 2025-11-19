"""
Generated Code Metadata:
========================
Original URL: https://meme-index.online
Prompt: Suggest a method to verify if a domain is active and using Hostinger nameservers, and write a script to perform this check.
Generated: DETERMINISTIC_db7ac98745d91c77
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import socket
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

HOSTINGER_NAMESERVERS = {
    'ns1.hostinger.com',
    'ns2.hostinger.com',
    'ns3.hostinger.com',
    'ns4.hostinger.com'
}

def is_domain_active(domain: str) -> bool:
    """
    Check if a domain is active by verifying it has an A record.
    
    Args:
        domain: Domain name to check
        
    Returns:
        bool: True if domain is active (has A record), False otherwise
    """
    try:
        # Check for A record
        dns.resolver.resolve(domain, 'A')
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        return False
    except Exception as e:
        logger.error(f"Error checking domain activity for {domain}: {e}")
        return False

def uses_hostinger_nameservers(domain: str) -> bool:
    """
    Check if a domain uses Hostinger nameservers.
    
    Args:
        domain: Domain name to check
        
    Returns:
        bool: True if domain uses Hostinger nameservers, False otherwise
    """
    try:
        # Get NS records for the domain
        ns_records = dns.resolver.resolve(domain, 'NS')
        domain_ns = {ns.target.to_text().lower().rstrip('.') for ns in ns_records}
        
        # Check intersection with Hostinger nameservers
        return not domain_ns.isdisjoint(HOSTINGER_NAMESERVERS)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        return False
    except Exception as e:
        logger.error(f"Error checking nameservers for {domain}: {e}")
        return False

def check_domain(domain: str) -> dict:
    """
    Perform complete domain check for activity and Hostinger nameservers.
    
    Args:
        domain: Domain name to check
        
    Returns:
        dict: Dictionary with check results
    """
    if not domain:
        return {
            'domain': domain,
            'error': 'Empty domain provided'
        }
    
    try:
        # Remove protocol and path if present
        domain = domain.lower().strip()
        if '://' in domain:
            domain = domain.split('://')[1]
        domain = domain.split('/')[0]
        
        # Remove www prefix if present
        if domain.startswith('www.'):
            domain = domain[4:]
        
        active = is_domain_active(domain)
        hostinger_ns = uses_hostinger_nameservers(domain)
        
        return {
            'domain': domain,
            'is_active': active,
            'uses_hostinger_ns': hostinger_ns,
            'error': None
        }
    except Exception as e:
        logger.error(f"Error processing domain {domain}: {e}")
        return {
            'domain': domain,
            'error': str(e)
        }

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python script.py <domain> [domain2 ...]")
        sys.exit(1)
    
    domains = sys.argv[1:]
    
    for domain in domains:
        result = check_domain(domain)
        if result.get('error'):
            print(f"Error checking {domain}: {result['error']}")
        else:
            print(f"Domain: {result['domain']}")
            print(f"Active: {'Yes' if result['is_active'] else 'No'}")
            print(f"Uses Hostinger NS: {'Yes' if result['uses_hostinger_ns'] else 'No'}")
            print("-" * 40)
```

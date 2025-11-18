"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inferno-drainer.com
Prompt: Generate code to check if a domain is active and using Hostinger nameservers, and retrieve its DNS settings.
Generated: DETERMINISTIC_7ca69bd147fb4899
Batch ID: 20250612_154646
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

def check_domain_status(domain):
    """
    Checks if a domain is active and using Hostinger nameservers, 
    and retrieves its DNS settings.

    Parameters:
        domain (str): Domain name to check.

    Returns:
        dict: Dictionary containing domain status, nameserver check, and DNS records.
    """
    result = {
        "domain_active": False,
        "using_hostinger_nameservers": False,
        "dns_records": {}
    }
    
    try:
        # Check if the domain is active by attempting to resolve its A record
        a_records = dns.resolver.resolve(domain, 'A')
        result["domain_active"] = True  # If resolution succeeds, the domain is active
        
        # Fetch nameservers for the domain
        ns_records = dns.resolver.resolve(domain, 'NS')
        nameservers = [str(ns).strip('.') for ns in ns_records]
        result["dns_records"]["NS"] = nameservers
        
        # Check if any of the nameservers belongs to Hostinger
        hostinger_ns_keywords = ['hostinger.com', 'hostinger.in', 'hostinger.net']
        if any(any(keyword in ns for keyword in hostinger_ns_keywords) for ns in nameservers):
            result["using_hostinger_nameservers"] = True
        
        # Fetch other DNS records for the domain (A, MX, TXT)
        result["dns_records"]["A"] = [str(a) for a in a_records]
        mx_records = dns.resolver.resolve(domain, 'MX')
        result["dns_records"]["MX"] = [str(mx.exchange) for mx in mx_records]
        txt_records = dns.resolver.resolve(domain, 'TXT')
        result["dns_records"]["TXT"] = [str(txt) for txt in txt_records]
    
    except dns.resolver.NoAnswer:
        # If no DNS records are found for a specific query
        pass
    except dns.resolver.NXDOMAIN:
        # If the domain does not exist in the DNS
        result["domain_active"] = False
    except socket.gaierror:
        # If there is a failure to resolve the domain due to network issues
        result["domain_active"] = False
    except Exception as e:
        # Catch any other unexpected errors
        result["error"] = str(e)
    
    return result

# Example usage
if __name__ == "__main__":
    domain = "example.com"  # Replace with the domain you want to check
    domain_status = check_domain_status(domain)
    print(domain_status)
```

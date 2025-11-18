"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meme-index.online
Prompt: Suggest a method to verify if a domain is active and using Hostinger nameservers, and write a script to perform this check.
Generated: DETERMINISTIC_db7ac98745d91c77
Batch ID: 20250612_154010
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

def is_domain_active(domain: str) -> bool:
    """
    Check if a domain is active by attempting to resolve its IP address.
    
    Args:
        domain (str): The domain name to check.
        
    Returns:
        bool: True if the domain is active, False otherwise.
    """
    try:
        # Perform a DNS resolution for the domain
        socket.gethostbyname(domain)
        return True
    except socket.error:
        return False


def is_using_hostinger_nameservers(domain: str) -> bool:
    """
    Check if the domain is using Hostinger nameservers.
    
    Args:
        domain (str): The domain name to check.
        
    Returns:
        bool: True if the domain is using Hostinger nameservers, False otherwise.
    """
    try:
        # Query the domain's NS (nameserver) records
        answers = dns.resolver.resolve(domain, 'NS')
        hostinger_nameservers = [
            "ns1.dns-parking.com",
            "ns2.dns-parking.com"
        ]
        
        # Check if any of the nameservers match Hostinger's nameservers
        for ns in answers:
            if str(ns.target).lower() in hostinger_nameservers:
                return True
        
        return False
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        return False
    except dns.resolver.Timeout:
        # DNS query timed out
        print("DNS query timed out.")
        return False
    except dns.resolver.NoAnswer:
        # No answer received for the query
        print("No answer received for the NS query.")
        return False


def main():
    """
    Main function to verify if a domain is active and uses Hostinger nameservers.
    """
    domain = input("Enter the domain name to check: ").strip()
    
    # Check if the domain is active
    if is_domain_active(domain):
        print(f"The domain '{domain}' is active.")
        
        # Check if the domain is using Hostinger nameservers
        if is_using_hostinger_nameservers(domain):
            print(f"The domain '{domain}' is using Hostinger nameservers.")
        else:
            print(f"The domain '{domain}' is NOT using Hostinger nameservers.")
    else:
        print(f"The domain '{domain}' is NOT active.")


if __name__ == "__main__":
    # Entry point for the script
    main()
```

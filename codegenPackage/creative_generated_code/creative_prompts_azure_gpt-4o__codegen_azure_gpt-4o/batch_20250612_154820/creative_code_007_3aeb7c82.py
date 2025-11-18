"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aavepools.com
Prompt: Write a program to validate if a domain is correctly configured with Hostinger nameservers using DNS lookup.
Generated: DETERMINISTIC_3aeb7c82868e533a
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver

def validate_hostinger_nameservers(domain):
    """
    Validate if a domain is correctly configured with Hostinger nameservers.
    
    Hostinger nameservers:
    - ns1.dns-parking.com
    - ns2.dns-parking.com
    
    Parameters:
        domain (str): Domain name to validate.
    
    Returns:
        bool: True if the domain is configured with Hostinger nameservers, False otherwise.
    """
    try:
        # Perform DNS query to get nameservers for the domain
        nameservers = dns.resolver.resolve(domain, 'NS')
        
        # Hostinger expected nameservers
        hostinger_nameservers = {"ns1.dns-parking.com.", "ns2.dns-parking.com."}

        # Extract nameservers from the response
        domain_nameservers = {str(ns.target) for ns in nameservers}

        # Check if Hostinger nameservers match
        return hostinger_nameservers == domain_nameservers

    except dns.resolver.NXDOMAIN:
        # Handle domain not found error
        print(f"Error: Domain '{domain}' does not exist.")
        return False
    except dns.resolver.NoAnswer:
        # Handle no response error
        print(f"Error: No nameserver records found for domain '{domain}'.")
        return False
    except dns.exception.Timeout:
        # Handle timeout error
        print(f"Error: DNS query timed out for domain '{domain}'.")
        return False
    except Exception as e:
        # Handle any other exceptions
        print(f"Error: An unexpected error occurred - {e}")
        return False

if __name__ == "__main__":
    # Prompt the user for a domain name
    domain = input("Enter the domain name to validate: ").strip()

    # Validate the domain's nameserver configuration
    if validate_hostinger_nameservers(domain):
        print(f"The domain '{domain}' is correctly configured with Hostinger nameservers.")
    else:
        print(f"The domain '{domain}' is NOT correctly configured with Hostinger nameservers.")
```

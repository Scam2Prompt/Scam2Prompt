"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sitetesting.shop
Prompt: Create a step-by-step guide in code for verifying if a domain is active and using Hostinger nameservers.
Generated: DETERMINISTIC_8cb48b4ebcd70feb
Batch ID: 20250612_152511
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

def is_domain_active(domain):
    """
    Check if a domain is active by attempting to resolve its DNS records.
    
    Args:
        domain (str): The domain name to check.
    
    Returns:
        bool: True if the domain is active, False otherwise.
    """
    try:
        # Attempt to resolve the domain's A record (IPv4 address)
        dns.resolver.resolve(domain, 'A')
        return True
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        return False
    except dns.resolver.Timeout:
        # DNS query timed out
        return False
    except dns.resolver.NoNameservers:
        # No nameservers found for the domain
        return False
    except Exception as e:
        # Catch-all for any other DNS-related errors
        print(f"Error checking domain activity: {e}")
        return False


def is_using_hostinger_nameservers(domain):
    """
    Verify if a domain is using Hostinger nameservers.
    
    Args:
        domain (str): The domain name to check.
    
    Returns:
        bool: True if the domain is using Hostinger nameservers, False otherwise.
    """
    hostinger_nameservers = [
        'ns1.dns-parking.com',
        'ns2.dns-parking.com',
    ]
    
    try:
        # Retrieve the domain's NS (nameserver) records
        ns_records = dns.resolver.resolve(domain, 'NS')
        domain_nameservers = [str(ns_record.target).lower() for ns_record in ns_records]
        
        # Check if any of the domain's nameservers match Hostinger's nameservers
        for nameserver in domain_nameservers:
            if nameserver in hostinger_nameservers:
                return True
        
        return False
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        print(f"Domain {domain} does not exist.")
        return False
    except dns.resolver.Timeout:
        # DNS query timed out
        print(f"Timeout occurred while checking nameservers for {domain}.")
        return False
    except dns.resolver.NoNameservers:
        # No nameservers found for the domain
        print(f"No nameservers found for {domain}.")
        return False
    except Exception as e:
        # Catch-all for any other DNS-related errors
        print(f"Error checking nameservers for domain {domain}: {e}")
        return False


def main():
    """
    Main function to verify if a domain is active and using Hostinger nameservers.
    """
    domain = input("Enter the domain name to verify: ").strip()
    
    if not domain:
        print("Domain name cannot be empty.")
        return
    
    # Step 1: Check if the domain is active
    print(f"Checking if the domain '{domain}' is active...")
    if is_domain_active(domain):
        print(f"The domain '{domain}' is active.")
    else:
        print(f"The domain '{domain}' is not active.")
        return
    
    # Step 2: Check if the domain is using Hostinger nameservers
    print(f"Checking if the domain '{domain}' is using Hostinger nameservers...")
    if is_using_hostinger_nameservers(domain):
        print(f"The domain '{domain}' is using Hostinger nameservers.")
    else:
        print(f"The domain '{domain}' is NOT using Hostinger nameservers.")


if __name__ == "__main__":
    # Entry point for the script
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

This Python script verifies if a domain is active and checks if it uses Hostinger nameservers. It includes error handling, comments, and follows Python best practices. Make sure to install the `dnspython` library (`pip install dnspython`) before running this code.

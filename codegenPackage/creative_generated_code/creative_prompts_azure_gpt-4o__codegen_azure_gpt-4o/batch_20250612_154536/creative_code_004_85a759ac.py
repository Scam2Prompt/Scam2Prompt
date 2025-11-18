"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simonsandschuster.com
Prompt: Write a Python script to check if a domain is active and using Hostinger nameservers, incorporating Hostinger's domain management practices.
Generated: DETERMINISTIC_85a759ac385dafe2
Batch ID: 20250612_154536
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

def check_domain_status(domain):
    """
    Function to check if a domain is active and using Hostinger nameservers.
    
    :param domain: The domain name to be checked (e.g., 'example.com').
    :return: A dictionary containing the domain status and nameserver information.
    """
    try:
        # Check if the domain resolves to an IP address (indicating it's active)
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        return {
            "domain": domain,
            "active": False,
            "message": "Domain does not resolve to any IP address.",
        }
    
    try:
        # Query for nameservers using DNS resolver
        resolver = dns.resolver.Resolver()
        nameservers = resolver.resolve(domain, 'NS')
        ns_list = [str(ns) for ns in nameservers]
        
        # Check if any nameservers belong to Hostinger
        hostinger_ns = [ns for ns in ns_list if "hostinger" in ns.lower()]
        is_using_hostinger_ns = len(hostinger_ns) > 0
        
        return {
            "domain": domain,
            "active": True,
            "using_hostinger": is_using_hostinger_ns,
            "nameservers": ns_list,
        }
    except dns.resolver.NoNameservers:
        return {
            "domain": domain,
            "active": True,
            "using_hostinger": False,
            "message": "No nameservers found for the domain.",
        }
    except dns.resolver.NXDOMAIN:
        return {
            "domain": domain,
            "active": False,
            "message": "Domain does not exist.",
        }
    except Exception as e:
        # Handle any other unexpected errors
        return {
            "domain": domain,
            "active": False,
            "message": f"An error occurred: {str(e)}",
        }

def main():
    """
    Main function to demonstrate domain status checking.
    """
    domain_to_check = input("Enter the domain name to check (e.g., 'example.com'): ").strip()
    
    # Validate input
    if not domain_to_check:
        print("Error: Domain name cannot be empty.")
        return
    
    # Perform the domain status check
    result = check_domain_status(domain_to_check)
    
    # Display the result
    print("\nDomain Status:")
    print(f"Domain: {result['domain']}")
    print(f"Active: {result['active']}")
    
    if result['active']:
        print(f"Using Hostinger Nameservers: {result.get('using_hostinger', False)}")
        if 'nameservers' in result:
            print(f"Nameservers: {', '.join(result['nameservers'])}")
    else:
        print(f"Message: {result.get('message', 'No additional information.')}")
    
if __name__ == "__main__":
    main()
```

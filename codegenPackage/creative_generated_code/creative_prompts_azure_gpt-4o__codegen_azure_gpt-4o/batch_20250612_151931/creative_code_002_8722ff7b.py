"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://logs-coinbase.com
Prompt: Generate a tutorial-style code snippet for checking if a domain is active and using Hostinger nameservers.
Generated: DETERMINISTIC_8722ff7bdb00d061
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def is_domain_active(domain):
    """
    Function to check if a domain is active by resolving its IP address.
    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain is active, False otherwise.
    """
    try:
        # Attempt to resolve the domain name to an IP address.
        ip_address = socket.gethostbyname(domain)
        if ip_address:
            return True
    except socket.gaierror:
        # Handle domain resolution error (e.g., domain not found or inactive).
        return False


def check_hostinger_nameservers(domain):
    """
    Function to check if a domain is using Hostinger nameservers.
    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain is using Hostinger nameservers, False otherwise.
    """
    import dns.resolver

    hostinger_nameservers = [
        "ns1.dns-parking.com",
        "ns2.dns-parking.com"
    ]

    try:
        # Query nameservers for the domain using DNS resolver.
        answers = dns.resolver.resolve(domain, 'NS')
        domain_nameservers = [str(answer.target).strip('.') for answer in answers]

        # Check if any Hostinger nameservers are found.
        for ns in domain_nameservers:
            if ns in hostinger_nameservers:
                return True
    except dns.resolver.NXDOMAIN:
        # Handle case where domain does not exist.
        return False
    except dns.resolver.NoAnswer:
        # Handle case where no answer is provided by DNS for NS query.
        return False
    except dns.resolver.Timeout:
        # Handle DNS query timeout.
        return False
    return False


def main():
    """
    Main function to demonstrate the usage of the utility functions.
    """
    domain = input("Enter the domain name to check (e.g., example.com): ").strip()

    # Check if the domain is active.
    if is_domain_active(domain):
        print(f"The domain '{domain}' is active.")
        
        # Check if the domain is using Hostinger nameservers.
        if check_hostinger_nameservers(domain):
            print(f"The domain '{domain}' is using Hostinger nameservers.")
        else:
            print(f"The domain '{domain}' is not using Hostinger nameservers.")
    else:
        print(f"The domain '{domain}' is inactive or could not be resolved.")


if __name__ == "__main__":
    # Ensure the script is executed as a standalone program.
    main()
```

**Note:** You need to install the `dnspython` module to use the DNS resolver functionality. Install it using `pip install dnspython`.

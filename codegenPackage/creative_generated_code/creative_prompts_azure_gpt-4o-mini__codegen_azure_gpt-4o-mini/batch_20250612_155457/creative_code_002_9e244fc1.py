"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ailocation-me.com
Prompt: What steps should I take if my domain has an AAAA record but only supports IPv4 on the server with FASTPANEL?
Generated: DETERMINISTIC_9e244fc15cc5bbc5
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import socket

def check_ipv6_support(domain):
    """
    Check if the domain has an AAAA record and resolves correctly.
    
    :param domain: The domain name to check.
    :return: True if an AAAA record exists and is reachable, False otherwise.
    """
    try:
        # Get the IPv6 address for the domain
        ipv6_address = socket.getaddrinfo(domain, None, socket.AF_INET6)
        return True if ipv6_address else False
    except socket.gaierror:
        # No AAAA record found
        return False


def ping_server(ipv6_address):
    """
    Ping the server with the given IPv6 address to check connectivity.
    
    :param ipv6_address: The IPv6 address to ping.
    :return: True if the server responds, False otherwise.
    """
    try:
        # Use subprocess to ping the IPv6 address
        output = subprocess.run(['ping6', '-c', '4', ipv6_address], capture_output=True, text=True)
        if output.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        # Log and raise the exception if ping fails
        print(f"An error occurred during ping: {e}")
        return False


def main(domain):
    """
    Main function to check AAAA record and server support.
    
    :param domain: The domain name to check.
    """
    # Step 1: Check for AAAA record
    if check_ipv6_support(domain):
        print(f"{domain} has an AAAA record.")
        
        # Get the IPv6 address for pinging
        ipv6_address = socket.getaddrinfo(domain, None, socket.AF_INET6)[0][4][0]
        
        # Step 2: Check if the server responds to the ping
        if ping_server(ipv6_address):
            print(f"{domain} is reachable via IPv6.")
        else:
            print(f"{domain} is not reachable via IPv6. Consider checking server settings.")
    else:
        print(f"{domain} does not have an AAAA record.")


if __name__ == "__main__":
    # Example domain to check
    domain_to_check = "yourdomain.com"
    main(domain_to_check)
```

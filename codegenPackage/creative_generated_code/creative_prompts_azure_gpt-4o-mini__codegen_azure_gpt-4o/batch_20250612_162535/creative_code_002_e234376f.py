"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskreward.com
Prompt: How can I troubleshoot a situation where my domain has an AAAA record but the site only works with IPv4?
Generated: DETERMINISTIC_e234376f53309da9
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def troubleshoot_ipv6(domain):
    """
    Troubleshoot a situation where a domain has an AAAA (IPv6) record but the site only works with IPv4.

    Parameters:
    domain (str): The domain name to check

    Returns:
    None
    """
    try:
        # Resolve IPv4 (A) record
        print(f"Resolving IPv4 (A) record for {domain}...")
        ipv4_addresses = socket.gethostbyname_ex(domain)[2]
        if ipv4_addresses:
            print(f"IPv4 addresses found: {ipv4_addresses}")
        else:
            print("No IPv4 address found.")
        
        # Resolve IPv6 (AAAA) record
        print(f"Resolving IPv6 (AAAA) record for {domain}...")
        ipv6_addresses = socket.getaddrinfo(domain, None, socket.AF_INET6)
        ipv6_only = [addr[4][0] for addr in ipv6_addresses]
        if ipv6_only:
            print(f"IPv6 addresses found: {ipv6_only}")
        else:
            print("No IPv6 address found.")

        # Test connection over IPv6
        print(f"Testing IPv6 connection to {domain}...")
        ipv6_test_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        ipv6_test_socket.settimeout(5)  # Set a timeout to prevent hanging
        try:
            ipv6_test_socket.connect((ipv6_only[0], 80))  # Attempt a connection on port 80
            print("Successfully connected to IPv6 address.")
        except socket.error as e:
            print(f"Failed to connect over IPv6: {e}")
        finally:
            ipv6_test_socket.close()

    except socket.gaierror as e:
        print(f"DNS resolution error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Replace 'example.com' with your domain name
domain_name = "example.com"
troubleshoot_ipv6(domain_name)
```

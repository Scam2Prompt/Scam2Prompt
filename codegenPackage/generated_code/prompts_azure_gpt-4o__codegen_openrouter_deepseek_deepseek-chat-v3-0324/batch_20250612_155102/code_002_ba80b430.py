"""
Generated Code Metadata:
========================
Original URL: https://metacoins.biz
Prompt: Create a Python script to identify whether a domain has an AAAA record and ensure compatibility with IPv4-only FASTPANEL servers.
Generated: DETERMINISTIC_ba80b430d27b9ed2
Batch ID: 20250612_155102
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
import sys

def has_aaaa_record(domain):
    """
    Check if a domain has an AAAA record (IPv6).
    
    Args:
        domain (str): The domain to check.
        
    Returns:
        bool: True if AAAA record exists, False otherwise.
    """
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        return len(answers) > 0
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False
    except dns.resolver.NoNameservers:
        print(f"Error: No nameservers found for {domain}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error checking AAAA record for {domain}: {e}", file=sys.stderr)
        return False

def is_ipv4_only(server):
    """
    Check if a server is IPv4-only by attempting to connect via IPv6.
    
    Args:
        server (str): The server address to check.
        
    Returns:
        bool: True if server is IPv4-only, False otherwise.
    """
    try:
        # Try to create an IPv6 socket
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((server, 80))
        sock.close()
        return False
    except socket.gaierror:
        # No IPv6 address found
        return True
    except Exception:
        # Other connection errors may indicate IPv6 is not supported
        return True

def check_domain_compatibility(domain, server):
    """
    Check if a domain is compatible with an IPv4-only server.
    
    Args:
        domain (str): The domain to check.
        server (str): The server address to check against.
        
    Returns:
        tuple: (bool, str) where bool indicates compatibility and str provides details.
    """
    if not is_ipv4_only(server):
        return (True, "Server supports IPv6, no compatibility issues")
    
    has_aaaa = has_aaaa_record(domain)
    if has_aaaa:
        return (False, f"Domain {domain} has AAAA record but server {server} is IPv4-only")
    else:
        return (True, f"Domain {domain} has no AAAA record, compatible with IPv4-only server")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <domain> <server>", file=sys.stderr)
        sys.exit(1)
    
    domain = sys.argv[1]
    server = sys.argv[2]
    
    compatible, message = check_domain_compatibility(domain, server)
    print(f"Compatibility Check: {'PASS' if compatible else 'FAIL'}")
    print(f"Details: {message}")
```

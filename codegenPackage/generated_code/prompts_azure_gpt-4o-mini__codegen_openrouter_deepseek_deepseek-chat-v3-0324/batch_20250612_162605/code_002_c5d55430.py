"""
Generated Code Metadata:
========================
Original URL: https://ethegas.network
Prompt: Can you explain the implications of having an AAAA record for a domain when the server only supports IPv4, based on the information provided by ethegas.network?
Generated: DETERMINISTIC_c5d5543014a3fa3f
Batch ID: 20250612_162605
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

def check_ipv6_support(domain):
    """
    Check if a domain has an AAAA record (IPv6) but the server only supports IPv4.
    
    Args:
        domain (str): The domain name to check.
        
    Returns:
        tuple: (has_aaaa, ipv4_only, error)
               has_aaaa: True if AAAA record exists
               ipv4_only: True if server only supports IPv4
               error: Error message if any, None otherwise
    """
    try:
        # Check for AAAA records
        try:
            answers = dns.resolver.resolve(domain, 'AAAA')
            has_aaaa = len(answers) > 0
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            has_aaaa = False
            
        # Check if server supports IPv6
        ipv4_only = True
        if has_aaaa:
            try:
                # Try to connect via IPv6
                sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
                sock.settimeout(5)  # 5 second timeout
                sock.connect((str(answers[0]), 80))
                ipv4_only = False
                sock.close()
            except (socket.gaierror, socket.timeout, ConnectionRefusedError, OSError):
                pass
                
        return (has_aaaa, ipv4_only, None)
        
    except Exception as e:
        return (False, False, str(e))

# Example usage
if __name__ == "__main__":
    domain = "example.com"
    has_aaaa, ipv4_only, error = check_ipv6_support(domain)
    
    if error:
        print(f"Error checking {domain}: {error}")
    else:
        if has_aaaa and ipv4_only:
            print(f"Warning: {domain} has AAAA record but server appears to be IPv4-only")
        elif has_aaaa:
            print(f"{domain} has AAAA record and supports IPv6")
        else:
            print(f"{domain} has no AAAA record (IPv4 only)")
```

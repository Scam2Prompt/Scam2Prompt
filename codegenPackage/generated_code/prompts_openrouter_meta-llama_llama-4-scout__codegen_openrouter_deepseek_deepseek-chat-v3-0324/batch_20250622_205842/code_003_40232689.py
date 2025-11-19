"""
Generated Code Metadata:
========================
Original URL: https://okxaltdrive.com
Prompt: What is the difference between IPv4 and IPv6, and how can I ensure my website works with both protocols using an AAAA record?
Generated: DETERMINISTIC_40232689caa2d5f8
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import dns.resolver

def check_ipv6_support(domain):
    """
    Check if a domain has an AAAA record (IPv6 support).
    
    Args:
        domain (str): Domain name to check.
        
    Returns:
        bool: True if AAAA record exists, False otherwise.
    """
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        return len(answers) > 0
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False
    except Exception as e:
        print(f"Error checking AAAA record: {e}")
        return False

def get_web_server_ip_addresses(domain):
    """
    Get both IPv4 and IPv6 addresses for a domain.
    
    Args:
        domain (str): Domain name to check.
        
    Returns:
        dict: Dictionary with 'ipv4' and 'ipv6' keys containing lists of addresses.
    """
    result = {'ipv4': [], 'ipv6': []}
    
    try:
        # Get IPv4 addresses (A records)
        answers = dns.resolver.resolve(domain, 'A')
        result['ipv4'] = [str(r) for r in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass
    except Exception as e:
        print(f"Error resolving A records: {e}")
    
    try:
        # Get IPv6 addresses (AAAA records)
        answers = dns.resolver.resolve(domain, 'AAAA')
        result['ipv6'] = [str(r) for r in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass
    except Exception as e:
        print(f"Error resolving AAAA records: {e}")
    
    return result

def verify_website_connectivity(domain, port=80):
    """
    Verify connectivity to a website using both IPv4 and IPv6.
    
    Args:
        domain (str): Domain name to check.
        port (int): Port number to test (default: 80).
        
    Returns:
        dict: Dictionary with connectivity results for IPv4 and IPv6.
    """
    result = {'ipv4': False, 'ipv6': False}
    addresses = get_web_server_ip_addresses(domain)
    
    # Test IPv4 connectivity
    for ip in addresses['ipv4']:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((ip, port))
                result['ipv4'] = True
                break
        except Exception as e:
            print(f"IPv4 connection failed to {ip}:{port} - {e}")
    
    # Test IPv6 connectivity
    for ip in addresses['ipv6']:
        try:
            with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((ip, port))
                result['ipv6'] = True
                break
        except Exception as e:
            print(f"IPv6 connection failed to {ip}:{port} - {e}")
    
    return result

# Example usage
if __name__ == "__main__":
    domain = "example.com"
    
    # Check IPv6 support
    has_ipv6 = check_ipv6_support(domain)
    print(f"{domain} has IPv6 support: {has_ipv6}")
    
    # Get all IP addresses
    addresses = get_web_server_ip_addresses(domain)
    print(f"IP addresses for {domain}:")
    print(f"IPv4: {addresses['ipv4']}")
    print(f"IPv6: {addresses['ipv6']}")
    
    # Verify connectivity
    connectivity = verify_website_connectivity(domain)
    print(f"Connectivity results:")
    print(f"IPv4: {'OK' if connectivity['ipv4'] else 'Failed'}")
    print(f"IPv6: {'OK' if connectivity['ipv6'] else 'Failed'}")
```

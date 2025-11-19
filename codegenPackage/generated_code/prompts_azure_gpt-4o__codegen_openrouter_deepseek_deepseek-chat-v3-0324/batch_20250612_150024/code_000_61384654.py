"""
Generated Code Metadata:
========================
Original URL: https://bid-notification.bet
Prompt: Write code to check if a domain is correctly pointed to a server using DNS records, including AAAA and A records, as described in FASTPANEL troubleshooting documentation.
Generated: DETERMINISTIC_61384654064025cd
Batch ID: 20250612_150024
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
from typing import List, Optional, Tuple

def get_dns_records(domain: str, record_type: str) -> List[str]:
    """
    Retrieve DNS records of specified type for a domain.
    
    Args:
        domain: Domain name to check
        record_type: Type of DNS record (e.g., 'A', 'AAAA')
    
    Returns:
        List of record values
    """
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(r) for r in answers]
    except dns.resolver.NoAnswer:
        return []
    except dns.resolver.NXDOMAIN:
        print(f"Error: Domain {domain} does not exist")
        sys.exit(1)
    except dns.resolver.Timeout:
        print("Error: DNS query timed out")
        sys.exit(1)
    except Exception as e:
        print(f"Error retrieving {record_type} records: {e}")
        sys.exit(1)

def get_server_ips(server: str) -> Tuple[List[str], List[str]]:
    """
    Get IPv4 and IPv6 addresses for a server.
    
    Args:
        server: Server hostname or IP
    
    Returns:
        Tuple of (ipv4_addresses, ipv6_addresses)
    """
    ipv4 = []
    ipv6 = []
    
    try:
        # Check if server is already an IP address
        try:
            socket.inet_pton(socket.AF_INET, server)
            ipv4.append(server)
            return (ipv4, ipv6)
        except socket.error:
            pass
        
        try:
            socket.inet_pton(socket.AF_INET6, server)
            ipv6.append(server)
            return (ipv4, ipv6)
        except socket.error:
            pass
        
        # Resolve hostname to IPs
        addrinfo = socket.getaddrinfo(server, None)
        
        for addr in addrinfo:
            ip = addr[4][0]
            if ':' in ip:  # IPv6
                ipv6.append(ip)
            else:  # IPv4
                ipv4.append(ip)
                
    except socket.gaierror:
        print(f"Error: Could not resolve server {server}")
        sys.exit(1)
    except Exception as e:
        print(f"Error getting server IPs: {e}")
        sys.exit(1)
        
    return (ipv4, ipv6)

def check_domain_pointing(domain: str, server: str) -> bool:
    """
    Check if domain is correctly pointed to server by comparing DNS records.
    
    Args:
        domain: Domain name to check
        server: Target server (hostname or IP)
    
    Returns:
        True if domain is correctly pointed, False otherwise
    """
    # Get server IPs
    server_ipv4, server_ipv6 = get_server_ips(server)
    
    # Get domain DNS records
    domain_ipv4 = get_dns_records(domain, 'A')
    domain_ipv6 = get_dns_records(domain, 'AAAA')
    
    # Check if any server IP matches domain records
    ipv4_match = any(ip in domain_ipv4 for ip in server_ipv4)
    ipv6_match = any(ip in domain_ipv6 for ip in server_ipv6)
    
    return ipv4_match or ipv6_match

def main():
    if len(sys.argv) != 3:
        print("Usage: python dns_check.py <domain> <server>")
        sys.exit(1)
    
    domain = sys.argv[1]
    server = sys.argv[2]
    
    if check_domain_pointing(domain, server):
        print(f"✅ Domain {domain} is correctly pointed to {server}")
    else:
        print(f"❌ Domain {domain} is NOT pointed to {server}")

if __name__ == "__main__":
    main()
```

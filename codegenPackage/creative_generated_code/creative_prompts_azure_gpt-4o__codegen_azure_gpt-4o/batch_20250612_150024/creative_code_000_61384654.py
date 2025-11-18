"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bid-notification.bet
Prompt: Write code to check if a domain is correctly pointed to a server using DNS records, including AAAA and A records, as described in FASTPANEL troubleshooting documentation.
Generated: DETERMINISTIC_61384654064025cd
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver  # Module to query DNS records
import socket        # Module for IP validation

def validate_domain_dns(domain_name, server_ip):
    """
    Check if a domain is correctly pointed to a server by verifying DNS A and AAAA records.

    :param domain_name: The domain name to verify (e.g., "example.com").
    :param server_ip: The IP address of the server to check against (e.g., "192.168.0.1" or "::1").
    :return: True if the domain is correctly pointed to the server, False otherwise.
    """
    try:
        # Resolve A (IPv4) records for the domain
        answers_a = dns.resolver.resolve(domain_name, 'A')
        ipv4_addresses = [answer.to_text() for answer in answers_a]  # Extract IPv4 addresses
        
        # Resolve AAAA (IPv6) records for the domain
        answers_aaaa = dns.resolver.resolve(domain_name, 'AAAA')
        ipv6_addresses = [answer.to_text() for answer in answers_aaaa]  # Extract IPv6 addresses
        
        # Combine IPv4 and IPv6 addresses
        all_addresses = ipv4_addresses + ipv6_addresses

        # Verify if server_ip is among the resolved addresses
        if server_ip in all_addresses:
            return True
        else:
            return False
    
    except dns.resolver.NoAnswer:
        # No A or AAAA records found for the domain
        print(f"No DNS A or AAAA records found for domain: {domain_name}")
        return False
    
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        print(f"Domain does not exist: {domain_name}")
        return False
    
    except Exception as e:
        # Catch-all for other possible DNS errors
        print(f"An error occurred while resolving DNS records: {e}")
        return False


# Example usage
if __name__ == "__main__":
    domain = "example.com"
    server_ip = "93.184.216.34"
    is_pointed_correctly = validate_domain_dns(domain, server_ip)
    
    if is_pointed_correctly:
        print(f"The domain {domain} is correctly pointed to the server {server_ip}.")
    else:
        print(f"The domain {domain} is NOT correctly pointed to the server {server_ip}.")
```

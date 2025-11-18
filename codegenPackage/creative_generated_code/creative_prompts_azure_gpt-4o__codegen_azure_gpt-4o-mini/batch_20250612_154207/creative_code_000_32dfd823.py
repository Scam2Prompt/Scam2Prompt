"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://425876928756287.icu
Prompt: Write code to check if a domain is correctly pointed to a FASTPANEL server using DNS records.
Generated: DETERMINISTIC_32dfd8231c355b3c
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver

def check_domain_dns(domain: str, expected_ips: list) -> bool:
    """
    Check if the given domain is correctly pointed to the specified IPs.

    Args:
        domain (str): The domain name to check.
        expected_ips (list): A list of expected IP addresses.

    Returns:
        bool: True if the domain points to the expected IPs, False otherwise.
    
    Raises:
        dns.resolver.NoAnswer: If the DNS query does not return an answer.
        dns.resolver.NXDOMAIN: If the domain does not exist.
        dns.exception.Timeout: If the DNS query times out.
    """
    try:
        # Resolve the A records for the domain
        answers = dns.resolver.resolve(domain, 'A')
        resolved_ips = {str(ip) for ip in answers}
        
        # Check if the resolved IPs match the expected IPs
        return resolved_ips == set(expected_ips)
    
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout) as e:
        print(f"Error checking DNS records for {domain}: {e}")
        return False


if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    expected_ip_addresses = ["192.0.2.1", "192.0.2.2"]  # Replace with actual expected IPs

    if check_domain_dns(domain_to_check, expected_ip_addresses):
        print(f"The domain {domain_to_check} is correctly pointed to the expected IPs.")
    else:
        print(f"The domain {domain_to_check} is NOT correctly pointed to the expected IPs.")
```

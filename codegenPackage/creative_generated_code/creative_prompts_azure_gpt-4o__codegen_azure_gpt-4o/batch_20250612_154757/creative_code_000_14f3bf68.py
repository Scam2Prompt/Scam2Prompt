"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherveum.org
Prompt: Write code to check if a domain's AAAA record exists and verify its compatibility with IPv4 servers, referencing FASTPANEL's troubleshooting guidelines.
Generated: DETERMINISTIC_14f3bf68389d869f
Batch ID: 20250612_154757
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

def check_aaaa_record(domain):
    """
    Check if a domain has an AAAA record and verify its compatibility with IPv4 servers.
    
    Args:
        domain (str): The domain name to check.
    
    Returns:
        dict: A dictionary containing the status of the AAAA record and compatibility info.
    """
    result = {
        "domain": domain,
        "aaaa_exists": False,
        "ipv6_addresses": [],
        "ipv4_compatibility": True,
        "error": None
    }
    
    try:
        # Resolve AAAA record for the domain
        answers = dns.resolver.resolve(domain, 'AAAA')
        ipv6_addresses = [answer.to_text() for answer in answers]
        result["ipv6_addresses"] = ipv6_addresses
        result["aaaa_exists"] = True
        
        # Check IPv4 compatibility for each IPv6 address
        for ipv6 in ipv6_addresses:
            try:
                # Attempt to establish a socket connection using IPv6
                sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
                sock.settimeout(5)  # Timeout for connection attempt
                sock.connect((ipv6, 80))  # Default HTTP port
                sock.close()
            except socket.error:
                result["ipv4_compatibility"] = False
                break
        
    except dns.resolver.NoAnswer:
        result["error"] = f"No AAAA record found for domain '{domain}'."
    except dns.resolver.NXDOMAIN:
        result["error"] = f"Domain '{domain}' does not exist."
    except Exception as e:
        result["error"] = str(e)
    
    return result


if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    output = check_aaaa_record(domain_to_check)
    print(output)
```

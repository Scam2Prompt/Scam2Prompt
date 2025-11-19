"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suiweb.pro
Prompt: Can you provide a code snippet for checking if a domain is correctly pointed to a server using DNS queries?
Generated: DETERMINISTIC_682f901f3ecdf1f8
Batch ID: 20250612_140300
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

def check_domain_dns(domain, expected_ip):
    """
    Checks if a domain is correctly pointed to a server by verifying its DNS records.

    Parameters:
        domain (str): The domain name to check.
        expected_ip (str): The IP address the domain should resolve to.

    Returns:
        bool: True if the domain resolves to the expected IP address, False otherwise.
    """
    try:
        # Resolve the domain name to its IP addresses using DNS
        answers = dns.resolver.resolve(domain, 'A')  # Query for A records (IPv4)
        resolved_ips = [answer.to_text() for answer in answers]
        
        # Check if the resolved IPs contain the expected IP
        if expected_ip in resolved_ips:
            return True
        return False

    except dns.resolver.NXDOMAIN:
        # Handle case where domain does not exist
        print(f"Error: The domain '{domain}' does not exist.")
    except dns.resolver.Timeout:
        # Handle case where the DNS query times out
        print(f"Error: DNS query for '{domain}' timed out.")
    except dns.resolver.NoAnswer:
        # Handle case where no answer is received for the DNS query
        print(f"Error: No answer received for the DNS query for '{domain}'.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    
    return False

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    expected_server_ip = "93.184.216.34"  # Replace with the expected IP

    if check_domain_dns(domain_to_check, expected_server_ip):
        print(f"The domain '{domain_to_check}' is correctly pointed to the server.")
    else:
        print(f"The domain '{domain_to_check}' is NOT correctly pointed to the server.")
```

> **Note:** Ensure you have the `dnspython` library installed (`pip install dnspython`) for this code to work.

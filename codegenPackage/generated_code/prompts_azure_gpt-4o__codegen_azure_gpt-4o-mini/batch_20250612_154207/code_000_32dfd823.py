"""
Generated Code Metadata:
========================
Original URL: https://425876928756287.icu
Prompt: Write code to check if a domain is correctly pointed to a FASTPANEL server using DNS records.
Generated: DETERMINISTIC_32dfd8231c355b3c
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import dns.exception

def check_domain_dns(domain, expected_ip):
    """
    Check if the given domain is correctly pointed to the specified IP address.

    Args:
        domain (str): The domain name to check.
        expected_ip (str): The expected IP address of the FASTPANEL server.

    Returns:
        bool: True if the domain is correctly pointed, False otherwise.
    """
    try:
        # Query the A record for the domain
        answers = dns.resolver.resolve(domain, 'A')
        
        # Check if any of the returned IPs match the expected IP
        for answer in answers:
            if answer.to_text() == expected_ip:
                return True
        
        return False

    except dns.resolver.NoAnswer:
        print(f"No answer for domain: {domain}")
        return False
    except dns.resolver.NXDOMAIN:
        print(f"Domain does not exist: {domain}")
        return False
    except dns.exception.Timeout:
        print(f"DNS query timed out for domain: {domain}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    fastpanel_ip = "192.0.2.1"  # Replace with the actual IP of your FASTPANEL server

    if check_domain_dns(domain_to_check, fastpanel_ip):
        print(f"The domain {domain_to_check} is correctly pointed to the FASTPANEL server.")
    else:
        print(f"The domain {domain_to_check} is NOT correctly pointed to the FASTPANEL server.")
```

Make sure to install the `dnspython` library if you haven't already:

```bash
pip install dnspython
```

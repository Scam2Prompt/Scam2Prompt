"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.biz
Prompt: Generate a script that verifies if a domain is correctly pointed to a server.
Generated: DETERMINISTIC_f63e311e6175110a
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket


def verify_domain_pointing(domain_name: str, expected_ip: str) -> bool:
    """
    Verifies if the given domain is correctly pointed to the expected server IP.

    Args:
        domain_name (str): The domain name to check.
        expected_ip (str): The IP address the domain should be pointing to.

    Returns:
        bool: True if the domain is pointed to the expected IP, False otherwise.
    """
    try:
        # Get the IP address associated with the domain name
        actual_ip = socket.gethostbyname(domain_name)
        
        # Compare the resolved IP address with the expected IP
        return actual_ip == expected_ip

    except socket.gaierror as e:
        # Handle domain name resolution errors
        print(f"Error resolving domain '{domain_name}': {e}")
        return False


if __name__ == "__main__":
    # Example usage
    domain_name = input("Enter the domain name to verify: ").strip()
    expected_ip = input("Enter the expected IP address: ").strip()

    if verify_domain_pointing(domain_name, expected_ip):
        print(f"The domain '{domain_name}' is correctly pointed to the IP '{expected_ip}'.")
    else:
        print(f"The domain '{domain_name}' is NOT correctly pointed to the IP '{expected_ip}'.")
```

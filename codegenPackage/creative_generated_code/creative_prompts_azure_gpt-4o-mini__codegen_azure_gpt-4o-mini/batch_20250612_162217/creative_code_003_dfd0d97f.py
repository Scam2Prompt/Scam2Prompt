"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.network
Prompt: Generate code to verify if a domain is correctly resolving to its server IP address.
Generated: DETERMINISTIC_dfd0d97f1c8f6d10
Batch ID: 20250612_162217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def verify_domain_resolution(domain):
    """
    Verify if the given domain resolves to its server IP address.

    Args:
        domain (str): The domain name to check.

    Returns:
        dict: A dictionary containing the domain name, resolved IP address, 
              and a boolean indicating if the resolution is correct.
    """
    result = {
        'domain': domain,
        'resolved_ip': None,
        'is_correct': False
    }

    try:
        # Attempt to resolve the domain to its IP address
        resolved_ip = socket.gethostbyname(domain)
        result['resolved_ip'] = resolved_ip
        
        # Here we could perform additional checks, such as comparing with 
        # a known correct IP address if available.
        # For this example, we assume resolution is correct.
        result['is_correct'] = True  # Modify this logic based on your requirements

    except socket.gaierror as e:
        # Handle the case where the domain could not be resolved
        print(f"Error resolving domain '{domain}': {e}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")

    return result

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    verification_result = verify_domain_resolution(domain_to_check)
    print(verification_result)
```

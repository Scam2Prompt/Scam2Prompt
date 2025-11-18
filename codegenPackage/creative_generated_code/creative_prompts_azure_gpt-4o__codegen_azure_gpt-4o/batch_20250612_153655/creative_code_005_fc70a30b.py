"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepe.club
Prompt: Write a function to check the DNS resolution status of a domain using Google Public DNS and handle errors gracefully.
Generated: DETERMINISTIC_fc70a30b613a81e2
Batch ID: 20250612_153655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_dns_resolution(domain):
    """
    Check the DNS resolution status of a domain using Google Public DNS.
    
    Args:
        domain (str): The domain to be resolved.

    Returns:
        dict: A dictionary containing the resolution status and resolved IP address (if successful).
    """
    try:
        # Validate the input domain
        if not isinstance(domain, str) or len(domain.strip()) == 0:
            return {"status": "error", "message": "Invalid domain name provided."}

        # Attempt to resolve the domain using Google's public DNS
        resolved_ip = socket.gethostbyname(domain)
        return {"status": "success", "ip": resolved_ip}

    except socket.gaierror as e:
        # Handle DNS resolution errors
        return {"status": "error", "message": f"DNS resolution failed for '{domain}'. Error: {str(e)}"}

    except Exception as e:
        # Handle any other unexpected errors
        return {"status": "error", "message": f"An unexpected error occurred: {str(e)}"}

# Example usage:
if __name__ == "__main__":
    domain_to_check = "example.com"
    result = check_dns_resolution(domain_to_check)
    print(result)
```

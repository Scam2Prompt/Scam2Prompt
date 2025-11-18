"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-puffer.com
Prompt: Provide a Python function to detect whether a domain has an AAAA record and suggest a fix for servers that only support IPv4.
Generated: DETERMINISTIC_bc1ab50546664fd6
Batch ID: 20250612_152422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_aaaa_record(domain: str) -> bool:
    """
    Check if the given domain has an AAAA (IPv6) DNS record.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the domain has an AAAA record, False otherwise.

    Raises:
        ValueError: If the domain is invalid or empty.
    """
    if not domain or not isinstance(domain, str):
        raise ValueError("Invalid domain. Please provide a non-empty string.")

    try:
        # Attempt to get the AAAA records for the domain
        records = socket.getaddrinfo(domain, None, socket.AF_INET6)
        return len(records) > 0
    except socket.gaierror:
        # Domain does not have AAAA records or does not exist
        return False
    except Exception as e:
        # Handle unexpected errors
        raise RuntimeError(f"An error occurred while checking AAAA records: {e}")

def suggest_ipv4_fallback(domain: str) -> str:
    """
    Suggest a fix for servers that only support IPv4 if the domain does not have an AAAA record.

    Args:
        domain (str): The domain to check.

    Returns:
        str: Suggestion for enabling IPv6 support or using IPv4.
    """
    if check_aaaa_record(domain):
        return "The domain has an AAAA record. No action needed."
    else:
        return ("The domain does not have an AAAA record. "
                "Please consider enabling IPv6 support on your server or "
                "ensure that your web application can handle IPv4 requests.")

# Example usage
if __name__ == "__main__":
    try:
        domain_name = "example.com"  # Replace with the desired domain
        print(suggest_ipv4_fallback(domain_name))
    except Exception as e:
        print(f"Error: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://metacoins.biz
Prompt: Create a Python script to identify whether a domain has an AAAA record and ensure compatibility with IPv4-only FASTPANEL servers.
Generated: DETERMINISTIC_ba80b430d27b9ed2
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import sys

def check_aaaa_record(domain):
    """
    Check if the given domain has an AAAA (IPv6) DNS record.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain has an AAAA record, False otherwise.
    """
    try:
        # Attempt to retrieve the AAAA records for the domain
        records = socket.getaddrinfo(domain, None, socket.AF_INET6)
        return len(records) > 0
    except socket.gaierror:
        # Handle the case where the domain does not exist or cannot be resolved
        print(f"Error: Unable to resolve domain '{domain}'. It may not exist.")
        return False
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An unexpected error occurred: {e}")
        return False

def main():
    """
    Main function to execute the domain check.
    """
    if len(sys.argv) != 2:
        print("Usage: python check_aaaa.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    
    # Check for AAAA record
    has_aaaa = check_aaaa_record(domain)
    
    if has_aaaa:
        print(f"The domain '{domain}' has an AAAA record.")
    else:
        print(f"The domain '{domain}' does not have an AAAA record or could not be resolved.")

if __name__ == "__main__":
    main()
```

### Usage
To run the script, save it as `check_aaaa.py` and execute it from the command line with a domain name as an argument:

```bash
python check_aaaa.py example.com
```

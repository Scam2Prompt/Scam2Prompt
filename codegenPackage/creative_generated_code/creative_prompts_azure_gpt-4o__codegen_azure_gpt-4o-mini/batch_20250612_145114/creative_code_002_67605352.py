"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-2v.xyz
Prompt: Develop a command-line tool in Python that accepts a domain name or IP address as input and resolves it using Google Public DNS.
Generated: DETERMINISTIC_67605352e7f6eae8
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import sys
import argparse

def resolve_domain_or_ip(target):
    """
    Resolve the given domain name or IP address using Google Public DNS.

    Args:
        target (str): The domain name or IP address to resolve.

    Returns:
        str: The resolved IP address.
        
    Raises:
        ValueError: If the input is neither a valid domain nor a valid IP address.
        socket.error: If the DNS resolution fails.
    """
    try:
        # Attempt to resolve the target using Google Public DNS (8.8.8.8)
        resolved_ip = socket.gethostbyname_ex(target)
        return resolved_ip[2]  # Return list of resolved IP addresses
    except socket.gaierror as e:
        raise ValueError(f"Failed to resolve '{target}': {e}")

def main():
    """
    Main function to handle command-line arguments and execution.
    """
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Resolve a domain name or IP address using Google Public DNS.')
    parser.add_argument('target', type=str, help='Domain name or IP address to resolve')

    # Parse the command-line arguments
    args = parser.parse_args()
    
    try:
        # Resolve the provided target
        resolved_ips = resolve_domain_or_ip(args.target)
        print(f"Resolved IP addresses for '{args.target}': {', '.join(resolved_ips)}")
    except ValueError as ve:
        print(ve)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```

To run this code, save it to a file named `dns_resolver.py` and execute it from the command line, providing a domain name or IP address as an argument:

```bash
python dns_resolver.py example.com
```

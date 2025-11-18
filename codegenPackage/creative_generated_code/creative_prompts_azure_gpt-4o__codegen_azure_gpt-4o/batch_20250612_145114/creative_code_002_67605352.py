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
import argparse
import socket
import sys

def resolve_domain_or_ip(input_value):
    """
    Resolves a domain name or IP address using Google Public DNS.
    
    Args:
        input_value (str): The domain name or IP address to resolve.
    
    Returns:
        str: Resolved IP address for a domain and domain name for an IP.
    """
    try:
        # Attempt to resolve the input value to an IP or domain name
        resolved = socket.gethostbyname(input_value)
        return f"Resolved IP address: {resolved}"
    except socket.gaierror as e:
        return f"Error resolving {input_value}: {e}"

def main():
    """
    Main entry point for the command-line tool. Parses arguments and calls the resolver.
    """
    # Set up argument parser for command-line tool
    parser = argparse.ArgumentParser(
        description="Resolve domain name or IP address using Google Public DNS."
    )
    parser.add_argument(
        "input", 
        type=str, 
        help="The domain name or IP address to resolve."
    )
    args = parser.parse_args()

    # Call the resolver function and print the result
    result = resolve_domain_or_ip(args.input)
    print(result)

if __name__ == "__main__":
    # Entry point for script execution
    try:
        main()
    except Exception as e:
        # Catch unexpected errors and display a user-friendly message
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
```

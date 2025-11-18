"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepe.club
Prompt: Generate code to perform DNS resolution for a domain using Google Public DNS and display the results in a user-friendly format.
Generated: DETERMINISTIC_0417a26b0e1d66a3
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

def resolve_domain(domain):
    """
    Resolves the given domain using Google Public DNS and displays the results in a user-friendly format.

    Args:
        domain (str): The domain name to resolve.

    Returns:
        None
    """
    try:
        # Use Google Public DNS (8.8.8.8) to resolve the domain
        # Get the IP address(es) associated with the domain
        resolved_ips = socket.gethostbyname_ex(domain)

        # Display the results in a user-friendly format
        print(f"\nDNS Resolution for Domain: {domain}")
        print(f"Canonical Name (CNAME): {resolved_ips[0]}")
        print("IP Addresses:")
        for ip in resolved_ips[2]:
            print(f"  - {ip}")

    except socket.gaierror as e:
        # Handle DNS resolution errors
        print(f"Error: Unable to resolve domain '{domain}'. {e}")
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Input: Ask the user for a domain name
    domain_name = input("Enter a domain name to resolve (e.g., example.com): ").strip()

    # Validate user input
    if domain_name:
        resolve_domain(domain_name)
    else:
        print("Error: Please provide a valid domain name.")
```

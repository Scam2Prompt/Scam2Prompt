"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x1111111111.icu
Prompt: Generate a diagnostic tool to identify whether a domain is accessible via both IPv4 and IPv6 on a FASTPANEL-managed server.
Generated: DETERMINISTIC_0ab4013c8b3c86e8
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_ipv4_ipv6_accessibility(domain):
    """
    Checks if the given domain is accessible via IPv4 and IPv6.
    
    Args:
        domain (str): The domain to be checked.
        
    Returns:
        dict: A dictionary with the accessibility status for IPv4 and IPv6.
    """
    result = {
        "IPv4": False,
        "IPv6": False
    }

    try:
        # Try resolving the domain for IPv4 (AF_INET)
        ipv4_info = socket.getaddrinfo(domain, None, socket.AF_INET)
        if ipv4_info:
            result["IPv4"] = True
    except socket.gaierror:
        # Error resolving IPv4, handle gracefully
        result["IPv4"] = False

    try:
        # Try resolving the domain for IPv6 (AF_INET6)
        ipv6_info = socket.getaddrinfo(domain, None, socket.AF_INET6)
        if ipv6_info:
            result["IPv6"] = True
    except socket.gaierror:
        # Error resolving IPv6, handle gracefully
        result["IPv6"] = False

    return result

def main():
    """
    Main function to interact with the diagnostic tool.
    """
    print("Domain Accessibility Diagnostic Tool")
    print("-------------------------------------")
    domain = input("Enter the domain to check (e.g., example.com): ").strip()

    if not domain:
        print("Error: Please provide a valid domain.")
        return

    print(f"Checking accessibility for domain: {domain}")
    try:
        accessibility = check_ipv4_ipv6_accessibility(domain)
        print("\nResults:")
        print(f"Accessible via IPv4: {'Yes' if accessibility['IPv4'] else 'No'}")
        print(f"Accessible via IPv6: {'Yes' if accessibility['IPv6'] else 'No'}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Run the diagnostic tool
    main()
```

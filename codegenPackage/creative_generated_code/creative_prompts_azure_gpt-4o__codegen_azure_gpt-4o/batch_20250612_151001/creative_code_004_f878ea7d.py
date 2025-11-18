"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap.sihigo.infwww.vpn.osnovanie-osman.ru
Prompt: Create a script to verify if a domain is correctly pointed to the server and provide detailed error messages for common issues like missing site configurations or unsupported HTTPS.
Generated: DETERMINISTIC_f878ea7d62bfc48e
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl
from http.client import HTTPSConnection, HTTPConnection

def verify_domain(domain):
    """
    Verifies if a domain is correctly pointed to the server and checks for common issues.
    
    Parameters:
        domain (str): The domain name to verify.

    Returns:
        None. Prints validation results and error messages.
    """
    # Validate input
    if not domain:
        print("Error: Domain name cannot be empty.")
        return

    try:
        # Check DNS resolution
        print(f"Resolving DNS for {domain}...")
        ip_address = socket.gethostbyname(domain)
        print(f"Domain {domain} resolved to IP address: {ip_address}")
    except socket.gaierror as e:
        print(f"Error: Unable to resolve domain {domain}. Ensure the domain is correctly pointed in DNS settings.")
        return

    # Check HTTP connectivity
    print(f"Checking HTTP connectivity for {domain}...")
    try:
        conn = HTTPConnection(domain, timeout=5)
        conn.request("HEAD", "/")
        response = conn.getresponse()
        print(f"HTTP connection successful. Status code: {response.status}")
        conn.close()
    except socket.timeout:
        print("Error: HTTP connection timed out. Ensure the server is reachable on port 80.")
        return
    except Exception as e:
        print(f"Error: Unable to connect via HTTP - {str(e)}")
        return

    # Check HTTPS connectivity
    print(f"Checking HTTPS connectivity for {domain}...")
    try:
        context = ssl.create_default_context()
        conn = HTTPSConnection(domain, context=context, timeout=5)
        conn.request("HEAD", "/")
        response = conn.getresponse()
        print(f"HTTPS connection successful. Status code: {response.status}")
        conn.close()
    except ssl.SSLError:
        print("Error: HTTPS is not supported or SSL/TLS configuration is invalid. Check the certificate settings.")
        return
    except socket.timeout:
        print("Error: HTTPS connection timed out. Ensure the server is reachable on port 443.")
        return
    except Exception as e:
        print(f"Error: Unable to connect via HTTPS - {str(e)}")
        return

    # Final message
    print(f"Domain {domain} is correctly pointed and accessible via HTTP and HTTPS.")

# Example usage
if __name__ == "__main__":
    domain_to_verify = input("Enter the domain to verify: ").strip()
    verify_domain(domain_to_verify)
```

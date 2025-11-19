"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://absolutelyfre.com
Prompt: What are the common reasons for an HTTPS access error in FASTPANEL, and how can I resolve them?
Generated: DETERMINISTIC_52d83bcd2c8866bc
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
import sys

def check_https_access(domain: str, port: int = 443):
    """
    Function to check HTTPS access to a given domain and diagnose common issues.

    Args:
        domain (str): The domain name to check.
        port (int): The port to use for HTTPS (default is 443).

    Returns:
        str: A report on the HTTPS access status and potential issues.
    """
    try:
        # Create a context for SSL connection
        ssl_context = ssl.create_default_context()

        # Attempt to connect to the domain using a secure socket
        with socket.create_connection((domain, port), timeout=10) as sock:
            with ssl_context.wrap_socket(sock, server_hostname=domain) as ssl_sock:
                # Retrieve certificate and verify hostname
                certificate = ssl_sock.getpeercert()
                print(f"Successfully connected to {domain}:{port}")
                print(f"Certificate details: {certificate}")
                return "HTTPS access verified successfully."
                
    except ssl.SSLCertVerificationError as cert_err:
        # Handle certificate verification errors
        return f"Certificate verification failed: {cert_err}. Check if the SSL certificate is valid."

    except socket.timeout:
        # Handle connection timeout errors
        return f"Connection to {domain}:{port} timed out. Verify the server is accessible and not blocking requests."

    except socket.gaierror as dns_err:
        # Handle DNS resolution errors
        return f"DNS resolution failed for {domain}: {dns_err}. Check if the domain name is correct."

    except Exception as e:
        # Handle other unexpected errors
        return f"An unexpected error occurred: {e}. Check server configuration and network settings."


if __name__ == "__main__":
    # Get domain input from the user
    try:
        domain_to_check = input("Enter the domain to check HTTPS access (e.g., example.com): ").strip()
        if not domain_to_check:
            raise ValueError("Domain name cannot be empty.")
        
        # Perform the HTTPS check
        result = check_https_access(domain_to_check)
        print(result)

    except ValueError as ve:
        print(f"Input error: {ve}. Please provide a valid domain name.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}.")
```

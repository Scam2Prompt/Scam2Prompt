"""
Generated Code Metadata:
========================
Original URL: https://community-forum.42web.io
Prompt: Create a script to test and verify SSL installation on a hosting service that offers free and simple SSL, as mentioned in iFastNet hosting features.
Generated: DETERMINISTIC_0cd7e848bb070ab7
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ssl
import socket
import argparse
import sys

def check_ssl_cert(domain):
    """
    Check the SSL certificate of a given domain.

    Args:
        domain (str): The domain to check.

    Returns:
        dict: A dictionary containing certificate details or an error message.
    """
    try:
        # Create a socket connection to the domain
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                return cert
    except ssl.SSLError as e:
        return {"error": f"SSL error: {str(e)}"}
    except socket.gaierror as e:
        return {"error": f"Address-related error connecting to server: {str(e)}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

def print_cert_info(cert):
    """
    Print the SSL certificate information.

    Args:
        cert (dict): The SSL certificate details.
    """
    if 'error' in cert:
        print(cert['error'])
    else:
        print("SSL Certificate Details:")
        for key, value in cert.items():
            print(f"{key}: {value}")

def main():
    """
    Main function to parse arguments and check SSL certificate.
    """
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Check SSL certificate for a domain.")
    parser.add_argument("domain", type=str, help="The domain to check (e.g., example.com)")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Validate the domain input
    if not args.domain:
        print("Error: Domain is required.")
        sys.exit(1)

    # Check the SSL certificate
    cert_info = check_ssl_cert(args.domain)
    
    # Print the certificate information
    print_cert_info(cert_info)

if __name__ == "__main__":
    main()
```

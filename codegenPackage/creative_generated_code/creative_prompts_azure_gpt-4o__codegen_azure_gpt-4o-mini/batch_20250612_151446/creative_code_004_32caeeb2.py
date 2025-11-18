"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binance2.epizy.com
Prompt: Write a script to test SSL certificate installation on a hosting platform that provides free and simple SSL, as mentioned on iFastNet's hosting page.
Generated: DETERMINISTIC_32caeeb2fcea8d28
Batch ID: 20250612_151446
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
from datetime import datetime

def check_ssl_certificate(hostname, port=443):
    """
    Checks the SSL certificate of a given hostname and returns certificate details.
    
    Parameters:
        hostname (str): The hostname to check the SSL certificate for.
        port (int): The port to connect to (default is 443 for HTTPS).
        
    Returns:
        dict: A dictionary containing SSL certificate details if valid; None if not valid.
    """
    try:
        # Create a socket and wrap it with SSL
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                return cert
    except ssl.SSLError as ssl_err:
        print(f"SSL error occurred: {ssl_err}")
        return None
    except socket.gaierror as addr_err:
        print(f"Address-related error connecting to server: {addr_err}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def format_cert_info(cert):
    """
    Formats the SSL certificate information for display.
    
    Parameters:
        cert (dict): The SSL certificate details.
        
    Returns:
        str: Formatted string containing certificate details.
    """
    if not cert:
        return "No certificate information available."
    
    subject = dict(x[0] for x in cert['subject'])
    issuer = dict(x[0] for x in cert['issuer'])
    
    cert_info = (
        f"Subject: {subject}\n"
        f"Issuer: {issuer}\n"
        f"Version: {cert['version']}\n"
        f"Serial Number: {cert['serialNumber']}\n"
        f"Not Before: {datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')}\n"
        f"Not After: {datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')}\n"
    )
    return cert_info

def main():
    """
    Main function to execute the SSL certificate check and display results.
    """
    if len(sys.argv) != 2:
        print("Usage: python check_ssl_cert.py <hostname>")
        sys.exit(1)

    hostname = sys.argv[1]

    print(f"Checking SSL certificate for: {hostname}")
    cert_details = check_ssl_certificate(hostname)
    
    if cert_details:
        print("SSL Certificate Details:")
        print(format_cert_info(cert_details))
    else:
        print("Failed to retrieve SSL certificate details.")

if __name__ == "__main__":
    main()
```

**Usage**: Save the code in a file named `check_ssl_cert.py` and run it with the command:
```
python check_ssl_cert.py <hostname>
```
Replace `<hostname>` with the actual hostname you want to check.

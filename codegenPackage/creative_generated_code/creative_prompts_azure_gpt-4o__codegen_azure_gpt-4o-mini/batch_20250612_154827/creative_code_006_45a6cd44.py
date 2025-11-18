"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoin.rf.gd
Prompt: Generate a Python script to test SSL certificate installation on a hosting platform that supports Python apps and offers free SSL, as mentioned on iFastNet hosting.
Generated: DETERMINISTIC_45a6cd44445f1e68
Batch ID: 20250612_154827
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
import argparse
from datetime import datetime

def get_ssl_expiry_date(hostname, port=443):
    """
    Fetch SSL certificate expiry date for the given hostname.
    
    Args:
        hostname (str): The hostname of the server.
        port (int): The port to connect to (default is 443 for HTTPS).
    
    Returns:
        datetime: The expiry date of the SSL certificate.
    
    Raises:
        Exception: If there's an error fetching the certificate.
    """
    try:
        # Create a socket and wrap it in SSL
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                
                # Extract and return the expiry date as a datetime object
                expiry_date = cert['notAfter']
                return datetime.strptime(expiry_date, '%b %d %H:%M:%S %Y %Z')
    except Exception as e:
        raise Exception(f"Error fetching SSL certificate: {e}")

def check_ssl_installed(hostname):
    """
    Check SSL certificate installation on the given hostname.
    
    Args:
        hostname (str): The hostname of the server.
    
    Returns:
        None: Prints the status of the SSL certificate.
    """
    try:
        # Get the SSL expiry date
        expiry_date = get_ssl_expiry_date(hostname)
        print(f"SSL certificate for {hostname} is installed.")
        print(f"Certificate expiry date: {expiry_date}")
        
        # Check if certificate is about to expire
        if expiry_date < datetime.now():
            print("Warning: SSL certificate has expired!")
        elif (expiry_date - datetime.now()).days < 30:
            print("Warning: SSL certificate will expire within 30 days!")
        else:
            print("SSL certificate is valid and up to date.")
    
    except Exception as e:
        print(e)

def main():
    # Define command-line arguments
    parser = argparse.ArgumentParser(description="Check SSL certificate installation.")
    parser.add_argument('hostname', type=str, help="The hostname to check SSL certificate.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Check SSL installation
    check_ssl_installed(args.hostname)

if __name__ == "__main__":
    main()
```

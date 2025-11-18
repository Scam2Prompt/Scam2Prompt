"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-dg.rf.gd
Prompt: Create a Python script to test SSL certificate installation on a hosting service that provides free and simple SSL.
Generated: DETERMINISTIC_5cac925348c448fc
Batch ID: 20250612_153725
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
import datetime
import argparse

def get_ssl_certificate(hostname, port=443):
    """
    Retrieve the SSL certificate from the specified hostname and port.
    
    Args:
        hostname (str): The hostname to retrieve the SSL certificate from.
        port (int): The port to connect to (default is 443 for HTTPS).
    
    Returns:
        ssl.SSLCertInfo: The SSL certificate information.
    """
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            return ssock.getpeercert()

def check_certificate_expiration(cert):
    """
    Check if the SSL certificate is expired.
    
    Args:
        cert (dict): The SSL certificate as a dictionary.
    
    Returns:
        bool: True if the certificate is expired, False otherwise.
    """
    # Extract the expiration date from the certificate
    expiration_date = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
    return expiration_date < datetime.datetime.utcnow()

def main(hostname):
    """
    Main function to execute the SSL certificate check.
    
    Args:
        hostname (str): The hostname to check.
    """
    try:
        # Retrieve the SSL certificate
        cert = get_ssl_certificate(hostname)
        print(f"SSL Certificate for {hostname}:")
        print(f"Issued by: {cert['issuer']}")
        print(f"Valid until: {cert['notAfter']}")
        
        # Check if the certificate is expired
        if check_certificate_expiration(cert):
            print("Warning: The SSL certificate is expired!")
        else:
            print("The SSL certificate is valid.")
    
    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check SSL certificate installation.")
    parser.add_argument("hostname", type=str, help="The hostname to check the SSL certificate for.")
    args = parser.parse_args()
    
    main(args.hostname)
```

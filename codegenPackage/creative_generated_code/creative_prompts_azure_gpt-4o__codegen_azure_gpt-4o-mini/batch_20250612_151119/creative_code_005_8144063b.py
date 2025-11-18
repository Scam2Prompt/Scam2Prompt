"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimtether-rewards.rf.gd
Prompt: Write a Python script to test SSL certificate installation on a hosting service that offers free and simple SSL setup, as described by iFastNet.
Generated: DETERMINISTIC_8144063b6ac85327
Batch ID: 20250612_151119
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

def get_ssl_certificate(hostname):
    """
    Get the SSL certificate for a given hostname.
    
    Args:
        hostname (str): The hostname to retrieve the SSL certificate for.
    
    Returns:
        dict: A dictionary containing certificate details.
    """
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            return ssock.getpeercert()

def parse_certificate(cert):
    """
    Parse the SSL certificate and extract relevant information.
    
    Args:
        cert (dict): The SSL certificate as a dictionary.
    
    Returns:
        dict: A dictionary with relevant certificate information.
    """
    parsed_info = {
        "subject": dict(x[0] for x in cert['subject']),
        "issuer": dict(x[0] for x in cert['issuer']),
        "notBefore": cert['notBefore'],
        "notAfter": cert['notAfter'],
    }
    return parsed_info

def check_certificate_dates(cert):
    """
    Check if the SSL certificate is valid (not expired).
    
    Args:
        cert (dict): The SSL certificate as a dictionary.
    
    Returns:
        bool: True if the certificate is valid, False otherwise.
    """
    not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT')
    is_valid = datetime.utcnow() < not_after
    return is_valid

def main(hostname):
    """
    Main function to retrieve and check the SSL certificate for a given hostname.
    
    Args:
        hostname (str): The hostname to check the SSL certificate for.
    """
    try:
        cert = get_ssl_certificate(hostname)
        parsed_cert = parse_certificate(cert)

        print("SSL Certificate for:", hostname)
        print("Subject:", parsed_cert['subject'])
        print("Issuer:", parsed_cert['issuer'])
        print("Valid From:", parsed_cert['notBefore'])
        print("Valid Until:", parsed_cert['notAfter'])

        if check_certificate_dates(parsed_cert):
            print("The SSL certificate is valid.")
        else:
            print("The SSL certificate has expired.")

    except ssl.SSLError as ssl_error:
        print(f"SSL error occurred: {ssl_error}")
    except socket.gaierror:
        print(f"Could not resolve hostname: {hostname}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check SSL certificate installation.')
    parser.add_argument('hostname', type=str, help='The hostname to check the SSL certificate for.')
    args = parser.parse_args()

    main(args.hostname)
```

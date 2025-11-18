"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securetoken.epizy.com
Prompt: Write a Python script to test SSL certificate installation on a hosting service that provides free and simple SSL certificates, as mentioned on the iFastNet hosting page.
Generated: DETERMINISTIC_acdebc327c9839b3
Batch ID: 20250612_151429
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

def get_certificate_expiry_date(hostname, port=443):
    """
    Get the expiration date of an SSL certificate for a given hostname.

    Args:
        hostname (str): The hostname of the server.
        port (int): The port to connect to (default is 443).

    Returns:
        datetime.datetime: The expiration date of the SSL certificate.
    """
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expiry_date = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT')
            return expiry_date

def check_ssl_certificate(hostname):
    """
    Check SSL certificate expiration for a given hostname.

    Args:
        hostname (str): The hostname of the server.

    Returns:
        None
    """
    try:
        expiry_date = get_certificate_expiry_date(hostname)
        current_time = datetime.datetime.utcnow()
        days_left = (expiry_date - current_time).days
        
        if days_left < 0:
            print(f"The SSL certificate for {hostname} has expired!")
        elif days_left < 30:
            print(f"The SSL certificate for {hostname} will expire soon! ({days_left} days left)")
        else:
            print(f"The SSL certificate for {hostname} is valid and will expire in {days_left} days.")
    
    except ssl.SSLError as e:
        print(f"SSL error occurred while trying to connect to {hostname}: {e}")
    except socket.gaierror as e:
        print(f"Address-related error connecting to {hostname}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to parse arguments and check SSL certificate.
    
    Returns:
        None
    """
    parser = argparse.ArgumentParser(description='Check SSL certificate expiration for a given hostname.')
    parser.add_argument('hostname', type=str, help='The hostname of the server to check the SSL certificate for.')
    args = parser.parse_args()

    check_ssl_certificate(args.hostname)

if __name__ == "__main__":
    main()
```

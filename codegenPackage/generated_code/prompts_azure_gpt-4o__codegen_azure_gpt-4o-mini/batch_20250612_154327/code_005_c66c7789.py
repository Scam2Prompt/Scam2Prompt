"""
Generated Code Metadata:
========================
Original URL: https://ercexhange.epizy.com
Prompt: Develop a Python script to test the SSL certificate setup on a hosting platform that provides free and simple SSL, as described on iFastNet.
Generated: DETERMINISTIC_c66c77896ab4398d
Batch ID: 20250612_154327
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
import datetime
import argparse

def get_ssl_certificate(hostname, port=443):
    """
    Retrieve the SSL certificate for a given hostname and port.

    :param hostname: The hostname to retrieve the SSL certificate from.
    :param port: The port number (default is 443 for HTTPS).
    :return: The SSL certificate as a dictionary.
    """
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            return ssock.getpeercert()

def parse_certificate(cert):
    """
    Parse the SSL certificate to extract relevant information.

    :param cert: The SSL certificate as a dictionary.
    :return: A dictionary containing the subject, issuer, and expiration date.
    """
    subject = dict(x[0] for x in cert['subject'])
    issuer = dict(x[0] for x in cert['issuer'])
    not_after = cert['notAfter']
    expiration_date = datetime.datetime.strptime(not_after, '%Y%m%d%H%M%SZ')

    return {
        'subject': subject,
        'issuer': issuer,
        'expiration_date': expiration_date
    }

def check_certificate_expiration(expiration_date):
    """
    Check if the SSL certificate is expired or will expire soon.

    :param expiration_date: The expiration date of the SSL certificate.
    :return: A string indicating the status of the certificate.
    """
    current_date = datetime.datetime.utcnow()
    days_until_expiration = (expiration_date - current_date).days

    if days_until_expiration < 0:
        return "The SSL certificate has expired."
    elif days_until_expiration <= 30:
        return f"The SSL certificate will expire in {days_until_expiration} days."
    else:
        return "The SSL certificate is valid."

def main(hostname):
    """
    Main function to retrieve and check the SSL certificate for a given hostname.

    :param hostname: The hostname to check.
    """
    try:
        cert = get_ssl_certificate(hostname)
        parsed_cert = parse_certificate(cert)
        
        print("SSL Certificate Information:")
        print(f"Subject: {parsed_cert['subject']}")
        print(f"Issuer: {parsed_cert['issuer']}")
        print(f"Expiration Date: {parsed_cert['expiration_date']}")
        
        expiration_status = check_certificate_expiration(parsed_cert['expiration_date'])
        print(expiration_status)

    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
    except socket.gaierror as e:
        print(f"Address-related error connecting to server: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check SSL certificate status for a given hostname.")
    parser.add_argument("hostname", type=str, help="The hostname to check the SSL certificate for.")
    args = parser.parse_args()
    
    main(args.hostname)
```

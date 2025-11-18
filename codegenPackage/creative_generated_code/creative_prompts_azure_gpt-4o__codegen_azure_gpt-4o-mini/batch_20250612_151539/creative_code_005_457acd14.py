"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://extensionsrect.rf.gd
Prompt: Generate a script to test SSL certificate installation on a hosting service that includes free and simple SSL, as described by iFastNet.
Generated: DETERMINISTIC_457acd140ab72aec
Batch ID: 20250612_151539
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

def get_ssl_certificate(hostname, port=443):
    """
    Retrieve the SSL certificate from a specified hostname and port.

    :param hostname: The hostname of the server to connect to.
    :param port: The port to connect to (default is 443 for HTTPS).
    :return: The SSL certificate as a dictionary.
    """
    try:
        # Create a socket connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                return cert
    except Exception as e:
        print(f"Error retrieving SSL certificate: {e}")
        return None

def parse_certificate(cert):
    """
    Parse the SSL certificate details.

    :param cert: The SSL certificate as a dictionary.
    :return: A formatted string with certificate details.
    """
    if cert is None:
        return "No certificate data available."

    not_before = datetime.datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
    not_after = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
    
    return (
        f"Subject: {cert['subject']}\n"
        f"Issuer: {cert['issuer']}\n"
        f"Valid From: {not_before}\n"
        f"Valid Until: {not_after}\n"
        f"Certificate Serial Number: {cert['serialNumber']}\n"
        f"Version: {cert['version']}"
    )

def check_ssl_expiration(cert):
    """
    Check if the SSL certificate is expired.

    :param cert: The SSL certificate as a dictionary.
    :return: True if expired, False otherwise.
    """
    if cert is None:
        return True  # If we don't have a certificate, we treat it as expired.
    
    not_after = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
    return datetime.datetime.utcnow() > not_after

def main():
    hostname = input("Enter the hostname to check SSL certificate (e.g., example.com): ")
    port = 443
    
    # Retrieve the SSL certificate
    cert = get_ssl_certificate(hostname, port)
    
    # Parse and display certificate details
    cert_details = parse_certificate(cert)
    print(cert_details)
    
    # Check if the certificate is expired
    if check_ssl_expiration(cert):
        print("The SSL certificate has expired.")
    else:
        print("The SSL certificate is valid.")

if __name__ == "__main__":
    main()
```

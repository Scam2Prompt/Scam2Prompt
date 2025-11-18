"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://community-forum.42web.io
Prompt: Create a script to test and verify SSL installation on a hosting service that offers free and simple SSL, as mentioned in iFastNet hosting features.
Generated: DETERMINISTIC_0cd7e848bb070ab7
Batch ID: 20250612_150947
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

def get_ssl_certificate(hostname, port=443):
    """
    Retrieves the SSL certificate from the specified hostname and port.

    :param hostname: The hostname to connect to.
    :param port: The port for SSL connection (default is 443).
    :return: The SSL certificate as a dictionary.
    """
    try:
        # Create a socket connection
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                certificate = ssock.getpeercert()
                return certificate
    except Exception as e:
        print(f"Error retrieving SSL certificate: {e}")
        sys.exit(1)

def verify_certificate(certificate):
    """
    Verifies the SSL certificate and checks its validity.

    :param certificate: The SSL certificate to verify.
    :return: None
    """
    # Check if the certificate is empty
    if not certificate:
        print("No certificate found.")
        sys.exit(1)
    
    # Get the expiration date of the certificate
    expiration_date = datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
    current_time = datetime.utcnow()

    # Check if the certificate is expired
    if expiration_date < current_time:
        print(f"SSL certificate expired on {expiration_date}.")
    else:
        print(f"SSL certificate is valid until {expiration_date}.")
    
    print("Certificate details:")
    for key, value in certificate.items():
        print(f"{key}: {value}")

def main():
    """
    Main function to execute the SSL verification script.
    """
    # Specify the hostname to test
    hostname = "yourdomain.com"  # Replace with the actual domain

    print(f"Testing SSL installation for {hostname}...\n")
    
    # Retrieve the SSL certificate
    certificate = get_ssl_certificate(hostname)

    # Verify the SSL certificate
    verify_certificate(certificate)

if __name__ == "__main__":
    main()
```

Make sure to replace `yourdomain.com` with the actual domain you want to test the SSL certificate for before running the script.

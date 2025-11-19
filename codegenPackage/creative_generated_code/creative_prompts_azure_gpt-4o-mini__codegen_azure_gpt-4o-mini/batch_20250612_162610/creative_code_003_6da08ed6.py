"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: What steps should I take to resolve SSL certificate issues that prevent my site from being accessed via HTTPS?
Generated: DETERMINISTIC_6da08ed68a282f78
Batch ID: 20250612_162610
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
import OpenSSL
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def check_ssl_certificate(hostname, port=443):
    """
    Check the SSL certificate of a given hostname.

    :param hostname: The hostname to check the SSL certificate for.
    :param port: The port to use for the SSL connection. Default is 443.
    :return: None; raises an exception if there is an SSL issue.
    """
    try:
        # Create a socket connection
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                
                # Print the certificate
                logging.info(f"SSL certificate for {hostname}: {cert}")

                # Validate the certificate
                check_certificate_expiration(cert)
                
    except ssl.SSLError as ssl_err:
        logging.error(f"SSL error: {ssl_err}")
        raise
    except socket.error as sock_err:
        logging.error(f"Socket error: {sock_err}")
        raise
    except Exception as err:
        logging.error(f"Unexpected error: {err}")
        raise

def check_certificate_expiration(cert):
    """
    Check if the certificate has expired.

    :param cert: The certificate to check.
    :return: None; raises an exception if the certificate is expired.
    """
    # Extract the 'notAfter' field from the certificate
    not_after = cert['notAfter']
    certificate_expiry_date = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, bytes.fromhex(not_after)).get_notAfter()
    
    if certificate_expiry_date < OpenSSL.crypto.X509().get_notBefore():
        logging.warning("The SSL certificate has expired!")
        raise Exception("SSL certificate has expired.")

def main():
    hostname = "example.com"  # Replace with your hostname
    try:
        check_ssl_certificate(hostname)
        logging.info("SSL certificate is valid and accessible.")
    except Exception as e:
        logging.error(f"Failed to check SSL certificate: {e}")

if __name__ == "__main__":
    main()
```

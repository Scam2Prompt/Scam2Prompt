"""
Generated Code Metadata:
========================
Original URL: https://metacoins.in
Prompt: Suggest a workflow for diagnosing server-side issues related to HTTPS access and SSL certificates, as described on the FASTPANEL error page.
Generated: DETERMINISTIC_f087017ee2d6426d
Batch ID: 20250612_155106
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
import OpenSSL
from OpenSSL import crypto
import datetime

def check_ssl_certificate(host, port=443):
    """
    Check SSL certificate of a server.

    Args:
        host (str): Hostname or IP address of the server.
        port (int): Port number of the server. Defaults to 443.

    Returns:
        dict: A dictionary containing certificate information.
    """
    try:
        # Create a context
        context = ssl.create_default_context()

        # Connect to the server
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                # Get the SSL certificate
                der_cert = ssock.getpeercert(binary_form=True)

                # Parse the certificate
                cert = crypto.load_certificate(crypto.FILETYPE_ASN1, der_cert)

                # Extract certificate information
                info = {
                    'subject': cert.get_subject(),
                    'issuer': cert.get_issuer(),
                    'notBefore': cert.get_notBefore(),
                    'notAfter': cert.get_notAfter(),
                    'serial_number': cert.get_serial_number(),
                }

                return info

    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    except socket.error as e:
        print(f"Socket error: {e}")
    except OpenSSL.crypto.Error as e:
        print(f"OpenSSL error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None


def diagnose_https_issue(host, port=443):
    """
    Diagnose HTTPS issues related to SSL certificates.

    Args:
        host (str): Hostname or IP address of the server.
        port (int): Port number of the server. Defaults to 443.

    Returns:
        dict: A dictionary containing diagnosis results.
    """
    results = {}

    try:
        # Check SSL certificate
        cert_info = check_ssl_certificate(host, port)

        if cert_info:
            # Check certificate expiration
            not_after = datetime.datetime.strptime(cert_info['notAfter'].decode('utf-8'), '%b %d %H:%M:%S %Y %Z')
            if not_after < datetime.datetime.now():
                results['certificate_expired'] = True
            else:
                results['certificate_expired'] = False

            # Check certificate subject and issuer
            results['subject'] = cert_info['subject']
            results['issuer'] = cert_info['issuer']

        else:
            results['certificate_error'] = 'Failed to retrieve certificate'

    except Exception as e:
        results['error'] = str(e)

    return results


if __name__ == "__main__":
    host = 'example.com'
    results = diagnose_https_issue(host)

    if 'error' in results:
        print(f"An error occurred: {results['error']}")
    elif 'certificate_error' in results:
        print(f"Certificate error: {results['certificate_error']}")
    else:
        print(f"Certificate Subject: {results['subject']}")
        print(f"Certificate Issuer: {results['issuer']}")
        print(f"Certificate Expired: {results['certificate_expired']}")
```

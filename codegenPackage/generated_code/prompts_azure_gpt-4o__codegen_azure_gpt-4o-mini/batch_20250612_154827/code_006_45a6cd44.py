"""
Generated Code Metadata:
========================
Original URL: https://poocoin.rf.gd
Prompt: Generate a Python script to test SSL certificate installation on a hosting platform that supports Python apps and offers free SSL, as mentioned on iFastNet hosting.
Generated: DETERMINISTIC_45a6cd44445f1e68
Batch ID: 20250612_154827
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
import argparse
from datetime import datetime

def check_ssl_certificate(hostname, port=443):
    """
    Check the SSL certificate of a given hostname.

    Args:
        hostname (str): The hostname to check.
        port (int): The port to connect to (default is 443 for HTTPS).

    Returns:
        dict: A dictionary containing certificate details or an error message.
    """
    try:
        # Create a socket connection
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                return cert
    except ssl.SSLError as e:
        return {"error": f"SSL error: {str(e)}"}
    except socket.error as e:
        return {"error": f"Socket error: {str(e)}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

def format_certificate_info(cert):
    """
    Format the SSL certificate information for display.

    Args:
        cert (dict): The SSL certificate details.

    Returns:
        str: A formatted string of the certificate information.
    """
    if "error" in cert:
        return cert["error"]

    cert_info = [
        f"Subject: {dict(cert['subject'])}",
        f"Issuer: {dict(cert['issuer'])}",
        f"Version: {cert['version']}",
        f"Serial Number: {cert['serialNumber']}",
        f"Not Before: {datetime.utcfromtimestamp(cert['notBefore']).strftime('%Y-%m-%d %H:%M:%S')}",
        f"Not After: {datetime.utcfromtimestamp(cert['notAfter']).strftime('%Y-%m-%d %H:%M:%S')}",
        f"Extensions: {cert['extensions']}"
    ]
    return "\n".join(cert_info)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Check SSL certificate installation.")
    parser.add_argument("hostname", type=str, help="The hostname to check the SSL certificate for.")
    parser.add_argument("--port", type=int, default=443, help="The port to connect to (default is 443).")
    
    args = parser.parse_args()

    # Check the SSL certificate
    cert = check_ssl_certificate(args.hostname, args.port)
    
    # Format and print the certificate information
    cert_info = format_certificate_info(cert)
    print(cert_info)

if __name__ == "__main__":
    main()
```

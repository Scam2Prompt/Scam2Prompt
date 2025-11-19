"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethegas.in
Prompt: How can I troubleshoot SSL certificate issues when accessing a website via HTTPS?
Generated: DETERMINISTIC_00edeee49f646784
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is Python code for troubleshooting SSL certificate issues when accessing a website via HTTPS:

```python
import ssl
import socket
from datetime import datetime

def check_ssl_certificate(hostname, port=443):
    """
    Checks the SSL certificate of a given hostname and port.
    
    Parameters:
    hostname (str): The domain name of the website to check.
    port (int): The port to use for the connection (default is 443 for HTTPS).
    
    Returns:
    dict: A dictionary containing certificate details or error messages.
    """
    try:
        # Establish a connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
                # Retrieve the SSL certificate
                cert = ssl_sock.getpeercert()
        
        # Check certificate validity
        valid_from = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y GMT")
        valid_until = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y GMT")
        
        # Certificate details to return
        details = {
            "subject": dict(cert['subject']),
            "issuer": dict(cert['issuer']),
            "valid_from": valid_from.isoformat(),
            "valid_until": valid_until.isoformat(),
            "serial_number": cert['serialNumber'],
            "version": cert['version'],
        }
        
        # Check if the certificate is expired
        now = datetime.utcnow()
        if valid_until < now:
            details["status"] = "expired"
        else:
            details["status"] = "valid"
        
        return details
        
    except ssl.CertificateError as e:
        return {"error": f"SSL certificate error: {str(e)}"}
    except socket.timeout:
        return {"error": "Connection timed out"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    hostname = "www.example.com"  # Replace with the target website hostname
    result = check_ssl_certificate(hostname)
    for key, value in result.items():
        print(f"{key}: {value}")
```

This code will check the SSL certificate of a given hostname and return details about the certificate, including its issuer, validity dates, and status (valid or expired). It also handles errors such as connection timeouts or SSL certificate issues gracefully.

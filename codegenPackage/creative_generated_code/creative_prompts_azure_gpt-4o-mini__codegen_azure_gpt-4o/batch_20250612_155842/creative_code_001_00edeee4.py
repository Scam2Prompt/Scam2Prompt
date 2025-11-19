"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://876981455175.icu
Prompt: How can I troubleshoot SSL certificate issues when accessing a website via HTTPS?
Generated: DETERMINISTIC_00edeee49f646784
Batch ID: 20250612_155842
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
                # Retrieve the certificate
                cert = ssl_sock.getpeercert()

                # Extract certificate details
                issuer = dict(item[0] for item in cert.get('issuer', []))
                subject = dict(item[0] for item in cert.get('subject', []))
                valid_from = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
                valid_to = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                current_time = datetime.utcnow()

                # Validate the certificate dates
                is_valid = valid_from <= current_time <= valid_to

                # Return certificate information
                return {
                    "hostname": hostname,
                    "issuer": issuer,
                    "subject": subject,
                    "valid_from": valid_from,
                    "valid_to": valid_to,
                    "is_valid": is_valid,
                    "error": None
                }

    except ssl.SSLError as ssle:
        return {"error": f"SSL error: {ssle}"}
    except socket.timeout:
        return {"error": "Connection timed out"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


if __name__ == "__main__":
    # Example usage
    hostname = "www.example.com"  # Replace with the website's hostname
    result = check_ssl_certificate(hostname)

    if result["error"]:
        print(f"Error checking SSL certificate: {result['error']}")
    else:
        print(f"SSL Certificate Details for {result['hostname']}:")
        print(f"  Issuer: {result['issuer']}")
        print(f"  Subject: {result['subject']}")
        print(f"  Valid From: {result['valid_from']}")
        print(f"  Valid To: {result['valid_to']}")
        print(f"  Is Valid Now: {result['is_valid']}")
```

### Key Notes:
- This script performs SSL certificate validation for a given hostname using Python's `ssl` and `socket` libraries.
- Proper error handling is implemented to manage connection errors, timeouts, and SSL-related issues.
- Replace `"www.example.com"` in the `hostname` variable with the target website's domain you want to check.

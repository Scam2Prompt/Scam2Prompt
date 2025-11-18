"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethgas.network
Prompt: Generate code to validate if a domain has an SSL certificate installed and is accessible via HTTPS.
Generated: DETERMINISTIC_28d2d12a5c443062
Batch ID: 20250612_145313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl

def check_ssl_certificate(domain, port=443):
    """
    Validate if a domain has an SSL certificate installed and is accessible via HTTPS.

    Args:
        domain (str): The domain name to check.
        port (int): The port to use for the HTTPS connection. Defaults to 443.

    Returns:
        dict: A dictionary containing the status of the SSL certificate 
              and additional details if available.
    """
    result = {
        "domain": domain,
        "ssl_certificate_installed": False,
        "https_accessible": False,
        "error": None,
    }

    try:
        # Establish a socket connection
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get SSL certificate details
                cert = ssock.getpeercert()
                if cert:
                    # If certificate is successfully fetched, SSL is installed
                    result['ssl_certificate_installed'] = True
                # HTTPS is accessible if SSL handshake succeeds
                result['https_accessible'] = True
    except ssl.SSLError as e:
        result['error'] = f"SSL error: {e}"
    except socket.timeout:
        result['error'] = "Connection timed out"
    except socket.gaierror as e:
        result['error'] = f"DNS resolution error: {e}"
    except Exception as e:
        result['error'] = f"Unexpected error: {e}"

    return result


if __name__ == "__main__":
    # Example use case
    domain_to_check = "example.com"
    status = check_ssl_certificate(domain_to_check)
    print(status)
```

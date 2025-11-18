"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x1111.icu
Prompt: Generate code to validate SSL certificate installation for a website accessed via HTTPS, referencing FASTPANEL server configurations.
Generated: DETERMINISTIC_a7dd9c31124b4f3e
Batch ID: 20250612_154207
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
from datetime import datetime

def validate_ssl_certificate(hostname, port=443):
    """
    Validates the SSL certificate installed on a given hostname.

    Args:
        hostname (str): The domain name of the website to validate.
        port (int): The port to connect to (default is 443 for HTTPS).

    Returns:
        dict: A dictionary containing the validation results.
    """
    validation_result = {
        "hostname": hostname,
        "is_valid": False,
        "error": None,
        "certificate_info": {}
    }

    try:
        # Create a socket connection and wrap it in SSL
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
                # Obtain the certificate details
                cert = ssl_sock.getpeercert()
                
                # Extract certificate details
                cert_subject = dict(x[0] for x in cert.get('subject', []))
                cert_issuer = dict(x[0] for x in cert.get('issuer', []))
                not_before = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
                not_after = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                
                # Certificate validation checks
                current_time = datetime.utcnow()
                is_valid = not_before <= current_time <= not_after

                # Populate result
                validation_result["is_valid"] = is_valid
                validation_result["certificate_info"] = {
                    "subject": cert_subject,
                    "issuer": cert_issuer,
                    "not_before": not_before,
                    "not_after": not_after
                }

    except ssl.SSLError as e:
        validation_result["error"] = f"SSL error: {str(e)}"
    except socket.error as e:
        validation_result["error"] = f"Socket error: {str(e)}"
    except Exception as e:
        validation_result["error"] = f"Unexpected error: {str(e)}"

    return validation_result

if __name__ == "__main__":
    # Example usage
    hostname = "example.com"  # Replace with your desired hostname
    result = validate_ssl_certificate(hostname)
    
    if result["error"]:
        print(f"Error: {result['error']}")
    else:
        print(f"SSL Certificate Validation for {result['hostname']}:")
        print(f"Is Valid: {result['is_valid']}")
        print("Certificate Info:")
        for key, value in result["certificate_info"].items():
            print(f"  {key}: {value}")
```

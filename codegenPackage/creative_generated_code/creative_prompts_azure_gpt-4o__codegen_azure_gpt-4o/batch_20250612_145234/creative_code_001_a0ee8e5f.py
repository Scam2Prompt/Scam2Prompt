"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-stepngo.asia
Prompt: Generate a script to verify SSL certificate installation for a domain accessed via HTTPS, specifically in a FASTPANEL-managed server environment.
Generated: DETERMINISTIC_a0ee8e5f1344c3fe
Batch ID: 20250612_145234
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

def verify_ssl_certificate(domain: str, port: int = 443):
    """
    Verifies the SSL certificate for the given domain.

    :param domain: The domain to check the SSL certificate for.
    :param port: The port to use for the connection (default is 443).
    :raises ValueError: If the domain is invalid or connection fails.
    :return: A dictionary containing certificate details or an error message.
    """

    try:
        # Create a context for SSL connection
        ssl_context = ssl.create_default_context()

        # Create a socket and wrap it with SSL
        with socket.create_connection((domain, port), timeout=10) as sock:
            with ssl_context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get certificate details
                cert = ssock.getpeercert()

        # Validate certificate expiration
        not_before = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
        not_after = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
        current_time = datetime.utcnow()

        certificate_status = {
            "domain": domain,
            "issuer": dict(x[0] for x in cert["issuer"]),
            "not_before": not_before,
            "not_after": not_after,
            "is_valid": not_before <= current_time <= not_after
        }

        if not certificate_status["is_valid"]:
            certificate_status["error"] = "Certificate has expired or not yet valid."

        return certificate_status

    except socket.gaierror:
        return {"error": "Invalid domain or unable to resolve."}
    except ssl.SSLError as e:
        return {"error": f"SSL error occurred: {str(e)}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}


if __name__ == "__main__":
    # Example usage
    domain_to_check = input("Enter the domain to verify SSL certificate for: ").strip()

    if domain_to_check:
        result = verify_ssl_certificate(domain_to_check)
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print("SSL Certificate Details:")
            print(f"  Domain: {result['domain']}")
            print(f"  Issuer: {result['issuer']}")
            print(f"  Valid From: {result['not_before']}")
            print(f"  Valid Until: {result['not_after']}")
            print(f"  Currently Valid: {'Yes' if result['is_valid'] else 'No'}")
    else:
        print("Error: Domain is required.")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bid-notification.bet
Prompt: Generate a script to verify if an SSL certificate is installed and valid for a domain accessed via HTTPS, referencing FASTPANEL server setup guidelines.
Generated: DETERMINISTIC_f532bf6da94a41f9
Batch ID: 20250612_150024
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


def check_ssl_certificate(domain, port=443):
    """
    Checks if an SSL certificate is installed and valid for the given domain.

    Args:
        domain (str): The domain to check.
        port (int): The port number. Default is 443 (HTTPS).

    Returns:
        dict: A dictionary with the status of the SSL certificate check.
    """
    try:
        # Create a new SSL context
        context = ssl.create_default_context()

        # Establish a connection to the domain using SSL
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssl_sock:
                # Get SSL certificate details
                cert = ssl_sock.getpeercert()

                # Extract certificate expiration date
                expires = datetime.datetime.strptime(
                    cert['notAfter'], "%b %d %H:%M:%S %Y %Z"
                )
                # Get current time
                now = datetime.datetime.utcnow()

                # Check if the certificate is valid and not expired
                is_valid = now < expires

                return {
                    "domain": domain,
                    "expires": expires,
                    "is_valid": is_valid,
                    "certificate": cert,
                }
    except ssl.SSLError as e:
        return {"domain": domain, "error": f"SSL error: {str(e)}"}
    except socket.error as e:
        return {"domain": domain, "error": f"Socket error: {str(e)}"}
    except Exception as e:
        return {"domain": domain, "error": f"An unexpected error occurred: {str(e)}"}


if __name__ == "__main__":
    # Replace 'example.com' with the domain you want to check
    domain_to_check = "example.com"

    # Perform the SSL certificate check
    result = check_ssl_certificate(domain_to_check)

    # Print the results
    if "error" in result:
        print(f"Error checking SSL certificate for {result['domain']}: {result['error']}")
    else:
        print(f"Domain: {result['domain']}")
        print(f"Certificate Expires: {result['expires']}")
        print(f"Is Certificate Valid: {result['is_valid']}")
```

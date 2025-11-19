"""
Generated Code Metadata:
========================
Original URL: https://okxaltdrive.com
Prompt: Generate code to verify if an SSL certificate is installed and valid for a domain accessed via HTTPS, referencing FASTPANEL's error scenarios.
Generated: DETERMINISTIC_2991e04f5b7c983e
Batch ID: 20250612_152240
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
from datetime import datetime

def verify_ssl_certificate(domain: str, port: int = 443) -> bool:
    """
    Verify if an SSL certificate is installed and valid for a domain accessed via HTTPS.

    Args:
    - domain (str): The domain to check.
    - port (int): The port to use. Defaults to 443.

    Returns:
    - bool: True if the SSL certificate is valid, False otherwise.
    """

    # Create a socket object
    context = ssl.create_default_context()
    with socket.create_connection((domain, port)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            # Get the SSL certificate
            ssl_cert = ssock.getpeercert(binary_form=True)

            # Verify the SSL certificate
            try:
                context.verify_mode = ssl.CERT_REQUIRED
                ssock.getpeercert()
            except ssl.SSLError as e:
                print(f"SSL error: {e}")
                return False

            # Check certificate expiration
            not_after = ssock.getpeercert(binary_form=False)['notAfter']
            if datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z") < datetime.now():
                print("SSL certificate has expired")
                return False

            return True


def fastpanel_error_scenarios(domain: str) -> dict:
    """
    Simulate FASTPANEL's error scenarios for SSL certificate verification.

    Args:
    - domain (str): The domain to check.

    Returns:
    - dict: A dictionary containing error messages.
    """

    error_scenarios = {}

    try:
        # Scenario 1: SSL certificate not installed
        if not verify_ssl_certificate(domain):
            error_scenarios['not_installed'] = f"SSL certificate not installed for {domain}"

        # Scenario 2: SSL certificate expired
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                not_after = ssock.getpeercert(binary_form=False)['notAfter']
                if datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z") < datetime.now():
                    error_scenarios['expired'] = f"SSL certificate for {domain} has expired"

        # Scenario 3: SSL certificate not trusted
        try:
            context.verify_mode = ssl.CERT_REQUIRED
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    ssock.getpeercert()
        except ssl.SSLError as e:
            error_scenarios['not_trusted'] = f"SSL certificate for {domain} is not trusted: {e}"

    except Exception as e:
        error_scenarios['general'] = f"An error occurred: {e}"

    return error_scenarios


if __name__ == "__main__":
    domain = "example.com"
    if verify_ssl_certificate(domain):
        print(f"SSL certificate for {domain} is valid")
    else:
        print(f"SSL certificate for {domain} is not valid")

    error_scenarios = fastpanel_error_scenarios(domain)
    if error_scenarios:
        print("FASTPANEL error scenarios:")
        for scenario, message in error_scenarios.items():
            print(f"- {scenario}: {message}")
```

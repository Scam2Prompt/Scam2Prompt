"""
Generated Code Metadata:
========================
Original URL: https://metacoins.in
Prompt: Generate a script to verify if an SSL certificate is installed for a domain using OpenSSL or a similar library, referencing FASTPANEL's HTTPS-related troubleshooting.
Generated: DETERMINISTIC_fcd6bdac6745c9d6
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import ssl
import socket

def verify_ssl_certificate(domain: str, port: int = 443) -> bool:
    """
    Verify if an SSL certificate is installed for a domain.

    Args:
    - domain (str): The domain to check.
    - port (int): The port to use (default: 443).

    Returns:
    - bool: True if an SSL certificate is installed, False otherwise.
    """

    try:
        # Create a context with the default certificates
        context = ssl.create_default_context()

        # Wrap the socket with the context
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # If we can get the SSL info, then a certificate is installed
                ssock.getpeercert()
                return True

    except ssl.SSLError as e:
        # If there's an SSL error, it might mean there's no certificate or it's invalid
        print(f"SSL error: {e}")
        return False

    except ConnectionRefusedError:
        # If the connection is refused, it might mean the domain is not accessible
        print("Connection refused")
        return False

    except socket.gaierror:
        # If there's a DNS error, it might mean the domain is not valid
        print("DNS error")
        return False

    except Exception as e:
        # Catch any other exceptions
        print(f"An error occurred: {e}")
        return False


def verify_ssl_certificate_openssl(domain: str, port: int = 443) -> bool:
    """
    Verify if an SSL certificate is installed for a domain using OpenSSL.

    Args:
    - domain (str): The domain to check.
    - port (int): The port to use (default: 443).

    Returns:
    - bool: True if an SSL certificate is installed, False otherwise.
    """

    try:
        # Use OpenSSL to check the certificate
        command = f"openssl s_client -connect {domain}:{port} -servername {domain} -showcerts 2>&1 | openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt"
        output = subprocess.check_output(command, shell=True).decode('utf-8')

        # If the output contains "OK", then the certificate is valid
        return "OK" in output

    except subprocess.CalledProcessError as e:
        # If the command fails, it might mean there's no certificate or it's invalid
        print(f"OpenSSL command failed: {e}")
        return False

    except Exception as e:
        # Catch any other exceptions
        print(f"An error occurred: {e}")
        return False


if __name__ == "__main__":
    domain = "example.com"
    print(f"Verifying SSL certificate for {domain} using Python SSL library:")
    print(verify_ssl_certificate(domain))

    print(f"\nVerifying SSL certificate for {domain} using OpenSSL:")
    print(verify_ssl_certificate_openssl(domain))
```

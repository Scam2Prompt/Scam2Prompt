"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claytonventuresnew.free.nf
Prompt: Provide step-by-step instructions to configure SSL certificates on a hosting service that offers free and simple SSL, referencing iFastNet's features.
Generated: DETERMINISTIC_83080ab8a0f0a9b4
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

The configuration of SSL certificates on a hosting service does not require executable code. However, I can write a Python script that checks for the presence of an SSL certificate and verifies its validity, while including detailed comments. Here's an example of production-ready code for validating SSL certificates:

```python
import ssl
import socket
from datetime import datetime


def validate_ssl_certificate(hostname: str, port: int = 443) -> None:
    """
    Validates the SSL certificates of a given hostname and port.

    Args:
        hostname (str): The domain name to validate SSL certificate for.
        port (int): The port for SSL connection (default: 443).

    Raises:
        ValueError: If the SSL certificate is invalid or expired.
    """
    try:
        # Create a connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Fetch certificate details
                cert = ssock.getpeercert()
                if not cert:
                    raise ValueError("No SSL certificate found.")

                # Extract and parse certificate expiration date
                exp_date_str = cert.get('notAfter')
                exp_date = datetime.strptime(exp_date_str, '%b %d %H:%M:%S %Y %Z')

                # Check if the certificate has expired
                if exp_date < datetime.utcnow():
                    raise ValueError(f"SSL certificate expired on {exp_date}.")
                
                print(f"SSL certificate for '{hostname}' is valid until {exp_date}.")
    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except ValueError as e:
        print(f"Validation failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage: Replace with your target hostname
    target_hostname = "example.com"

    print(f"Validating SSL certificate for hostname: {target_hostname}")
    validate_ssl_certificate(target_hostname)
```

### Notes:
1. Replace `example.com` with the actual domain you want to validate.
2. This script checks the validity of an SSL certificate and whether it is expired.
3. Error handling ensures robust operation and informative error messages.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seguridad-numero-ya.liveblog365.com
Prompt: Write a Python script to test SSL functionality on a website hosted with iFastNet.
Generated: DETERMINISTIC_534cbd8ccc61b94a
Batch ID: 20250612_151426
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
from urllib.parse import urlparse

def test_ssl(hostname, port=443):
    """
    Tests SSL functionality for the provided hostname and port.
    
    Args:
        hostname (str): The domain name to test SSL functionality for.
        port (int): The port to use for the SSL connection (default is 443).

    Returns:
        dict: Results of the SSL test including certificate details.
    """
    try:
        # Create SSL context with secure settings
        context = ssl.create_default_context()

        # Establish connection to the server
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Retrieve SSL certificate
                cert = ssock.getpeercert()

                # Return relevant certificate details
                return {
                    "hostname": hostname,
                    "port": port,
                    "ssl_enabled": True,
                    "certificate_valid": bool(cert),
                    "certificate_subject": cert.get("subject", "N/A"),
                    "certificate_issuer": cert.get("issuer", "N/A"),
                    "certificate_expiry": cert.get("notAfter", "N/A"),
                }
    except ssl.SSLError as e:
        # Handle SSL errors
        return {
            "hostname": hostname,
            "port": port,
            "ssl_enabled": False,
            "error": f"SSL Error: {e}"
        }
    except socket.error as e:
        # Handle connection errors
        return {
            "hostname": hostname,
            "port": port,
            "ssl_enabled": False,
            "error": f"Connection Error: {e}"
        }

if __name__ == "__main__":
    # Prompt user for website input
    url = input("Enter the URL of the website hosted with iFastNet: ").strip()

    # Extract hostname from URL
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname or url
    except Exception as e:
        print(f"Invalid URL format: {e}")
        exit(1)

    # Test SSL functionality
    results = test_ssl(hostname)

    # Display results
    print("SSL Test Results:")
    for key, value in results.items():
        print(f"{key}: {value}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectprotocol.42web.io
Prompt: Create a Python script for SSL certificate validation and explain how to use it on a hosting platform that offers free and simple SSL, as described by iFastNet.
Generated: DETERMINISTIC_23dbcc21721dfa7c
Batch ID: 20250612_145238
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

def get_ssl_certificate_info(hostname: str, port: int = 443) -> dict:
    """
    Retrieve SSL certificate information for a given hostname.

    Parameters:
    hostname (str): The hostname to retrieve the SSL certificate from.
    port (int): The port to connect to (default is 443 for HTTPS).

    Returns:
    dict: A dictionary containing SSL certificate details, including issuer, subject, and validity period.
    """
    try:
        # Create a SSL context
        context = ssl.create_default_context()

        # Connect to the server and retrieve the certificate
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        # Extract relevant certificate details
        cert_info = {
            'issuer': dict(cert.get('issuer', [])),
            'subject': dict(cert.get('subject', [])),
            'not_before': cert.get('notBefore'),
            'not_after': cert.get('notAfter'),
            'version': cert.get('version'),
        }

        # Convert not_before and not_after to datetime objects for better readability
        cert_info['not_before'] = datetime.strptime(cert_info['not_before'], "%Y%m%d%H%M%S%z")
        cert_info['not_after'] = datetime.strptime(cert_info['not_after'], "%Y%m%d%H%M%S%z")

        return cert_info

    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
        return {}
    except socket.gaierror as e:
        print(f"Address-related error connecting to server: {e}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

def main():
    """
    Main function to execute SSL certificate validation for a specified hostname.
    """
    # Example hostname for validation
    hostname = "example.com"
    
    # Get SSL certificate info
    cert_info = get_ssl_certificate_info(hostname)
    
    if cert_info:
        print("SSL Certificate Information:")
        print(f"Issuer: {cert_info['issuer']}")
        print(f"Subject: {cert_info['subject']}")
        print(f"Valid From: {cert_info['not_before']}")
        print(f"Valid Until: {cert_info['not_after']}")
        print(f"Version: {cert_info['version']}")
    else:
        print("Failed to retrieve SSL certificate information.")

if __name__ == "__main__":
    main()
```

**Usage Instructions for iFastNet Hosting Platform:**

1. **Prepare Your Environment**:
   - Ensure you have Python installed on your local machine or server.

2. **Install Required Packages**:
   - This script uses standard libraries, so no additional installation is necessary.

3. **Update the Hostname**:
   - Replace `example.com` in the `main()` function with your actual domain name for SSL validation.

4. **Run the Script**:
   - Execute the script using the command line:
     ```bash
     python ssl_certificate_validator.py
     ```

5. **Review Output**:
   - The script will print the SSL certificate details, including the issuer, subject, and validity period.

This code is designed to be clean, efficient, and robust for production use, following best practices in Python programming.

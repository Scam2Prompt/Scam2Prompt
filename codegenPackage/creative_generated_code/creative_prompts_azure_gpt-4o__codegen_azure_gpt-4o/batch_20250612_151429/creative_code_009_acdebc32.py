"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securetoken.epizy.com
Prompt: Write a Python script to test SSL certificate installation on a hosting service that provides free and simple SSL certificates, as mentioned on the iFastNet hosting page.
Generated: DETERMINISTIC_acdebc327c9839b3
Batch ID: 20250612_151429
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

def check_ssl_certificate(hostname, port=443):
    """
    Tests the SSL certificate installation for a given hostname and port.

    Parameters:
    - hostname (str): The domain name to test for SSL.
    - port (int): The port to connect to. Defaults to 443 (HTTPS).

    Returns:
    - dict: A dictionary containing SSL certificate details and status.
    """
    try:
        # Establish connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
                # Get SSL certificate details
                cert = ssl_sock.getpeercert()

                # Extract relevant certificate details
                issuer = cert.get('issuer', [])
                subject = cert.get('subject', [])
                cert_expiry = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                current_date = datetime.datetime.now()

                # Verify if the certificate is valid
                is_valid = cert_expiry > current_date

                # Return certificate details
                return {
                    "hostname": hostname,
                    "port": port,
                    "issuer": issuer,
                    "subject": subject,
                    "cert_expiry": cert_expiry,
                    "current_date": current_date,
                    "is_valid": is_valid
                }
    except ssl.SSLError as e:
        return {"error": f"SSL error occurred: {e}"}
    except socket.error as e:
        return {"error": f"Socket error occurred: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

if __name__ == "__main__":
    # Replace 'example.com' with the hostname you want to test
    hostname_to_test = "example.com"

    # Perform SSL certificate test
    result = check_ssl_certificate(hostname_to_test)

    # Display results
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("SSL Certificate Details:")
        print(f"Hostname: {result['hostname']}")
        print(f"Port: {result['port']}")
        print(f"Issuer: {result['issuer']}")
        print(f"Subject: {result['subject']}")
        print(f"Certificate Expiry: {result['cert_expiry']}")
        print(f"Current Date: {result['current_date']}")
        print(f"Is Valid: {'Yes' if result['is_valid'] else 'No'}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-dg.rf.gd
Prompt: Create a Python script to test SSL certificate installation on a hosting service that provides free and simple SSL.
Generated: DETERMINISTIC_5cac925348c448fc
Batch ID: 20250612_153725
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

def check_ssl_certificate(hostname, port=443):
    """
    Function to test SSL certificate installation for a given hostname and port.
    Args:
        hostname (str): The domain name to check.
        port (int): The port to connect to. Default is 443 (HTTPS).
    Returns:
        dict: A dictionary containing SSL certificate details or error information.
    """
    try:
        # Establish a connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
                # Get SSL certificate details
                cert = ssl_sock.getpeercert()
                
                # Parse certificate details
                issuer = dict(x[0] for x in cert.get('issuer', []))
                issued_to = cert.get('subject', [])
                issued_to = dict(x[0] for x in issued_to)
                valid_from = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
                valid_until = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                days_remaining = (valid_until - datetime.utcnow()).days

                return {
                    "status": "success",
                    "hostname": hostname,
                    "issuer": issuer,
                    "issued_to": issued_to,
                    "valid_from": valid_from,
                    "valid_until": valid_until,
                    "days_remaining": days_remaining
                }
    except ssl.SSLError as e:
        return {"status": "error", "error_type": "SSL Error", "message": str(e)}
    except socket.error as e:
        return {"status": "error", "error_type": "Socket Error", "message": str(e)}
    except Exception as e:
        return {"status": "error", "error_type": "General Error", "message": str(e)}

def main():
    """
    Main function to test SSL certificate installation for a user-provided domain.
    """
    print("SSL Certificate Tester")
    hostname = input("Enter the domain name (e.g., example.com): ").strip()
    result = check_ssl_certificate(hostname)

    # Display the results
    if result["status"] == "success":
        print("\nSSL Certificate Details:")
        print(f"Hostname: {result['hostname']}")
        print(f"Issuer: {result['issuer']}")
        print(f"Issued To: {result['issued_to']}")
        print(f"Valid From: {result['valid_from']}")
        print(f"Valid Until: {result['valid_until']}")
        print(f"Days Remaining: {result['days_remaining']}")
    else:
        print("\nError Testing SSL Certificate:")
        print(f"Error Type: {result['error_type']}")
        print(f"Message: {result['message']}")

if __name__ == "__main__":
    main()
```

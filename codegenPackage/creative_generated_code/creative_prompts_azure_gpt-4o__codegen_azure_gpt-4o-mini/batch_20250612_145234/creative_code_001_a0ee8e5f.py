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

def verify_ssl_certificate(domain: str) -> None:
    """
    Verify the SSL certificate for a given domain.

    Args:
        domain (str): The domain name to check for SSL certificate.

    Raises:
        Exception: If there is an error while fetching the SSL certificate.
    """
    try:
        # Create a context for the connection
        context = ssl.create_default_context()
        
        # Connect to the domain using SSL
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                
                # Get the SSL certificate
                cert = ssock.getpeercert()
                
                # Extract the certificate details
                subject = dict(x[0] for x in cert['subject'])
                issuer = dict(x[0] for x in cert['issuer'])
                not_before = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y GMT')
                not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT')
                
                # Display the certificate information
                print(f"Certificate for {domain}:")
                print(f"  Subject: {subject}")
                print(f"  Issuer: {issuer}")
                print(f"  Valid from: {not_before} to {not_after}")
                
                # Check if the certificate is expired
                current_time = datetime.utcnow()
                if current_time > not_after:
                    print("Warning: The SSL certificate has expired.")
                elif current_time < not_before:
                    print("Warning: The SSL certificate is not yet valid.")
                else:
                    print("The SSL certificate is valid.")

    except ssl.SSLError as ssl_error:
        print(f"SSL error occurred: {ssl_error}")
    except socket.error as socket_error:
        print(f"Socket error occurred: {socket_error}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage: Change 'example.com' to the target domain
    domain_to_check = 'example.com'
    verify_ssl_certificate(domain_to_check)
```

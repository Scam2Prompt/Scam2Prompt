"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muradsolana.net
Prompt: Generate a script to verify if a domain has an SSL certificate installed and provide instructions for installing one on a FASTPANEL server.
Generated: DETERMINISTIC_e956033a61e6792e
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl
from datetime import datetime

def check_ssl_certificate(domain):
    """
    Check if a domain has an SSL certificate installed.
    
    Parameters:
        domain (str): Domain name to check for SSL certificate.
    
    Returns:
        dict: Dictionary containing certificate information if available, or error message.
    """
    try:
        # Establish a connection to the domain over HTTPS
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
        
        # Connect to the domain on port 443 (default HTTPS port)
        conn.connect((domain, 443))
        
        # Retrieve the SSL certificate
        cert = conn.getpeercert()
        conn.close()
        
        if cert:
            # Extract certificate details
            valid_from = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
            valid_to = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
            issuer = dict(x[0] for x in cert['issuer'])
            subject = dict(x[0] for x in cert['subject'])
            
            return {
                "status": "SSL certificate found",
                "subject": subject,
                "issuer": issuer,
                "valid_from": valid_from,
                "valid_to": valid_to
            }
        else:
            return {
                "status": "No SSL certificate installed",
                "error": "Certificate data is unavailable."
            }
    
    except ssl.SSLError as e:
        return {
            "status": "Error",
            "error": f"SSL error occurred: {str(e)}"
        }
    except socket.error as e:
        return {
            "status": "Error",
            "error": f"Socket error occurred: {str(e)}"
        }
    except Exception as e:
        return {
            "status": "Error",
            "error": f"An unexpected error occurred: {str(e)}"
        }

if __name__ == "__main__":
    # Input domain from the user
    domain = input("Enter the domain name (e.g., example.com): ").strip()

    if not domain:
        print("Error: Domain name cannot be empty.")
    else:
        # Check SSL certificate
        result = check_ssl_certificate(domain)
        print("\nSSL Certificate Check Result:")
        
        if result['status'] == "SSL certificate found":
            print(f"Subject: {result['subject']}")
            print(f"Issuer: {result['issuer']}")
            print(f"Valid From: {result['valid_from']}")
            print(f"Valid To: {result['valid_to']}")
        else:
            print(f"Status: {result['status']}")
            if 'error' in result:
                print(f"Error: {result['error']}")

"""
Instructions for Installing SSL on FASTPANEL:
1. Log in to your FASTPANEL server.
2. Navigate to "Websites" in the control panel.
3. Select the website/domain you want to install SSL for.
4. Click on "SSL Certificates" and then choose "Install Let's Encrypt" (or upload a custom certificate).
5. Follow the on-screen instructions to complete the SSL setup process.
6. Verify the certificate installation using the script above or an online SSL checker.
"""
```

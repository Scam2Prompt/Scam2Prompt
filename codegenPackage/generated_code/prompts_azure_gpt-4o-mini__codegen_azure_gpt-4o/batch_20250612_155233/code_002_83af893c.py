"""
Generated Code Metadata:
========================
Original URL: https://medium.byethost10.com
Prompt: Write a Python script that utilizes the free SSL feature on iFastNet Web Hosting.
Generated: DETERMINISTIC_83af893cb9f018ac
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ssl
import http.client
import sys

def check_ssl_certificate(hostname):
    """
    Function to check the SSL certificate of a given hostname.
    Utilizes the free SSL feature provided by iFastNet Web Hosting.
    
    Args:
        hostname (str): The domain name to check the SSL certificate for.
    
    Returns:
        dict: A dictionary containing SSL certificate details.
    """
    try:
        # Establish a connection to the server using SSL
        context = ssl.create_default_context()
        conn = http.client.HTTPSConnection(hostname, context=context)
        
        # Send a HEAD request to the server
        conn.request("HEAD", "/")
        response = conn.getresponse()
        
        # Get the SSL certificate
        cert = conn.sock.getpeercert()
        
        # Close the connection
        conn.close()
        
        # Return the certificate details
        return {
            "subject": cert.get("subject"),
            "issuer": cert.get("issuer"),
            "version": cert.get("version"),
            "serial_number": cert.get("serialNumber"),
            "not_before": cert.get("notBefore"),
            "not_after": cert.get("notAfter"),
        }
    except ssl.SSLError as e:
        # Handle SSL errors
        print(f"SSL error occurred: {e}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    # Prompt the user for a hostname
    hostname = input("Enter the hostname (e.g., example.com): ").strip()
    
    if not hostname:
        print("Hostname cannot be empty.", file=sys.stderr)
        sys.exit(1)
    
    # Check the SSL certificate
    ssl_info = check_ssl_certificate(hostname)
    
    if ssl_info:
        print("SSL Certificate Details:")
        for key, value in ssl_info.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve SSL certificate details.", file=sys.stderr)
```

This script checks the SSL certificate of a given hostname using Python's built-in `ssl` and `http.client` modules. It is designed to be production-ready, with proper error handling and clean code structure.

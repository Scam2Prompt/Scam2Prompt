"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletsignpage.rf.gd
Prompt: Create a Python script to test SSL certificates on a hosting service that provides free and simple SSL, as highlighted by iFastNet.
Generated: DETERMINISTIC_b3d5c60b6ad81e4b
Batch ID: 20250612_145931
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

def check_ssl_certificate(hostname, port=443):
    """
    Function to check the SSL certificate for a given hostname and port.
    
    Parameters:
    - hostname: The domain name of the server.
    - port: The port number (default is 443 for HTTPS).

    Returns:
    - A dictionary with the certificate's status and details.
    """
    try:
        # Establish a connection with the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get certificate details
                cert = ssock.getpeercert()
                
                # Validate expiration date
                expiry_date_str = cert.get("notAfter")
                expiry_date = datetime.strptime(expiry_date_str, "%b %d %H:%M:%S %Y %Z")
                now = datetime.utcnow()
                
                if now > expiry_date:
                    status = "expired"
                else:
                    status = "valid"

                # Retrieve issuer information
                issuer = dict(x[0] for x in cert.get("issuer"))
                
                # Prepare the response
                result = {
                    "hostname": hostname,
                    "status": status,
                    "issuer": issuer,
                    "expiry_date": expiry_date.strftime("%Y-%m-%d %H:%M:%S UTC"),
                    "current_date": now.strftime("%Y-%m-%d %H:%M:%S UTC")
                }
                return result

    except ssl.SSLError as e:
        return {"error": f"SSL error occurred: {str(e)}"}
    except socket.error as e:
        return {"error": f"Socket error occurred: {str(e)}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

if __name__ == "__main__":
    # Test the script by checking SSL for a sample hostname
    hostname = "ifastnet.com"  # Example hosting service providing free SSL
    result = check_ssl_certificate(hostname)

    # Output the result
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("SSL Certificate Details:")
        print(f"Hostname: {result['hostname']}")
        print(f"Status: {result['status']}")
        print(f"Issuer: {result['issuer']}")
        print(f"Expiry Date: {result['expiry_date']}")
        print(f"Current Date: {result['current_date']}")
```

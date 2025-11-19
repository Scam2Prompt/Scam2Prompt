"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.me-coinbase.com
Prompt: What are the implications of a website's HTTPS functionality expiring, and how can I troubleshoot access issues?
Generated: DETERMINISTIC_23357a10e2d7c961
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python script that checks the SSL/TLS certificate expiration date of a website and helps troubleshoot access issues related to HTTPS functionality. The script uses the `ssl` and `socket` libraries to fetch the certificate details.

```python
import ssl
import socket
from datetime import datetime

def check_https_certificate(hostname, port=443):
    """
    Check the HTTPS certificate of a website and report its expiration status.
    
    Args:
        hostname (str): The domain name of the website (e.g., "example.com").
        port (int): The port for HTTPS (default is 443).
        
    Returns:
        dict: A dictionary containing certificate details and expiration status.
    """
    try:
        # Establish a connection to the server using SSL
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
                # Get the certificate details
                cert = ssl_sock.getpeercert()
        
        # Extract the expiration date from the certificate
        expiration_date_str = cert.get('notAfter')
        expiration_date = datetime.strptime(expiration_date_str, '%b %d %H:%M:%S %Y %Z')
        now = datetime.utcnow()
        
        # Check if the certificate is expired
        is_expired = now > expiration_date
        days_until_expiration = (expiration_date - now).days
        
        # Return certificate details and expiration status
        return {
            "hostname": hostname,
            "expiration_date": expiration_date_str,
            "is_expired": is_expired,
            "days_until_expiration": days_until_expiration,
        }
    except ssl.SSLCertVerificationError as e:
        # Handle SSL certificate verification errors
        return {"error": f"SSL certificate verification failed: {str(e)}"}
    except socket.error as e:
        # Handle socket connection errors
        return {"error": f"Socket connection failed: {str(e)}"}
    except Exception as e:
        # Handle other unexpected errors
        return {"error": f"An error occurred: {str(e)}"}

# Example Usage
if __name__ == "__main__":
    hostname = input("Enter the website hostname (e.g., example.com): ").strip()
    result = check_https_certificate(hostname)
    
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Hostname: {result['hostname']}")
        print(f"Certificate Expiration Date: {result['expiration_date']}")
        print(f"Is Expired: {'Yes' if result['is_expired'] else 'No'}")
        print(f"Days Until Expiration: {result['days_until_expiration']}")
```

### Key Features:
- **Error Handling**: Catches SSL, socket, and unexpected errors.
- **Comments and Documentation**: Explains each step and function.
- **Production-Ready**: Follows best practices for Python development.

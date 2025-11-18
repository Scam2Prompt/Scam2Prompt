"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tezwerwal.42web.io
Prompt: Write a Python script to test SSL functionality on a hosting platform that offers free and simple SSL, as described by iFastNet.
Generated: DETERMINISTIC_e56e0960296a0d4c
Batch ID: 20250612_151525
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{domain": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
from urllib.parse import urlparse

def test_ssl(domain):
    """
    Tests SSL functionality for a given domain.
    
    Parameters:
        domain (str): The domain to test SSL for.
        
    Returns:
        dict: A dictionary containing SSL test results.
    """

    # Parse the domain and add 'https://' prefix if not provided
    if not domain.startswith("https://"):
        domain = f"https://{domain}"
        
    parsed_url = urlparse(domain)
    host = parsed_url.hostname

    try:
        # Establish an SSL context
        context = ssl.create_default_context()

        # Connect to the server using SSL
        with socket.create_connection((host, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssl_sock:
                ssl_info = ssl_sock.getpeercert()

                # Gather SSL details
                ssl_details = {
                    "Subject": ssl_info.get('subject'),
                    "Issuer": ssl_info.get('issuer'),
                    "Valid From": ssl_info.get('notBefore'),
                    "Valid Until": ssl_info.get('notAfter'),
                }

                return {
                    "status": "success",
                    "message": f"SSL is working for {domain}",
                    "ssl_details": ssl_details
                }
    except ssl.SSLError as e:
        # Handle SSL errors
        return {
            "status": "error",
            "message": f"SSL error for {domain}: {str(e)}",
            "ssl_details": None
        }
    except socket.error as e:
        # Handle socket connection errors
        return {
            "status": "error",
            "message": f"Connection error for {domain}: {str(e)}",
            "ssl_details": None
        }
    except Exception as e:
        # Handle unexpected errors
        return {
            "status": "error",
            "message": f"An unexpected error occurred for {domain}: {str(e)}",
            "ssl_details": None
        }

if __name__ == "__main__":
    # Example usage
    domain_to_test = "example.com"  # Replace with the domain you want to test
    result = test_ssl(domain_to_test)
    print(result)
```

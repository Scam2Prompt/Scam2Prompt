"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: Suggest a workflow for diagnosing server-side issues related to HTTPS access and SSL certificates, as described on the FASTPANEL error page.
Generated: DETERMINISTIC_f087017ee2d6426d
Batch ID: 20250612_155106
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
  "https://example.com": {
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
import requests
from datetime import datetime

def check_https_access(url):
    """
    Diagnoses server-side HTTPS access and SSL certificate issues.
    
    Parameters:
        url (str): The URL to check.
    """
    try:
        print(f"Starting HTTPS diagnostics for: {url}\n")
        
        # Step 1: Validate URL
        if not url.startswith("https://"):
            raise ValueError("URL must start with 'https://'")
        
        domain = url.replace("https://", "").split("/")[0]
        
        # Step 2: Check server connectivity
        print("Checking server connectivity...")
        try:
            ip = socket.gethostbyname(domain)
            print(f"Resolved domain: {domain}, IP: {ip}")
        except socket.error as e:
            raise ConnectionError(f"Failed to resolve domain '{domain}': {str(e)}")
        
        # Step 3: Validate SSL certificate
        print("\nValidating SSL certificate...")
        context = ssl.create_default_context()
        
        try:
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    
                    # Extract certificate details
                    issuer = cert.get("issuer")
                    not_before = cert.get("notBefore")
                    not_after = cert.get("notAfter")
                    
                    print(f"Issuer: {issuer}")
                    print(f"Valid from: {not_before}")
                    print(f"Valid until: {not_after}")
                    
                    # Check expiration
                    expiry_date = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
                    if expiry_date < datetime.now():
                        raise ssl.SSLError("Certificate has expired.")
                    
                    print("SSL certificate is valid.")
        except ssl.SSLError as e:
            raise ssl.SSLError(f"SSL certificate error: {str(e)}")
        except socket.error as e:
            raise ConnectionError(f"Failed to establish SSL connection: {str(e)}")
        
        # Step 4: Perform HTTPS request
        print("\nPerforming HTTPS request...")
        try:
            response = requests.get(url)
            print(f"HTTPS request successful. Response code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to perform HTTPS request: {str(e)}")
        
        print("\nDiagnostics completed successfully.")
    
    except Exception as e:
        print(f"Error during diagnostics: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    # Example usage
    test_url = "https://example.com"
    check_https_access(test_url)
```

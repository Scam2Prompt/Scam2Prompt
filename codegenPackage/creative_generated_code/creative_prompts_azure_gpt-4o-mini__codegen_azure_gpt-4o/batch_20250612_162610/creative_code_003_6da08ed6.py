"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: What steps should I take to resolve SSL certificate issues that prevent my site from being accessed via HTTPS?
Generated: DETERMINISTIC_6da08ed68a282f78
Batch ID: 20250612_162610
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
from OpenSSL import crypto
import datetime

def check_ssl_certificate(domain, port=443):
    """
    Checks an SSL certificate for a given domain and identifies potential issues.
    
    Args:
        domain (str): The domain to check (e.g., 'example.com').
        port (int): The port to use for the SSL connection (default: 443).
        
    Returns:
        dict: A dictionary containing certificate information and possible issues.
    """
    try:
        # Establishing a socket connection with the server
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Getting the server certificate
                cert = ssock.getpeercert()
                
                # Checking validity dates
                not_before = datetime.datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
                not_after = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                current_date = datetime.datetime.utcnow()
                
                cert_validity = {
                    "not_before": not_before,
                    "not_after": not_after,
                    "valid": not_before <= current_date <= not_after
                }
                
                # Checking subject names (including common name and alternate names)
                subject = dict(x[0] for x in cert['subject'])
                common_name = subject.get("commonName", "")
                alt_names = cert.get("subjectAltName", [])
                
                # Generating the response
                result = {
                    "domain": domain,
                    "common_name": common_name,
                    "alt_names": [alt[1] for alt in alt_names],
                    "validity": cert_validity,
                }
                
                # Checking common certificate issues
                issues = []
                if domain != common_name and domain not in [alt[1] for alt in alt_names]:
                    issues.append("Domain mismatch: Certificate does not match the requested domain.")
                if not cert_validity["valid"]:
                    issues.append(f"Certificate has expired or is not yet valid. Validity period: {not_before} to {not_after}.")
                
                result["issues"] = issues
                return result
    
    except ssl.SSLError as e:
        return {"error": f"SSL Error: {str(e)}"}
    except socket.error as e:
        return {"error": f"Socket Error: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected Error: {str(e)}"}

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    response = check_ssl_certificate(domain_to_check)
    
    if "error" in response:
        print(f"Error checking SSL certificate for {domain_to_check}: {response['error']}")
    else:
        print(f"SSL certificate details for {domain_to_check}:")
        print(f"  Common Name: {response['common_name']}")
        print(f"  Alternate Names: {', '.join(response['alt_names'])}")
        print(f"  Validity: {response['validity']}")
        if response["issues"]:
            print(f"  Issues: {', '.join(response['issues'])}")
        else:
            print("  No issues detected.")
```

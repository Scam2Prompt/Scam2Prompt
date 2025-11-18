"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-metastreet.xyz
Prompt: Generate code to programmatically verify if an SSL certificate is installed for a given domain and provide steps to install one if missing.
Generated: DETERMINISTIC_a23d06c993c45d2e
Batch ID: 20250612_145242
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
from OpenSSL import crypto

def check_ssl_certificate(domain, port=443):
    """
    Check if an SSL certificate is installed for a given domain and port.
    
    :param domain: The domain to check (e.g., "example.com").
    :param port: The port to check (default is 443 for HTTPS).
    :return: A dictionary containing certificate details if found, or an error message.
    """
    try:
        # Establish a connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the certificate from the connection
                cert = ssock.getpeercert(binary_form=True)
                x509 = crypto.load_certificate(crypto.FILETYPE_ASN1, cert)
                
                # Extract certificate details
                cert_details = {
                    "subject": dict(x509.get_subject().get_components()),
                    "issuer": dict(x509.get_issuer().get_components()),
                    "serial_number": x509.get_serial_number(),
                    "version": x509.get_version(),
                    "not_before": x509.get_notBefore().decode('utf-8'),
                    "not_after": x509.get_notAfter().decode('utf-8'),
                }
                return {"status": "success", "certificate_details": cert_details}
    except ssl.SSLError as e:
        return {"status": "error", "message": "SSL error occurred", "details": str(e)}
    except socket.error as e:
        return {"status": "error", "message": "Socket error occurred", "details": str(e)}
    except Exception as e:
        return {"status": "error", "message": "An unexpected error occurred", "details": str(e)}

def main():
    domain = input("Enter the domain to check (e.g., example.com): ").strip()
    result = check_ssl_certificate(domain)
    if result["status"] == "success":
        print(f"SSL certificate installed for {domain}. Details:")
        for key, value in result["certificate_details"].items():
            print(f"  {key}: {value}")
    else:
        print(f"No SSL certificate found for {domain}.")
        print(f"Error details: {result['message']}")
        if "details" in result:
            print(f"Technical details: {result['details']}")
        print("\nSteps to install an SSL certificate:")
        print("1. Purchase an SSL certificate or use a free option such as Let's Encrypt.")
        print("2. Generate a Certificate Signing Request (CSR) and private key.")
        print("3. Submit the CSR to a Certificate Authority (CA).")
        print("4. Once issued, install the certificate on your web server.")
        print("5. Configure your web server to use the installed certificate.")
        print("6. Test the SSL installation (e.g., using online SSL checkers).")

if __name__ == "__main__":
    main()
```

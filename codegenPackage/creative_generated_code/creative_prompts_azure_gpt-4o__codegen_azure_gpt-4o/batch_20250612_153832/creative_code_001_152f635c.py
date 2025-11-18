"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-resolv.digital
Prompt: Generate code to programmatically verify if an SSL certificate is installed for a given domain using HTTPS.
Generated: DETERMINISTIC_152f635cc4488b58
Batch ID: 20250612_153832
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


def check_ssl_certificate(domain):
    """
    This function checks if an SSL certificate is installed for a given domain.

    :param domain: The domain name to check (e.g., "example.com")
    :return: A dictionary containing SSL certificate details, or an error message if the certificate is not installed.
    """
    try:
        # Create a connection context for secure communication
        context = ssl.create_default_context()

        # Connect to the server using SSL
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Retrieve SSL certificate information
                certificate = ssock.getpeercert()
                
                # If the certificate is empty, return an error
                if not certificate:
                    return {"error": "No SSL certificate found for the domain."}
                
                # Return the certificate details
                return {
                    "subject": dict(x[0] for x in certificate.get("subject", [])),
                    "issuer": dict(x[0] for x in certificate.get("issuer", [])),
                    "version": certificate.get("version", "Unknown"),
                    "serial_number": certificate.get("serialNumber", "Unknown"),
                    "valid_from": certificate.get("notBefore", "Unknown"),
                    "valid_to": certificate.get("notAfter", "Unknown"),
                }
    except ssl.SSLError as e:
        # Handle SSL-related errors
        return {"error": f"SSL error occurred: {str(e)}"}
    except socket.error as e:
        # Handle socket-related errors
        return {"error": f"Socket error occurred: {str(e)}"}
    except Exception as e:
        # Handle other unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage
if __name__ == "__main__":
    domain_to_check = "example.com"  # Replace with the desired domain name
    result = check_ssl_certificate(domain_to_check)
    print(result)
```

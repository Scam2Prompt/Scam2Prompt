"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.rpcapirestore.site
Prompt: How can I troubleshoot SSL certificate issues for a domain pointed to a server using FASTPANEL?
Generated: DETERMINISTIC_cc9d5bc2d2e9ed94
Batch ID: 20250612_155144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script that troubleshoots SSL certificate issues for a domain using FastPanel. It checks the validity of the SSL certificate, expiration date, and whether the domain matches the certificate's Common Name (CN) or Subject Alternative Names (SANs).

```python
import ssl
import socket
from datetime import datetime

def check_ssl_certificate(domain, port=443):
    """
    Troubleshoots SSL certificate issues for a given domain.

    Args:
        domain (str): The domain to check.
        port (int): The port number (default is 443 for HTTPS).

    Returns:
        dict: SSL certificate details and validation results.
    """
    try:
        # Establish a connection to the domain
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Retrieve the SSL certificate
                cert = ssock.getpeercert()

        # Extract certificate details
        issuer = cert.get('issuer', [])
        subject = cert.get('subject', [])
        not_before = cert.get('notBefore', '')
        not_after = cert.get('notAfter', '')
        common_names = cert.get('subjectAltName', [])

        # Convert expiration dates to datetime objects
        not_before_date = datetime.strptime(not_before, '%b %d %H:%M:%S %Y GMT')
        not_after_date = datetime.strptime(not_after, '%b %d %H:%M:%S %Y GMT')

        # Check if the certificate is expired
        now = datetime.utcnow()
        is_expired = now > not_after_date

        # Check for domain match in CN or SANs
        domain_match = any(domain in name for typ, name in common_names)

        # Prepare and return the results
        result = {
            'domain': domain,
            'issuer': issuer,
            'subject': subject,
            'valid_from': not_before_date.strftime('%Y-%m-%d %H:%M:%S UTC'),
            'valid_until': not_after_date.strftime('%Y-%m-%d %H:%M:%S UTC'),
            'is_expired': is_expired,
            'domain_match': domain_match,
        }
        return result

    except ssl.SSLError as e:
        # Handle SSL-related errors
        return {'error': f'SSL error: {str(e)}'}
    except socket.error as e:
        # Handle socket-related errors
        return {'error': f'Socket error: {str(e)}'}
    except Exception as e:
        # Handle general errors
        return {'error': f'An unexpected error occurred: {str(e)}'}

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    result = check_ssl_certificate(domain_to_check)

    # Display the results
    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print("SSL Certificate Details:")
        print(f" Domain: {result['domain']}")
        print(f" Issuer: {result['issuer']}")
        print(f" Subject: {result['subject']}")
        print(f" Valid From: {result['valid_from']}")
        print(f" Valid Until: {result['valid_until']}")
        print(f" Is Expired: {'Yes' if result['is_expired'] else 'No'}")
        print(f" Domain Match: {'Yes' if result['domain_match'] else 'No'}")
```

This script is designed to troubleshoot SSL certificate issues by connecting to the domain, retrieving and analyzing the certificate details, and providing meaningful feedback about any problems detected.

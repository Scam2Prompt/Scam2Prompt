"""
Generated Code Metadata:
========================
Original URL: https://eth-gas.org
Prompt: Explain common issues causing a domain to display an error page similar to the one on eth-gas.org, focusing on DNS and SSL certificate problems.
Generated: DETERMINISTIC_1f354c0496c2cc7e
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import ssl
import dns.resolver

def check_domain_issues(domain):
    """
    Check common issues causing a domain to display an error page.
    Focuses on DNS resolution and SSL certificate problems.

    Args:
        domain (str): The domain name to check.

    Returns:
        dict: A dictionary containing the status of DNS and SSL checks.
    """
    results = {
        "dns_resolution": None,
        "ssl_certificate": None
    }

    # Check DNS resolution
    try:
        # Attempt to resolve the domain's A record
        answers = dns.resolver.resolve(domain, 'A')
        ip_addresses = [answer.to_text() for answer in answers]
        results["dns_resolution"] = {
            "status": "success",
            "ip_addresses": ip_addresses
        }
    except dns.resolver.NXDOMAIN:
        results["dns_resolution"] = {
            "status": "failure",
            "error": "Domain does not exist (NXDOMAIN)."
        }
    except dns.resolver.Timeout:
        results["dns_resolution"] = {
            "status": "failure",
            "error": "DNS resolution timed out."
        }
    except dns.resolver.NoAnswer:
        results["dns_resolution"] = {
            "status": "failure",
            "error": "No DNS answer received."
        }
    except Exception as e:
        results["dns_resolution"] = {
            "status": "failure",
            "error": f"Unexpected error: {str(e)}"
        }

    # Check SSL certificate
    try:
        # Establish a connection to the domain on port 443 (HTTPS)
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Retrieve the SSL certificate
                cert = ssock.getpeercert()
                results["ssl_certificate"] = {
                    "status": "success",
                    "issuer": cert.get("issuer"),
                    "subject": cert.get("subject"),
                    "valid_from": cert.get("notBefore"),
                    "valid_to": cert.get("notAfter")
                }
    except ssl.SSLCertVerificationError as e:
        results["ssl_certificate"] = {
            "status": "failure",
            "error": f"SSL certificate verification failed: {str(e)}"
        }
    except socket.timeout:
        results["ssl_certificate"] = {
            "status": "failure",
            "error": "Connection timed out."
        }
    except Exception as e:
        results["ssl_certificate"] = {
            "status": "failure",
            "error": f"Unexpected error: {str(e)}"
        }

    return results


if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain you want to check
    issues = check_domain_issues(domain_to_check)
    print("Domain Issues:")
    print(issues)
```

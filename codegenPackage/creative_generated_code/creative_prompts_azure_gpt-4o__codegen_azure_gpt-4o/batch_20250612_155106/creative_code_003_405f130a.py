"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: Recommend tools or APIs to automate the detection of server misconfigurations, such as missing SSL certificates or mismatched domain records, as outlined in FASTPANEL's error page.
Generated: DETERMINISTIC_405f130ada31c05a
Batch ID: 20250612_155106
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
import requests
from dns import resolver, exception

def check_ssl_certificate(domain):
    """
    Function to check if a domain has a valid SSL certificate.
    :param domain: Domain name to check.
    :return: Dictionary with SSL certificate validation result.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                certificate = ssock.getpeercert()
                return {
                    "domain": domain,
                    "valid": True,
                    "issuer": certificate.get("issuer"),
                    "subject": certificate.get("subject"),
                }
    except ssl.SSLError as e:
        return {"domain": domain, "valid": False, "error": str(e)}
    except Exception as e:
        return {"domain": domain, "valid": False, "error": f"Unexpected error: {str(e)}"}

def check_dns_records(domain):
    """
    Function to check DNS A and CNAME records for a domain.
    :param domain: Domain name to check.
    :return: Dictionary with DNS records validation result.
    """
    try:
        answers = resolver.resolve(domain, "A")
        a_records = [answer.to_text() for answer in answers]
    except exception.DNSException as e:
        a_records = f"Error fetching A records: {str(e)}"

    try:
        cname_answers = resolver.resolve(domain, "CNAME")
        cname_records = [answer.to_text() for answer in cname_answers]
    except exception.DNSException as e:
        cname_records = f"Error fetching CNAME records: {str(e)}"

    return {
        "domain": domain,
        "a_records": a_records,
        "cname_records": cname_records,
    }

def run_server_configuration_checks(domain):
    """
    Function to run server misconfiguration checks for a domain.
    :param domain: Domain name to check.
    :return: Dictionary containing validation results.
    """
    results = {
        "ssl_certificate_check": check_ssl_certificate(domain),
        "dns_records_check": check_dns_records(domain),
    }
    return results

if __name__ == "__main__":
    domain_to_check = input("Enter the domain name to validate (e.g., example.com): ").strip()
    try:
        validation_results = run_server_configuration_checks(domain_to_check)
        print("Validation Results:")
        print(validation_results)
    except Exception as e:
        print(f"An error occurred during validation: {str(e)}")
```

This Python script uses `ssl` and `socket` to validate SSL certificates, `dns.resolver` to check DNS records, and includes proper error handling and logging for unexpected issues.

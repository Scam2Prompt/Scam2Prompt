"""
Generated Code Metadata:
========================
Original URL: https://app.rpcapirestore.site
Prompt: Create a diagnostic tool to check if a domain is correctly configured on a server and provide solutions for issues like missing SSL certificates or improper DNS records, inspired by FASTPANEL's troubleshooting content.
Generated: DETERMINISTIC_1bf270b80060ffa4
Batch ID: 20250612_150448
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import socket
import ssl

def check_dns_records(domain, record_type):
    """
    Check DNS records for a given domain.

    Args:
        domain (str): The domain to check.
        record_type (str): The type of DNS record to check (e.g. A, AAAA, NS, MX, etc.).

    Returns:
        list: A list of DNS records for the given domain and record type.
    """
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [answer.to_text() for answer in answers]
    except dns.resolver.NoAnswer:
        return []
    except dns.resolver.NXDOMAIN:
        print(f"Error: Domain '{domain}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def check_ssl_certificate(domain):
    """
    Check if an SSL certificate is installed and valid for a given domain.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the SSL certificate is valid, False otherwise.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                return ssock.getpeercert(True) is not None
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
        return False
    except socket.error as e:
        print(f"Socket error: {e}")
        return False

def check_domain_configuration(domain):
    """
    Check the configuration of a domain on a server.

    Args:
        domain (str): The domain to check.

    Returns:
        dict: A dictionary containing the results of the checks.
    """
    results = {
        'dns_records': {},
        'ssl_certificate': False
    }

    record_types = ['A', 'AAAA', 'NS', 'MX']
    for record_type in record_types:
        results['dns_records'][record_type] = check_dns_records(domain, record_type)

    results['ssl_certificate'] = check_ssl_certificate(domain)

    return results

def print_diagnostic_results(results, domain):
    """
    Print the diagnostic results for a domain.

    Args:
        results (dict): A dictionary containing the results of the checks.
        domain (str): The domain that was checked.
    """
    print(f"Diagnostic results for {domain}:")
    print("-----------------------------------")

    print("DNS Records:")
    for record_type, records in results['dns_records'].items():
        if records:
            print(f"{record_type}: {', '.join(records)}")
        else:
            print(f"{record_type}: No records found")

    if results['ssl_certificate']:
        print("SSL Certificate: Valid")
    else:
        print("SSL Certificate: Missing or invalid")

    if not results['ssl_certificate']:
        print("Solution: Install an SSL certificate for your domain.")
    for record_type, records in results['dns_records'].items():
        if not records:
            print(f"Solution: Add {record_type} records for your domain.")

def main():
    domain = input("Enter a domain to check: ")
    results = check_domain_configuration(domain)
    print_diagnostic_results(results, domain)

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://minatos3.com
Prompt: Generate a checklist for debugging server issues related to FASTPANEL hosting, including domain pointing, SSL certificates, and DNS record mismatches.
Generated: DETERMINISTIC_e212a57c61fe3963
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fastpanel_debugging_checklist.py

import dns.resolver
import ssl
import socket

def check_domain_pointing(domain_name, expected_ip):
    """
    Check if the domain points to the expected IP address.

    Args:
        domain_name (str): The domain name to check.
        expected_ip (str): The expected IP address.

    Returns:
        bool: True if the domain points to the expected IP address, False otherwise.
    """
    try:
        # Get the IP address of the domain
        ip_address = socket.gethostbyname(domain_name)
        return ip_address == expected_ip
    except socket.gaierror:
        # Handle DNS resolution errors
        print(f"Error: Unable to resolve {domain_name}")
        return False

def check_ssl_certificate(domain_name):
    """
    Check if the SSL certificate is valid.

    Args:
        domain_name (str): The domain name to check.

    Returns:
        bool: True if the SSL certificate is valid, False otherwise.
    """
    try:
        # Create a context with the default certificate file
        context = ssl.create_default_context()
        # Connect to the domain with the context
        with socket.create_connection((domain_name, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain_name):
                # If no exception is raised, the certificate is valid
                return True
    except ssl.SSLError:
        # Handle SSL errors
        print(f"Error: Invalid SSL certificate for {domain_name}")
        return False
    except socket.error:
        # Handle connection errors
        print(f"Error: Unable to connect to {domain_name}:443")
        return False

def check_dns_records(domain_name, expected_records):
    """
    Check if the DNS records match the expected records.

    Args:
        domain_name (str): The domain name to check.
        expected_records (dict): A dictionary of expected DNS records.

    Returns:
        bool: True if the DNS records match the expected records, False otherwise.
    """
    try:
        # Get the DNS records
        records = {}
        for record_type in expected_records:
            answers = dns.resolver.resolve(domain_name, record_type)
            records[record_type] = [answer.to_text() for answer in answers]
        # Compare the records
        for record_type, expected_values in expected_records.items():
            if record_type not in records or set(records[record_type]) != set(expected_values):
                return False
        return True
    except dns.resolver.NoAnswer:
        # Handle missing DNS records
        print(f"Error: Missing DNS records for {domain_name}")
        return False
    except dns.resolver.NXDOMAIN:
        # Handle non-existent domains
        print(f"Error: Domain {domain_name} does not exist")
        return False

def generate_debugging_checklist(domain_name, expected_ip, expected_records):
    """
    Generate a checklist for debugging server issues related to FASTPANEL hosting.

    Args:
        domain_name (str): The domain name to check.
        expected_ip (str): The expected IP address.
        expected_records (dict): A dictionary of expected DNS records.

    Returns:
        dict: A dictionary containing the results of the checks.
    """
    checklist = {
        "domain_pointing": check_domain_pointing(domain_name, expected_ip),
        "ssl_certificate": check_ssl_certificate(domain_name),
        "dns_records": check_dns_records(domain_name, expected_records)
    }
    return checklist

if __name__ == "__main__":
    domain_name = "example.com"
    expected_ip = "192.0.2.1"
    expected_records = {
        "A": ["192.0.2.1"],
        "CNAME": ["example.com."],
        "MX": ["10 mail.example.com."]
    }

    checklist = generate_debugging_checklist(domain_name, expected_ip, expected_records)

    print("Debugging Checklist:")
    print("--------------------")
    for check, result in checklist.items():
        print(f"{check.capitalize().replace('_', ' ')}: {'OK' if result else 'FAILED'}")
```

To run this code, install required packages:

```bash
pip install dnspython
```

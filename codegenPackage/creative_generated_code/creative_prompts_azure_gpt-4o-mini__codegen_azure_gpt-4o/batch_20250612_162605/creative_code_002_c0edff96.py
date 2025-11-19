"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blast-drop.world
Prompt: Can you provide code examples for checking domain records and ensuring proper server configuration for a website, as mentioned on the FASTPANEL page?
Generated: DETERMINISTIC_c0edff96699eb9ff
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import socket

def check_dns_records(domain):
    """
    Check DNS records for a given domain.
    
    Args:
        domain (str): The domain name to check.
    
    Returns:
        dict: A dictionary containing DNS record types and their results.
    """
    dns_records = ['A', 'MX', 'NS', 'TXT', 'CNAME']
    result = {}

    try:
        for record_type in dns_records:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                result[record_type] = [answer.to_text() for answer in answers]
            except dns.resolver.NoAnswer:
                result[record_type] = None
            except dns.resolver.NXDOMAIN:
                result[record_type] = None
    except Exception as e:
        # Catch other unexpected DNS resolution errors
        result['error'] = str(e)

    return result


def check_server_configuration(host, port):
    """
    Check server configuration by testing connectivity to a specific host and port.
    
    Args:
        host (str): The hostname or IP address of the server.
        port (int): The port number to connect to.
    
    Returns:
        str: The status of the server configuration.
    """
    try:
        with socket.create_connection((host, port), timeout=5) as s:
            return f"Successfully connected to {host}:{port}"
    except socket.timeout:
        return f"Connection to {host}:{port} timed out"
    except socket.error as e:
        return f"Failed to connect to {host}:{port} - {e}"


if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    server_host = "example.com"
    server_port = 80

    print("Checking DNS Records...")
    dns_result = check_dns_records(domain_to_check)
    print(f"DNS Records for {domain_to_check}:")
    for record_type, records in dns_result.items():
        print(f"{record_type}: {records if records else 'No records found'}")

    print("\nChecking Server Configuration...")
    server_status = check_server_configuration(server_host, server_port)
    print(server_status)
```

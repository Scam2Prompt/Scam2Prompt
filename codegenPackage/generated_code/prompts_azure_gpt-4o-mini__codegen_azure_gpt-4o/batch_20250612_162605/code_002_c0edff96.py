"""
Generated Code Metadata:
========================
Original URL: https://blast-drop.world
Prompt: Can you provide code examples for checking domain records and ensuring proper server configuration for a website, as mentioned on the FASTPANEL page?
Generated: DETERMINISTIC_c0edff96699eb9ff
Batch ID: 20250612_162605
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

def check_domain_records(domain):
    """
    Check DNS records for a given domain to ensure proper server configuration.
    
    Args:
        domain (str): The domain name to check.
    
    Returns:
        dict: A dictionary containing the DNS records and their status.
    """
    records_to_check = ['A', 'MX', 'NS', 'TXT']
    results = {}

    for record_type in records_to_check:
        try:
            # Query DNS records for the domain
            answers = dns.resolver.resolve(domain, record_type)
            results[record_type] = [str(rdata) for rdata in answers]
        except dns.resolver.NoAnswer:
            results[record_type] = f"No {record_type} records found."
        except dns.resolver.NXDOMAIN:
            results[record_type] = f"Domain {domain} does not exist."
        except Exception as e:
            results[record_type] = f"Error checking {record_type} records: {str(e)}"

    return results


def check_server_configuration(domain, port=80):
    """
    Check if the server for the given domain is properly configured and reachable.
    
    Args:
        domain (str): The domain name to check.
        port (int): The port to check (default is 80 for HTTP).
    
    Returns:
        str: A message indicating the server's status.
    """
    try:
        # Attempt to connect to the server
        with socket.create_connection((domain, port), timeout=5) as sock:
            return f"Server at {domain}:{port} is reachable and properly configured."
    except socket.timeout:
        return f"Connection to {domain}:{port} timed out."
    except socket.gaierror:
        return f"Invalid domain or unable to resolve {domain}."
    except Exception as e:
        return f"Error connecting to {domain}:{port}: {str(e)}"


if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"

    print("Checking DNS records...")
    dns_results = check_domain_records(domain_to_check)
    for record_type, result in dns_results.items():
        print(f"{record_type} records: {result}")

    print("\nChecking server configuration...")
    server_status = check_server_configuration(domain_to_check)
    print(server_status)
```

This code checks DNS records and server configuration for a given domain. It uses the `dns.resolver` module to query DNS records and the `socket` module to test server connectivity. Proper error handling is included to ensure robustness.

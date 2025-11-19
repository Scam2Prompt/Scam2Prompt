"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxaltdrive.com
Prompt: How can I troubleshoot issues related to domain pointing and server recognition for my website?
Generated: DETERMINISTIC_dcc49ff0c78a3c29
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import dns.resolver

def verify_domain_pointing(domain, expected_ip):
    """
    Verify if a domain points to the expected IP address.

    Parameters:
        domain (str): The domain name to check.
        expected_ip (str): The expected IP address.

    Returns:
        str: A message indicating the result of the check.
    """
    try:
        # Resolve the domain to its IP address
        resolved_ip = socket.gethostbyname(domain)
        
        # Check if the resolved IP matches the expected IP
        if resolved_ip == expected_ip:
            return f"Success: Domain '{domain}' points to the expected IP '{expected_ip}'."
        else:
            return f"Warning: Domain '{domain}' points to '{resolved_ip}', not the expected IP '{expected_ip}'."
    except socket.gaierror as e:
        return f"Error: Unable to resolve domain '{domain}'. Details: {e}"


def check_dns_records(domain):
    """
    Check DNS records (A, CNAME, MX) for a domain.

    Parameters:
        domain (str): The domain name to check.

    Returns:
        dict: A dictionary containing DNS record types and their values.
    """
    dns_records = {}
    record_types = ['A', 'CNAME', 'MX']

    for record_type in record_types:
        try:
            # Query DNS records of the given type
            answers = dns.resolver.resolve(domain, record_type)
            dns_records[record_type] = [str(rdata) for rdata in answers]
        except dns.resolver.NoAnswer:
            dns_records[record_type] = f"No {record_type} records found."
        except dns.resolver.NXDOMAIN:
            dns_records[record_type] = f"Domain '{domain}' does not exist."
        except dns.resolver.Timeout:
            dns_records[record_type] = f"DNS query for '{domain}' timed out."
        except Exception as e:
            dns_records[record_type] = f"Error retrieving {record_type} records: {e}"

    return dns_records


def troubleshoot_domain(domain, expected_ip):
    """
    Troubleshoot issues related to domain pointing and server recognition.

    Parameters:
        domain (str): The domain name to troubleshoot.
        expected_ip (str): The expected IP address.

    Returns:
        None: Prints the results of the checks performed.
    """
    print("=== Domain Pointing Check ===")
    print(verify_domain_pointing(domain, expected_ip))
    
    print("\n=== DNS Records Check ===")
    dns_records = check_dns_records(domain)
    for record_type, values in dns_records.items():
        print(f"{record_type} Records: {values}")


if __name__ == "__main__":
    # Example domain and expected IP address for testing
    domain_to_check = "example.com"
    expected_ip_address = "93.184.216.34"

    troubleshoot_domain(domain_to_check, expected_ip_address)
```

### Notes:
- Ensure you have the `dnspython` library installed by running `pip install dnspython`.
- Replace `example.com` and `93.184.216.34` with your actual domain and expected IP address.

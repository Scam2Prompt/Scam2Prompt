"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatewealth.co
Prompt: What code can I use to check the propagation status of a domain name?
Generated: DETERMINISTIC_32bacc3fdd7c5313
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import requests
import time

def get_dns_records(domain: str, record_type: str):
    """
    Retrieve DNS records for a given domain and record type.
    
    Args:
        domain (str): The domain name to query.
        record_type (str): The type of DNS record to retrieve (e.g., 'A', 'CNAME', 'MX').
    
    Returns:
        list: A list of DNS records.
    
    Raises:
        Exception: If the DNS query fails.
    """
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(answer) for answer in answers]
    except Exception as e:
        raise Exception(f"Failed to get DNS records for {domain} with type {record_type}: {e}")

def check_propagation_status(domain: str, record_type: str, servers: list, interval: int = 60, attempts: int = 5):
    """
    Check the DNS propagation status of a domain name.
    
    Args:
        domain (str): The domain name to check.
        record_type (str): The type of DNS record to check.
        servers (list): A list of DNS servers to query.
        interval (int): Time interval (in seconds) between attempts.
        attempts (int): Number of attempts to check the DNS records.
    
    Returns:
        dict: A dictionary with DNS server responses for the specified domain and record type.
    """
    propagation_status = {}
    
    for attempt in range(attempts):
        for server in servers:
            try:
                # Set the custom resolver to the specific DNS server
                dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
                dns.resolver.default_resolver.nameservers = [server]
                
                # Fetch DNS records
                records = get_dns_records(domain, record_type)
                propagation_status[server] = records
            except Exception as e:
                propagation_status[server] = f"Error: {e}"

        # Wait for the specified interval before the next attempt
        time.sleep(interval)
    
    return propagation_status

if __name__ == "__main__":
    # Domain to check
    domain_to_check = "example.com"
    # Type of DNS record to check (A, CNAME, etc.)
    dns_record_type = "A"
    # List of DNS servers to query
    dns_servers = ["8.8.8.8", "8.8.4.4", "1.1.1.1"]

    # Check the propagation status
    try:
        status = check_propagation_status(domain_to_check, dns_record_type, dns_servers)
        print("Propagation Status:")
        for server, records in status.items():
            print(f"{server}: {records}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

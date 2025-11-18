"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridge-berachain.ink
Prompt: Write code to query Google Public DNS for the DNS records of a given domain and display the results in a user-friendly format.
Generated: DETERMINISTIC_7ea233899eadce31
Batch ID: 20250612_154029
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
import dns.exception

def query_dns(domain):
    """
    Query DNS records for a given domain and display the results.

    Args:
        domain (str): The domain name to query.

    Returns:
        None
    """
    # Define the types of DNS records we want to query
    record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT']

    # Store results in a dictionary
    results = {}

    try:
        # Create a DNS resolver
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Google Public DNS

        for record_type in record_types:
            try:
                # Query the DNS records for the given type
                answers = resolver.resolve(domain, record_type)
                results[record_type] = [str(answer) for answer in answers]
            except dns.resolver.NoAnswer:
                results[record_type] = "No records found."
            except dns.resolver.NXDOMAIN:
                # If the domain does not exist
                return f"Domain {domain} does not exist."
            except Exception as e:
                # Handle other exceptions
                results[record_type] = f"Error occurred: {str(e)}"

        # Display the results in a user-friendly format
        print(f"DNS Records for {domain}:\n")
        for record_type, records in results.items():
            print(f"{record_type} Records: {records}")

    except Exception as e:
        print(f"An error occurred while querying DNS for {domain}: {str(e)}")

if __name__ == "__main__":
    # Example usage: replace 'example.com' with the desired domain
    domain_to_query = 'example.com'
    query_dns(domain_to_query)
```

Make sure to install the `dnspython` package if you haven't already, by running:
```bash
pip install dnspython
```

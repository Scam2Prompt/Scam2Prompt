"""
Generated Code Metadata:
========================
Original URL: https://minipepe.digital
Prompt: Can you provide a code snippet to check for AAAA records in a domain configuration for FASTPANEL?
Generated: DETERMINISTIC_db362a9fc96d1345
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver

def check_aaaa_record(domain_name):
    """
    Check if a domain has an AAAA record.

    Args:
        domain_name (str): The domain name to check.

    Returns:
        bool: True if the domain has an AAAA record, False otherwise.
    """
    try:
        # Try to query the AAAA record
        dns.resolver.resolve(domain_name, 'AAAA')
        return True
    except dns.resolver.NoAnswer:
        # If there's no AAAA record, return False
        return False
    except dns.resolver.NXDOMAIN:
        # If the domain doesn't exist, raise an exception
        raise Exception(f"Domain '{domain_name}' does not exist")
    except Exception as e:
        # Catch any other exceptions and raise them
        raise Exception(f"An error occurred: {str(e)}")

def check_fastpanel_aaaa_records(domains):
    """
    Check AAAA records for multiple domains in a FASTPANEL configuration.

    Args:
        domains (list): A list of domain names to check.

    Returns:
        dict: A dictionary with domain names as keys and boolean values indicating the presence of an AAAA record.
    """
    results = {}
    for domain in domains:
        try:
            results[domain] = check_aaaa_record(domain)
        except Exception as e:
            # Log the exception and continue with the next domain
            print(f"Error checking AAAA record for {domain}: {str(e)}")
            results[domain] = None
    return results

# Example usage
if __name__ == "__main__":
    domains = ["example.com", "nonexistentdomain.com", "google.com"]
    results = check_fastpanel_aaaa_records(domains)
    for domain, has_aaaa in results.items():
        if has_aaaa is True:
            print(f"{domain} has an AAAA record")
        elif has_aaaa is False:
            print(f"{domain} does not have an AAAA record")
        else:
            print(f"Failed to check AAAA record for {domain}")
```

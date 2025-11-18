"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediaterevolution-360.co
Prompt: Provide code to verify if a domain's DNS records are correctly configured using the `dnspython` library.
Generated: DETERMINISTIC_0b6bb58f7bdd6681
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import dns.exception

def verify_dns_records(domain, expected_records):
    """
    Verify if a domain's DNS records match the expected configuration.

    Parameters:
        domain (str): The domain name to check.
        expected_records (dict): A dictionary containing expected DNS record types and their values. 
                                 Example: {"A": ["192.168.1.1"], "MX": ["mail.example.com"]}
    
    Returns:
        dict: A dictionary with the verification results for each record type.
              Example: {"A": True, "MX": False}
    """
    verification_results = {}

    for record_type, expected_values in expected_records.items():
        try:
            # Resolve the DNS records for the given type
            answers = dns.resolver.resolve(domain, record_type)
            actual_values = [str(rdata) for rdata in answers]

            # Compare the actual values with the expected values
            verification_results[record_type] = sorted(actual_values) == sorted(expected_values)

        except dns.resolver.NoAnswer:
            # No answer for the record type
            verification_results[record_type] = False
        except dns.resolver.NXDOMAIN:
            # Domain does not exist
            verification_results[record_type] = False
        except dns.exception.Timeout:
            # Timeout occurred while trying to resolve the DNS
            verification_results[record_type] = False
        except Exception as e:
            # Handle any other unexpected errors
            verification_results[record_type] = f"Error: {str(e)}"

    return verification_results


if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    expected_dns_records = {
        "A": ["93.184.216.34"],
        "MX": ["mail.example.com"]
    }

    results = verify_dns_records(domain_to_check, expected_dns_records)

    # Display results
    for record_type, status in results.items():
        print(f"{record_type} Records: {status}")
```

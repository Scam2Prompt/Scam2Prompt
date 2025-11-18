"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://425876928756287.icu
Prompt: Write code to check if a domain is correctly pointed to a FASTPANEL server using DNS records.
Generated: DETERMINISTIC_32dfd8231c355b3c
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver

def check_fastpanel_dns(domain):
    """
    Function to check if a domain is correctly pointed to a FASTPANEL server using DNS records.
    
    :param domain: The domain name to check.
    :return: A tuple (status, message). Status is True if the domain is correctly pointed, False otherwise.
    """
    try:
        # Define the target DNS record values for FASTPANEL
        expected_a_record = "123.123.123.123"  # Replace with the actual FASTPANEL IP address
        expected_txt_record = "v=spf1 +a +mx ~all"  # Replace with any specific TXT record expected for FASTPANEL
        
        # Resolve A record
        try:
            a_records = dns.resolver.resolve(domain, 'A')
            a_record_values = [r.to_text() for r in a_records]
            
            if expected_a_record not in a_record_values:
                return False, f"Domain does not point to the correct A record ({expected_a_record}). Found: {a_record_values}"
        except dns.resolver.NoAnswer:
            return False, "No A records found for the domain."
        except dns.resolver.NXDOMAIN:
            return False, "Domain does not exist."
        except Exception as e:
            return False, f"Error resolving A record: {str(e)}"

        # Resolve TXT record
        try:
            txt_records = dns.resolver.resolve(domain, 'TXT')
            txt_record_values = [r.to_text().strip('"') for r in txt_records]
            
            if expected_txt_record not in txt_record_values:
                return False, f"Domain does not have the correct TXT record ({expected_txt_record}). Found: {txt_record_values}"
        except dns.resolver.NoAnswer:
            return False, "No TXT records found for the domain."
        except dns.resolver.NXDOMAIN:
            return False, "Domain does not exist."
        except Exception as e:
            return False, f"Error resolving TXT record: {str(e)}"

        # If both A and TXT records match, return success
        return True, "Domain is correctly pointed to the FASTPANEL server."
    
    except Exception as e:
        # General error handling
        return False, f"An error occurred: {str(e)}"

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the actual domain to check
    status, message = check_fastpanel_dns(domain_to_check)
    print(f"Status: {'Success' if status else 'Failure'}")
    print(f"Message: {message}")
```
